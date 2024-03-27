import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from src.dynamic_executor.utils import _get_modules
from src.dynamic_executor.utils._re_import import _re_import_modules


def test_module_reimport():
    import ImportedModule1

    parent = Path(__file__).parent
    parent.joinpath("ImportedModule2.py").write_text(
        parent.joinpath("ImportedModuleBackUpModified.py").read_text()
    )
    try:
        some_instance = ImportedModule1.SomeClass()
        some_dynami_instance = ImportedModule1.SomeDynamicClass()
        modules = _get_modules()
        _re_import_modules(modules, locals(), globals())
        assert not isinstance(some_instance, ImportedModule1.SomeClass)
        assert isinstance(some_dynami_instance, ImportedModule1.SomeDynamicClass)
        assert not hasattr(some_instance, "foo")
        assert hasattr(some_dynami_instance, "foo")
    finally:
        parent.joinpath("ImportedModule2.py").write_text(
            parent.joinpath("ImportedModuleBackUp.py").read_text()
        )
