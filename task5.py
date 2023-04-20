import argparse
import os.path
import stat
import permissions
parser = argparse.ArgumentParser(description="executing linux command")
parser.add_argument("file_name", type=str ,help="file path")
arg=parser.parse_args()
if os.path.isfile(arg.file_name) is not True:
        with open(arg.file_name, 'w') as f:
            f.write('Create a new text file!')
            f.close()
current_permissions = os.stat(arg.file_name).st_mode

# Remove all permissions from all users
new_permissions = ~(stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

        
os.chmod(arg.file_name,  0o000)
try:
    file1 = open(arg.file_name,"r+")
except (PermissionError) as e:
     print("read write permsion denied")


     
permissions.change_permission(arg.file_name)
print("permissions reset")
