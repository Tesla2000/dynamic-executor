from pathlib import Path

from .ImportedModule1 import SomeClass, SomeDynamicClass
from src.dynamic_executor.utils import _get_modules
from src.dynamic_executor.utils._re_import import _re_import_modules


def test_class_nested_reimport_from():
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule2.py").write_text(
        parent.joinpath("ImportedModuleBackUpModified.py").read_text()
    )
    try:
        some_instance = SomeClass()
        some_dynami_instance = SomeDynamicClass()
        modules = _get_modules()
        _re_import_modules(modules, locals(), globals())
        assert not isinstance(some_instance, SomeClass)
        assert isinstance(some_dynami_instance, SomeDynamicClass)
        assert not hasattr(some_instance, "foo")
        assert hasattr(some_dynami_instance, "foo")
    finally:
        parent.joinpath("ImportedModule2.py").write_text(
            parent.joinpath("ImportedModuleBackUp.py").read_text()
        )
