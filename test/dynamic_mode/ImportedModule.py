from src.dynthon.classes.DynamicClassModule import DynamicClass


class SomeDynamicClass(DynamicClass):
    def foo(self):
        raise ValueError
