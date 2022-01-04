

import subprocess
import sys
import redis
#import paramiko


host = '172.16.1.87'
port = 6379


r  = redis.Redis(host = host, port=port,decode_responses=True)

print(r.keys())
cmd = 'vagrant ssh-config'
status, output= subprocess.getstatusoutput(cmd)




print(output)
print(type(output))

r.set("vagrant.ssh_config",output)


