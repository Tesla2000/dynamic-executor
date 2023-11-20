from typing import Any

from .module_type import module_type
from src.dynthon.classes.DynamicClassCreator import DynamicClassCreator


def get_defined_in_module(module: module_type) -> dict[str, Any]:
    return dict(
        (variable, value)
        for variable in dir(module)
        if not isinstance(value := getattr(module, variable), module_type)
        and not variable.startswith("__")
        and value not in DynamicClassCreator.created_classes
        and value != DynamicClassCreator
    )
