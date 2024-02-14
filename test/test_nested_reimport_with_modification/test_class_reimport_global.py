from .ImportedModule1 import SomeClass, SomeDynamicClass
from src.dynamic_executor.utils import get_modules
from src.dynamic_executor.utils.re_import import re_import_modules


def test_nested_reimport_with_modification_class_reimport():
    modules = get_modules()
    some_instance = SomeClass()
    some_dynamic_instance = SomeDynamicClass()
    assert hasattr(some_instance, "foo")
    assert hasattr(some_dynamic_instance, "foo")
    re_import_modules(modules, locals(), globals())
    assert not isinstance(some_instance, SomeClass)
    assert isinstance(some_dynamic_instance, SomeDynamicClass)
    assert hasattr(some_instance, "foo")
    assert hasattr(some_dynamic_instance, "foo")
