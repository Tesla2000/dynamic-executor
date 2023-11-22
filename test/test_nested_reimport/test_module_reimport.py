import ImportedModule1
from src.dynthon.utils import get_modules
from src.dynthon.utils.re_import import re_import_modules

if __name__ == "__main__":
    some_instance = ImportedModule1.SomeClass()
    modules = get_modules()
    re_import_modules(modules, locals(), globals())
    assert not isinstance(some_instance, ImportedModule1.SomeClass)
