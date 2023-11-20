import importlib
import sys

from .get_defined_in_module import get_defined_in_module
from .get_dynamic_classes import get_dynamic_classes
from .module_type import module_type


def re_import(module_name: str):
    module = sys.modules[module_name]
    dynamic_classes = get_dynamic_classes(module)
    defined_in_module = get_defined_in_module(module)
    module = importlib.reload(module)
    for variable, value in defined_in_module.items():
        setattr(module, variable, value)
    for variable, dynamic_class in dynamic_classes.items():
        new_class = getattr(module, variable)
        for instance in dynamic_class._instances:
            instance.__class__ = new_class
        new_class._instances = dynamic_class._instances
    sys.modules[module_name] = module
    return module


def re_import_modules(modules: dict, __locals: dict, __globals: dict):
    local_modules = dict(**__locals)
    for key, var in __globals.items():
        if key in local_modules:
            continue
        local_modules[key] = var
    local_modules = dict((key, value) for key, value in local_modules.items() if isinstance(value, module_type) and key != '__builtins__')
    for module_name, module in modules.items():
        if module_name in local_modules:
            continue
        del sys.modules[module_name]
    tuple(map(importlib.reload, local_modules.values()))

