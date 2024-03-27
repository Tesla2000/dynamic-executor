from .ImportedModule1 import SomeClass as SC, SomeDynamicClass as SDC
from src.dynamic_executor.utils import _get_modules
from src.dynamic_executor.utils._re_import import _re_import_modules


def test_nested_reimport_with_modification_class_reimport_as():
    modules = _get_modules()
    some_instance = SC()
    some_dynamic_instance = SDC()
    assert hasattr(some_instance, "foo")
    assert hasattr(some_dynamic_instance, "foo")
    _re_import_modules(modules, locals(), globals())
    assert not isinstance(some_instance, SC)
    assert isinstance(some_dynamic_instance, SDC)
    assert hasattr(some_instance, "foo")
    assert hasattr(some_dynamic_instance, "foo")
