import sys
from pathlib import Path

from src.dynamic_executor.utils.DynamicModeExecutor import DynamicModeExecutor


def test_dynamic_class_import_from():
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleFaulty.py").read_text()
    )
    sys.path.append(str(parent))
    from .ImportedModule import SomeDynamicClass

    dynamic_instance = SomeDynamicClass()
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
    assert index != -1
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleFaulty.py").read_text()
    )
