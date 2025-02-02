#!/usr/bin/env python3
# Author: Ajay Saini
# Author ID: 152730222
# Date Created: 2025/02/02

import sys

# Assign the first command-line argument to the timer
timer = int(sys.argv[1])  # Convert the argument to an integer

# While loop to count down
while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')
