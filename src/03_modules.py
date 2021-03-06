"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
#import fileinput
# for line in fileinput.input():
#   if str(line) == "exit":
#       break
#   else:
#       print(line)

## First run this on terminal `python3 03_modules.py arg1 arg2 arg3`
for arg in sys.argv:
    print(arg)

# Print out the OS platform you're using:
print(sys.platform)

# Print out the version of Python you're using:
print(sys.version_info)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getpgid(0))

# Print the current working directory (cwd):
print(os.getcwd())

# Print out your machine's login name
print(os.getlogin()) # this is availabel on Linux and Windows
