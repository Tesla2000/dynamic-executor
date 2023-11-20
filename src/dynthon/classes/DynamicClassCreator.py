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

    def __new__(cls, name, bases, namespace):
        new_class = super().__new__(cls, name, bases, namespace)
        cls.created_classes.append(new_class)
        new_class._instances = []
        new_class.__new__ = new_wrapper(new_class.__new__)
        return new_class
