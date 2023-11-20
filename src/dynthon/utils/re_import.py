import importlib
import sys
from collections import ChainMap
from inspect import getmodule
from types import ModuleType
from typing import Callable

from .get_defined_in_module import get_defined_in_module
from .get_dynamic_classes import get_dynamic_classes


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
    locals_from_modules = dict((key, module) for key, value in __locals.items() if isinstance(value, Callable) and (module := getmodule(value)) and module in modules.values())
    globals_from_modules = dict((key, module) for key, value in __globals.items() if isinstance(value, Callable) and (module := getmodule(value)) and module in modules.values())
    local_modules = dict((key, value) for key, value in __locals.items() if isinstance(value, ModuleType) and key != '__builtins__')
    global_modules = dict((key, value) for key, value in __globals.items() if isinstance(value, ModuleType) and key != '__builtins__')
    all_modules = ChainMap(local_modules, global_modules)
    for variable, module in locals_from_modules.items():
        all_modules[module.__name__] = module
    for variable, module in globals_from_modules.items():
        all_modules[module.__name__] = module
    for module_name, module in modules.items():
        del sys.modules[module_name]
    tuple(map(importlib.import_module, all_modules.keys()))
    local_modules = dict((variable, importlib.import_module(module.__name__)) for variable, module in local_modules.items())
    global_modules = dict((variable, importlib.import_module(module.__name__)) for variable, module in global_modules.items())
    locals_from_modules = dict((variable, importlib.import_module(module.__name__)) for variable, module in locals_from_modules.items())
    globals_from_modules = dict((variable, importlib.import_module(module.__name__)) for variable, module in globals_from_modules.items())
    for variable, module in locals_from_modules.items():
        __locals[variable] = getattr(module, variable)
    for variable, module in globals_from_modules.items():
        __globals[variable] = getattr(module, variable)
    for variable, module in local_modules.items():
        __locals[variable] = module
    for variable, module in global_modules.items():
        __globals[variable] = module
