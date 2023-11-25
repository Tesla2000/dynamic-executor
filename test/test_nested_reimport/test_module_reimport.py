from pathlib import Path

import ImportedModule1
from src.dynthon.utils import get_modules
from src.dynthon.utils.re_import import re_import_modules

if __name__ == "__main__":
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule2.py").write_text(
        parent.joinpath("ImportedModuleBackUpModified.py").read_text()
    )
    try:
        some_instance = ImportedModule1.SomeClass()
        modules = get_modules()
        re_import_modules(modules, locals(), globals())
        assert not isinstance(some_instance, ImportedModule1.SomeClass)
        assert hasattr(some_instance, 'foo')
    finally:
        parent.joinpath("ImportedModule2.py").write_text(
            parent.joinpath("ImportedModuleBackUp.py").read_text()
        )
