import re
import sys


def get_modules():
    return dict(
        (variable, value)
        for variable, value in sys.modules.items()
        if not re.findall(r"module \'[^\']+\' \((?:built-in|frozen)\)", str(value))
        and 'python3.12' not in str(value)
        and not variable.startswith('_')
        and not any(map(variable.__contains__, ('dynthon', 'pyexpat', 'pydev', 'xml.parsers.expat.', 'typing.')))
    )
