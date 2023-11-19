from src.dynthon.utils.module_type import module_type


def get_modules(local_vars: dict, global_vars: dict):
    all_vars = dict(**global_vars)
    for variable, value in local_vars.items():
        all_vars[variable] = all_vars.get(variable, value)
    return dict((variable, value) for variable, value in all_vars.items() if isinstance(value, module_type) and variable != '__builtins__')
