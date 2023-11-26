from pathlib import Path

import ImportedModule
from src.dynamic_executor.utils.DynamicModeExecutor import DynamicModeExecutor

if __name__ == "__main__":
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleFaulty.py").read_text()
    )
    some_dynamic_function = ImportedModule.some_dynamic_function
    index = -1
    for index, error in enumerate(
        DynamicModeExecutor(parent.joinpath("test_executor.py")).execute(
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
