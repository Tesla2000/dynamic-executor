from src.dynthon.DynamicClass import DynamicClass


class SomeDynamicClass(DynamicClass):
    def foo(self):
        raise ValueError
