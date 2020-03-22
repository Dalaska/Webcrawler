import subprocess

subprocess.call(["git", "status"])
subprocess.call(["git","add","."])
subprocess.call(["git","commit","-m","'auto push'"])
subprocess.call(["git","push"])
pass