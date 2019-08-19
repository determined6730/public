import subprocess
import os

print os.getcwd()

result = subprocess.check_output("git status",shell=True)
print result


if "nothing added to commit but untracked files present" in result:
    print subprocess.check_output("git add *",shell=True)
    print subprocess.check_output("git commit -m \"autocommit\"",shell=True)
    print subprocess.check_output("git push origin master",shell=True)
else:
    print "nothing"
