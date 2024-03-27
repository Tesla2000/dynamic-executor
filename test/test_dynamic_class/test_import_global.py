import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
import ImportedModule
from src.dynamic_executor.utils.DynamicModeExecutor import DynamicModeExecutor


def test_dynamic_class_import():
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleFaulty.py").read_text()
    )
    dynamic_instance = ImportedModule.SomeDynamicClass()
    index = -1
    for index, error in enumerate(
        DynamicModeExecutor(parent.joinpath("_test_executor.py")).execute(
            locals(), globals()
        )
    ):
        if index:
            assert False
        parent.joinpath("ImportedModule.py").write_text(
            parent.joinpath("ImportedModuleValid.py").read_text()
        )
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleFaulty.py").read_text()
    )
    assert index != -1
