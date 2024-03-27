from pathlib import Path

from src.dynamic_executor.utils.DynamicModeExecutor import DynamicModeExecutor


def test_dynamic_function_import_from():
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleFaulty.py").read_text()
    )
    from .ImportedModule import some_dynamic_function

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
