#!/usr/bin/env python3
# Author: Ajay Saini
# Author ID: asaini85 (152730222)
# Date Created: 2025/02/02

import sys

# Check if there is a command-line argument, if not, set timer to 3
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Convert the argument to an integer
else:
    timer = 3  # Default value if no argument is provided

# While loop to count down
while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')
