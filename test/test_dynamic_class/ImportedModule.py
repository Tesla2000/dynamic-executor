from src.dython.classes.DynamicClassModule import DynamicClass


class SomeDynamicClass(DynamicClass):
    def foo(self):
        raise ValueError
