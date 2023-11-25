from src.dynamic_executor.classes.DynamicClassModule import DynamicClass

print("importing module 2")
foo = "foo"


def function():
    pass


class SomeClass:
    def foo(self):
        pass


class SomeDynamicClass(DynamicClass):
    def foo(self):
        pass
