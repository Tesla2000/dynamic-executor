import threading
from pathlib import Path
from time import sleep

import ImportedModule
from src.dynthon.exec_in_dynamic_mode import exec_in_dynamic_mode

if __name__ == '__main__':
    parent = Path(__file__).parent
    parent.joinpath('ImportedModule.py').write_text(parent.joinpath('ImportedModuleFaulty.py').read_text())
    dynamic_instance = ImportedModule.SomeDynamicClass()
    thread = threading.Thread(
        target=lambda: exec_in_dynamic_mode(
            locals(), globals(), parent.joinpath('test_executor.py')
        )
    )
    thread.start()
    sleep(1)
    assert thread.is_alive()
    parent.joinpath('ImportedModule.py').write_text(parent.joinpath('ImportedModuleValid.py').read_text())
    sleep(1)
    assert not thread.is_alive()  # test not working properly for some reason
