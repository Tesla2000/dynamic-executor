import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from src.dynamic_executor.utils import _get_modules
from src.dynamic_executor.utils._re_import import _re_import_modules


def test_dynamic_import_import():
    import ImportedModule
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleBackUpModified.py").read_text()
    )
    try:
        standard_instance = ImportedModule.StandardClass()
        dynamic_instance = ImportedModule.SomeDynamicClass()
        assert not hasattr(ImportedModule.StandardClass, "foo")
        assert isinstance(standard_instance, ImportedModule.StandardClass)
        assert not hasattr(ImportedModule.SomeDynamicClass, "foo")
        assert isinstance(dynamic_instance, ImportedModule.SomeDynamicClass)
        _re_import_modules(_get_modules(), locals(), globals())
        assert hasattr(ImportedModule.StandardClass, "foo")
        assert not isinstance(standard_instance, ImportedModule.StandardClass)
        assert hasattr(ImportedModule.SomeDynamicClass, "foo")
        assert isinstance(dynamic_instance, ImportedModule.SomeDynamicClass)
    finally:
        parent.joinpath("ImportedModule.py").write_text(
            parent.joinpath("ImportedModuleBackUp.py").read_text()
        )
