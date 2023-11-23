print("importing module 1")
from test.test_nested_reimport.ImportedModule2 import SomeClass, SomeDynamicClasses

SomeClass.foo = lambda self: self
SomeDynamicClasses.foo = lambda self: self
