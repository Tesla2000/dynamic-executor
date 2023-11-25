from ImportedModule1 import SomeClass, SomeDynamicClass
from src.dython.utils import get_modules
from src.dython.utils.re_import import re_import_modules

if __name__ == "__main__":
    modules = get_modules()
    some_instance = SomeClass()
    some_dynamic_instance = SomeDynamicClass()
    assert hasattr(some_instance, 'foo')
    assert hasattr(some_dynamic_instance, 'foo')
    re_import_modules(modules, locals(), globals())
    assert not isinstance(some_instance, SomeClass)
    assert isinstance(some_dynamic_instance, SomeDynamicClass)
    assert hasattr(some_instance, 'foo')
    assert hasattr(some_dynamic_instance, 'foo')

