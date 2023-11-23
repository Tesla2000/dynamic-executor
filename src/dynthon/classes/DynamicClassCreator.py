from inspect import stack, getmodulename
from typing import Self


def new_wrapper(new):
    def wrapper(cls, *args, **kwargs):
        new_instance = new(cls, *args, **kwargs)
        if new_instance not in cls._instances:
            cls._instances.append(new_instance)
        return new_instance

    return wrapper


class DynamicClassCreator(type):
    created_classes: list[Self] = []

    def __new__(metacls, name, bases, namespace):
        new_class = super().__new__(metacls, name, bases, namespace)
        metacls.created_classes.append(new_class)
        type.__setattr__(new_class, "_instances", [])
        type.__setattr__(new_class, "__new__", new_wrapper(new_class.__new__))
        return new_class

    def __setattr__(self, key, value):
        super().__getattribute__('trace')()
        return super().__setattr__(key, value)

    def __getattribute__(self, item):
        super().__getattribute__('trace')()
        return super().__getattribute__(item)

    def trace(self):
        s = stack()
        module_path = s[2].filename
        module_name = getmodulename(module_path)
        try:
            if module_name not in super().__getattribute__('_modifications'):
                super().__getattribute__('_modifications').append(module_name)
        except AttributeError:
            super().__setattr__('_modifications', [module_name])
