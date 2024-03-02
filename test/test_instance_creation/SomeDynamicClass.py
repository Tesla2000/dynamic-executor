from src.dynamic_executor.classes.DynamicClassModule import DynamicClass


class SomeDynamicClass(DynamicClass):
    def __init__(self, foo):
        self.foo = foo
