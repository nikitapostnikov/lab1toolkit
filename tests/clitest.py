from pathlib import Path
import pytest
from toolkit.kernel import converTORR
SRC = Path(__file__).resolve().parents[1] / "src" / "toolkit"

def test_test0():
    command="--help"
    