import os
cmd = "/cygdrive/c/Program\ Files/PuTTY/putty.exe -ssh 192.168.155.3 22"

print('Opening SSH connection with putty...')
os.system(cmd)
