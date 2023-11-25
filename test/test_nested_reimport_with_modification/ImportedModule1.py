print("importing module 1")
from test.test_nested_reimport.ImportedModule2 import SomeClass, SomeDynamicClass

SomeClass.foo = lambda self: self
SomeDynamicClass.foo = lambda self: self
