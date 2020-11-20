import shlex
import subprocess

full_command = r'cmd /c dir c:\\class'
command_list = shlex.split(full_command)
print(command_list)
p1 = subprocess.run(command_list, stdout=subprocess.PIPE,
                    universal_newlines=False)

print(p1)
