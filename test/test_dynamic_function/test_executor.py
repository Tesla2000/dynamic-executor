try:
    some_dynamic_function()
except ValueError:
    parent.joinpath("ImportedModule.py").write_text(
        parent.joinpath("ImportedModuleValid.py").read_text()
    )
    raise ValueError