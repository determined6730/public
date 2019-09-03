# execute shell 
```python 
import subprocess
import os

work_dir = "..."

print os.getcwd()
os.chdir(work_dir)

def exec_command(str):
    result = subprocess.check_output(str,shell=True)
    print result
    return result

```
