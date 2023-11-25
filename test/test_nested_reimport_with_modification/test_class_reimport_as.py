from ImportedModule1 import SomeClass as SC, SomeDynamicClass as SDC
from src.dynamic_executor.utils import get_modules
from src.dynamic_executor.utils.re_import import re_import_modules

if __name__ == "__main__":
    modules = get_modules()
    some_instance = SC()
    some_dynamic_instance = SDC()
    assert hasattr(some_instance, 'foo')
    assert hasattr(some_dynamic_instance, 'foo')
    re_import_modules(modules, locals(), globals())
    assert not isinstance(some_instance, SC)
    assert isinstance(some_dynamic_instance, SDC)
    assert hasattr(some_instance, 'foo')
    assert hasattr(some_dynamic_instance, 'foo')
