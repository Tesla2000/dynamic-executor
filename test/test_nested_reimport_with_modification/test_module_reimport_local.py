import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from src.dynamic_executor.utils import _get_modules
from src.dynamic_executor.utils._re_import import _re_import_modules


def test_nested_reimport_with_modification_module_reimport():
    import ImportedModule1

    modules = _get_modules()
    some_instance = ImportedModule1.SomeClass()
    some_dynamic_instance = ImportedModule1.SomeDynamicClass()
    assert hasattr(some_instance, "foo")
    assert hasattr(some_dynamic_instance, "foo")
    _re_import_modules(modules, locals(), globals())
    assert not isinstance(some_instance, ImportedModule1.SomeClass)
    assert isinstance(some_dynamic_instance, ImportedModule1.SomeDynamicClass)
    assert hasattr(some_instance, "foo")
    assert hasattr(some_dynamic_instance, "foo")
