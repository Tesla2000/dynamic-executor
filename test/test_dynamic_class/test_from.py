from pathlib import Path

from ImportedModule import SomeDynamicClass
from src.dynthon.utils.exec_in_dynamic_mode import exec_in_dynamic_mode

if __name__ == "__main__":
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleFaulty.py").read_text()
    )
    dynamic_instance = SomeDynamicClass()
    exec_in_dynamic_mode(
        locals(), globals(), parent.joinpath("test_executor.py")
    )
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleFaulty.py").read_text()
    )
