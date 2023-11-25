from pathlib import Path
from ImportedModule1 import SomeClass as SC, SomeDynamicClass as SDC
from src.dynamic_executor.utils import get_modules
from src.dynamic_executor.utils.re_import import re_import_modules

if __name__ == "__main__":
    parent = Path(__file__).parent
    parent.joinpath("ImportedModule2.py").write_text(
        parent.joinpath("ImportedModuleBackUpModified.py").read_text()
    )
    try:
        some_instance = SC()
        some_dynami_instance = SDC()
        modules = get_modules()
        re_import_modules(modules, locals(), globals())
        assert not isinstance(some_instance, SC)
        assert isinstance(some_dynami_instance, SDC)
        assert not hasattr(some_instance, 'foo')
        assert hasattr(some_dynami_instance, 'foo')
    finally:
        parent.joinpath("ImportedModule2.py").write_text(
            parent.joinpath("ImportedModuleBackUp.py").read_text()
        )
