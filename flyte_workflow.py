#!/usr/bin/env python3
"""Flyte 2 workflow for autoresearch experiments.

Launch a run:
    uv run --group monitor pyflyte run flyte_workflow.py experiment --description "my note"

Or directly (local Python execution, no cluster needed):
    uv run --group monitor python flyte_workflow.py "my note"
"""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from flytekit import task, workflow

PROJECT_ROOT = Path(__file__).parent
RUN_LOG = PROJECT_ROOT / "run.log"


def _parse_metrics(text: str) -> dict:
    keys = [
        "val_bpb", "training_seconds", "total_seconds",
        "peak_vram_mb", "mfu_percent", "total_tokens_M",
        "num_steps", "num_params_M", "depth",
    ]
    metrics: dict = {}
    for key in keys:
        m = re.search(rf"^{key}:\s+([0-9.]+)", text, re.MULTILINE)
        if m:
            metrics[key] = float(m.group(1))
    return metrics


@task(cache=False)
def train(description: str = "") -> dict:
    """Run one training experiment, stream output to run.log, return metrics."""
    RUN_LOG.write_text("")  # reset log for this run

    with open(RUN_LOG, "wb", buffering=0) as log_file:
        result = subprocess.run(
            ["uv", "run", "train.py"],
            stdout=log_file,
            stderr=subprocess.STDOUT,
            cwd=str(PROJECT_ROOT),
        )

    log_text = RUN_LOG.read_text(errors="replace")
    metrics = _parse_metrics(log_text)

    git_commit = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True, cwd=str(PROJECT_ROOT),
    ).stdout.strip()

    return {
        **metrics,
        "commit": git_commit,
        "description": description,
        "status": "keep" if result.returncode == 0 else "crash",
        "timestamp": datetime.now().isoformat(),
        "returncode": result.returncode,
    }


@workflow
def experiment(description: str = "") -> dict:
    """Single training experiment workflow."""
    return train(description=description)


if __name__ == "__main__":
    desc = " ".join(sys.argv[1:])
    result = experiment(description=desc)
    print(f"\nResult: {result}")
