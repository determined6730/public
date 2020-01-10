import subprocess
import os

def exec_command(str):
    result = subprocess.check_output(str,shell=True)
    print result
    return result


exec_command("git pull")

re = exec_command("git status")

if "nothing to commit, working tree clean" in re:
    print "nothing"
else:
    print exec_command("git add *")
    print exec_command("git add -u :/")
    print exec_command("git commit -m \"autocommit\"")
    print exec_command("git push origin master")
    print exec_command("git push code master")

