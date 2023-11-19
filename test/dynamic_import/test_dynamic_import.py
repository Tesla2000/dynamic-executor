from pathlib import Path

import ImportedModule
from src.dynthon.utils.re_import import re_import

if __name__ == '__main__':
    parent = Path(__file__).parent
    parent.joinpath('ImportedModule.py').write_text(parent.joinpath('ImportedModuleValid.py').read_text())
    try:
        standard_instance = ImportedModule.StandardClass()
        dynamic_instance = ImportedModule.SomeDynamicClass()
        assert not hasattr(ImportedModule.StandardClass, 'foo')
        assert isinstance(standard_instance, ImportedModule.StandardClass)
        assert not hasattr(ImportedModule.SomeDynamicClass, 'foo')
        assert isinstance(dynamic_instance, ImportedModule.SomeDynamicClass)
        ImportedModule = re_import('ImportedModule')
        assert not hasattr(ImportedModule.StandardClass, 'foo')
        assert isinstance(standard_instance, ImportedModule.StandardClass)
        assert hasattr(ImportedModule.SomeDynamicClass, 'foo')
        assert isinstance(dynamic_instance, ImportedModule.SomeDynamicClass)
    except Exception as e:
        raise e
    finally:
        parent.joinpath('ImportedModule.py').write_text(parent.joinpath('ImportedModuleFaulty.py').read_text())
