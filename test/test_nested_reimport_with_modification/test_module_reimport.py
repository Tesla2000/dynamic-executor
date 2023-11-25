import ImportedModule1
from src.dython.utils import get_modules
from src.dython.utils.re_import import re_import_modules

if __name__ == "__main__":
    modules = get_modules()
    some_instance = ImportedModule1.SomeClass()
    some_dynamic_instance = ImportedModule1.SomeDynamicClass()
    assert hasattr(some_instance, 'foo')
    assert hasattr(some_dynamic_instance, 'foo')
    re_import_modules(modules, locals(), globals())
    assert not isinstance(some_instance, ImportedModule1.SomeClass)
    assert isinstance(some_dynamic_instance, ImportedModule1.SomeDynamicClass)
    assert hasattr(some_instance, 'foo')
    assert hasattr(some_dynamic_instance, 'foo')
