import subprocess
import os

def exec_command(str):
    result = subprocess.check_output(str,shell=True)
    print result



re = exec_command("git status")

if "nothing added to commit but untracked files present" in re:
    print exec_command("git add *")
    print exec_command("git commit -m \"autocommit\"")
    print exec_command("git push origin master")
else:
    print "nothing"

