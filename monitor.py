#!/usr/bin/env python3
"""Autoresearch experiment monitor TUI.

Run from any terminal — monitors ongoing training started elsewhere:
    uv run --group monitor python monitor.py

Keyboard shortcuts:
    r / f5   Refresh results table
    q        Quit
"""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

import psutil
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import DataTable, Footer, Header, Label, RichLog, Static

PROJECT_ROOT = Path(__file__).parent
RUN_LOG = PROJECT_ROOT / "run.log"
RESULTS_TSV = PROJECT_ROOT / "results.tsv"


def _is_training() -> bool:
    for proc in psutil.process_iter(["cmdline"]):
        try:
            if "train.py" in " ".join(proc.info["cmdline"] or []):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False


class SystemBar(Static):
    def on_mount(self) -> None:
        self._update()
        self.set_interval(2.0, self._update)

    def _update(self) -> None:
        cpu = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()
        used, total = mem.used / 1024 ** 3, mem.total / 1024 ** 3
        running = _is_training()
        status = "[bold green]▶ TRAINING[/]" if running else "[bold yellow]⏸ IDLE[/]"
        ts = datetime.now().strftime("%H:%M:%S")
        self.update(
            f" CPU [cyan]{cpu:.0f}%[/]  RAM [cyan]{used:.1f}/{total:.0f} GB[/]"
            f"  {status}  [dim]{ts}[/]"
        )


class LiveLog(RichLog):
    """Tails run.log, handling \\r-overwritten progress lines."""

    _pos: int = 0

    def on_mount(self) -> None:
        self.border_title = "Training Log  (live)"
        self.set_interval(0.4, self._poll)

    def _poll(self) -> None:
        if not RUN_LOG.exists():
            return
        size = RUN_LOG.stat().st_size
        if size < self._pos:          # new run reset the file
            self.clear()
            self._pos = 0
        if size == self._pos:
            return
        with open(RUN_LOG, "rb") as f:
            f.seek(self._pos)
            raw = f.read()
        self._pos = size
        text = raw.decode("utf-8", errors="replace")
        for chunk in text.split("\n"):
            segment = chunk.split("\r")[-1].rstrip()
            if segment:
                self.write(segment)


class ResultsTable(DataTable):
    """results.tsv experiment history, auto-refreshes every 5 s."""

    _row_count: int = 0

    def on_mount(self) -> None:
        self.border_title = "Experiment History"
        self.cursor_type = "row"
        self.add_columns("commit", "val_bpb", "mem_gb", "status", "description")
        self._load()
        self.set_interval(5.0, self._load)

    def _load(self) -> None:
        if not RESULTS_TSV.exists():
            return
        with open(RESULTS_TSV, newline="") as f:
            rows = list(csv.DictReader(f, delimiter="\t"))
        if len(rows) == self._row_count:
            return
        self.clear()
        self._row_count = 0
        for row in rows:
            s = row.get("status", "")
            styled = (
                f"[green]{s}[/]" if s == "keep"
                else f"[yellow]{s}[/]" if s == "discard"
                else f"[red]{s}[/]"
            )
            self.add_row(
                row.get("commit", ""),
                row.get("val_bpb", ""),
                row.get("memory_gb", ""),
                styled,
                (row.get("description") or "")[:50],
            )
            self._row_count += 1

    def refresh_now(self) -> None:
        self._row_count = 0
        self._load()


class Monitor(App):
    TITLE = "autoresearch monitor"
    CSS = """
    Screen { background: $background; }
    #main { height: 1fr; }
    #left  { width: 1fr; border: solid $accent; }
    #right { width: 1fr; border: solid $primary; margin-left: 1; }
    LiveLog      { height: 1fr; }
    ResultsTable { height: 1fr; }
    .lbl {
        height: 1; text-align: center; width: 100%;
        background: $accent; color: $background;
    }
    #right .lbl { background: $primary; }
    SystemBar { height: 1; background: $panel; padding: 0 1; }
    """

    BINDINGS = [
        ("r", "refresh", "Refresh"),
        ("f5", "refresh", "Refresh"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="main"):
            with Vertical(id="left"):
                yield Label("▶  Training Log  (live)", classes="lbl")
                yield LiveLog(id="log", markup=False, highlight=False, max_lines=2000)
            with Vertical(id="right"):
                yield Label("◆  Experiment History", classes="lbl")
                yield ResultsTable(id="results")
        yield SystemBar()
        yield Footer()

    def action_refresh(self) -> None:
        self.query_one(ResultsTable).refresh_now()


if __name__ == "__main__":
    Monitor().run()
