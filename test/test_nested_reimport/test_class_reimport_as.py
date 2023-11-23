from ImportedModule1 import SomeClass as SC
from src.dynthon.utils import get_modules
from src.dynthon.utils.re_import import re_import_modules

if __name__ == "__main__":
    some_instance = SC()
    modules = get_modules()
    re_import_modules(modules, locals(), globals())
    assert not isinstance(some_instance, SC)
