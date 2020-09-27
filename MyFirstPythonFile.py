import platform
import sys

print('Hello world !')

info = 'OS info: \n{} \n\nPython version is: {} and {}'.format(platform.uname(), sys.version, platform.architecture())
print(info)

with open('OS_info.txt', 'w') as file:
    file.write(info)
