from pathlib import Path
from ImportedModule1 import SomeClass as SC
from src.dynthon.utils import get_modules
from src.dynthon.utils.re_import import re_import_modules

if __name__ == "__main__":
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule2.py").write_text(
        parent.joinpath("ImportedModuleBackUpModified.py").read_text()
    )
    try:
        some_instance = SC()
        modules = get_modules()
        re_import_modules(modules, locals(), globals())
        assert not isinstance(some_instance, SC)
        assert hasattr(some_instance, 'foo')
    finally:
        parent.joinpath("ImportedModule2.py").write_text(
            parent.joinpath("ImportedModuleBackUp.py").read_text()
        )
