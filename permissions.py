import os
import stat
#stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO same as 0o777
def change_permission(file):
    os.chmod(file , 0o777)
def hello():
    print("hello")