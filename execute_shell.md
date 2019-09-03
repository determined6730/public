# execute shell 
```python 
import subprocess
import os

os.getcwd()
os.chdir()

def exec_command(str):
    result = subprocess.check_output(str,shell=True)
    print result
    return result
```
