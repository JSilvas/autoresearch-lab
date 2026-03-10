"""
Flyte 2 workflow for autoresearch experiment observability.

Usage:
    flyte run --local --tui workflow.py run_training
    flyte start tui   (to browse past runs)
"""

import re
import subprocess

import flyte

env = flyte.TaskEnvironment(name="autoresearch")


@env.task
def run_training() -> str:
    """Run uv run train.py and return the summary block."""
    result = subprocess.run(
        ["uv", "run", "train.py"],
        capture_output=True,
        text=True,
        cwd="/Users/jay/dev/autoresearch-macos",
    )

    output = result.stdout + result.stderr

    # Extract summary block (everything after "---")
    sep = output.rfind("\n---\n")
    summary = output[sep:].strip() if sep >= 0 else ""

    if not re.search(r"^val_bpb:", summary, re.MULTILINE):
        tail = output[-4000:] if len(output) > 4000 else output
        raise RuntimeError(f"Training did not produce val_bpb.\n\n{tail}")

    print(summary)
    return summary
