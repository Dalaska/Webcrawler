import subprocess

#https://zhuanlan.zhihu.com/p/33093791
#https://zhuanlan.zhihu.com/p/26767243

def run_cmd(cmd):
    return subprocess.Popen(cmd,
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)


p = run_cmd(['ping', 'zhihu.com'])
for i in iter(p.stdout.readline, ''):
    print(i.strip())

pass