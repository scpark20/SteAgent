"""Run the final course implementation from Chapter 08."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).parent / "code/chapter-08/agent.py"), run_name="__main__")
