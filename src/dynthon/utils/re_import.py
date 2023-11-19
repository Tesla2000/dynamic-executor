import importlib
import sys

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
