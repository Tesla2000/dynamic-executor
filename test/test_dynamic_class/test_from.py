from pathlib import Path

from ImportedModule import SomeDynamicClass
from src.dynamic_executor.utils.exec_in_dynamic_mode import exec_in_dynamic_mode

if __name__ == "__main__":
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleFaulty.py").read_text()
    )
    dynamic_instance = SomeDynamicClass()
    index = -1
    for index, error in enumerate(exec_in_dynamic_mode(locals(), globals(), parent.joinpath("test_executor.py"))):
        if index:
            assert False
        parent.joinpath("ImportedModule.py").write_text(
            parent.joinpath("ImportedModuleValid.py").read_text()
        )
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleFaulty.py").read_text()
    )
    assert index != -1
