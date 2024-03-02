from pathlib import Path

from src.dynamic_executor import DynamicModeExecutor
from .SomeDynamicClass import SomeDynamicClass


def test_instance_creation():
    _ = SomeDynamicClass
    parent = Path(__file__).parent
    for error in DynamicModeExecutor(parent.joinpath("_test_executor.py")).execute(
        locals(), globals()
    ):
        pass
