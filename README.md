# Dynamic-python library for changing python code during runtime

Dynamic python is ment to be used in test development for creating and updating tests or wherever the need arises to change the code during runtime and have results visible instantaneously without restarting. The main functionality is provided by `exec_in_dynamic_mode` generator that reloads all project-root modules (neither builtin not venv modules are reloaded)

## Installation

You can install the `dynamic-python` package using pip:

```bash
pip install dynamic-python
```

### Example

Here's an example of how to use the `exec_in_dynamic_mode` function:

```python
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from src import DbClass
from src import DbClassLiteral


def test_serialize_literal():
    @dataclass
    class Bar(DbClassLiteral):
        dictionary: dict
        date: datetime
        decimal: Decimal

    @dataclass
    class Foo(DbClass):
        dictionary: dict
        date: datetime
        decimal: Decimal
        bar: Bar

    foo = Foo({}, datetime.now(), Decimal(1), Bar({}, datetime.now(), Decimal(1)))
    serialized = foo.get_db_representation()
    try:
        json.dump(serialized, sys.stdout)
    except:
        assert False
    deserialized = Foo.from_dict(serialized)
    assert deserialized == foo


def test_serialize():
    @dataclass
    class Bar(DbClass):
        dictionary: dict
        date: datetime
        decimal: Decimal

    @dataclass
    class Foo(DbClass):
        dictionary: dict
        date: datetime
        decimal: Decimal
        bar: Bar

    foo = Foo({}, datetime.now(), Decimal(1), Bar({}, datetime.now(), Decimal(1)))
    serialized = foo.get_db_representation()
    foo.bar = foo.bar._id
    try:
        json.dump(serialized, sys.stdout)
    except:
        assert False
    deserialized = Foo.from_dict(serialized)
    assert deserialized == foo
```
