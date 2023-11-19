from .module_type import module_type
from ..DynamicClassCreator import DynamicClassCreator


def get_dynamic_classes(module: module_type) -> dict[str, DynamicClassCreator]:
    return dict((variable, value) for variable in dir(module) if (value := getattr(module, variable)) in DynamicClassCreator.created_classes)
