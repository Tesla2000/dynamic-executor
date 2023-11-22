print("importing module 1")
__all__ = [
    "SomeDynamicClasses",
    "SomeClass"
]

from test.test_nested_reimport.ImportedModule2 import SomeClass, SomeDynamicClasses
