import traceback
from pathlib import Path

from .utils import get_modules, re_import


def exec_in_dynamic_mode(
    local_vars: dict,
    global_vars: dict,
    executor_path: Path = None,
    finnish_upon_success: bool = True,
):
    if executor_path is None:
        executor_path = Path("executor.py")
    if not executor_path.exists():
        executor_path.write_text("# Save mode executor")
    done = False
    while True:
        try:
            compiled = compile(executor_path.read_text(), executor_path.name, "exec")
            exec(compiled, global_vars, local_vars)
            done = True
        except:
            traceback.print_exc()
        if not finnish_upon_success or not done:
            modules = get_modules(local_vars, global_vars)
            for module_name in modules:
                re_import(module_name)
            continue
        return
