# salt is random data fed as additional
# input to a one-way function

#Remotely connect to machine and execute
# commands from there

# command scp to copy files to remote machines

# scp my-notes.txt login.ccs.neu.edu:/home/hawang

# chmod ls -l

# advanced scripting:
# - 

# pwd will print out my current directory
# command ls shows all things in current directory

# change directory to the root, which is /
# mkdir makes a folder
# cp is the syntax 

# cp -r changes behavior of copy command to copy
# recursively

# read, write, execution metadata

# file perm changes

# echo "Arg $i is $arg" prints out the argument/value of argument
# 

# scripting. 

import sys

print(f'Received {len(sys.argv)} arguments')

for i, arg in enumerate(sys.argv):
    print(f'Arg {i} is {arg}')

# sys.argv is a list of arguments passed to the script
# sys.argv[0] is the name of the script
# sys.argv[1:] are the arguments passed to the script


# you can change input/output of a command into a file
# using ">", redirect messages sent to STDOUT
# ./stdio-demo Hello World 2> log.txt

# ./stdio-demo Hello World &> log.txt

# interested in a specific entry, we can use grep
# to search for it: Ps -aux | grep bash
# Demonstration of Input/Output redirection in Python







# Example 1: Writing to a file (STDOUT redirection)
with open('output.txt', 'w') as f:
    # This is equivalent to command: echo "Hello World" > output.txt
    print("Hello World", file=f)

# Example 2: Writing errors to a file (STDERR redirection)
import sys
try:
    # This will generate an error and write it to error_log.txt
    # Equivalent to: python script.py 2> error_log.txt
    x = 1/0
except Exception as e:
    with open('error_log.txt', 'w') as f:
        print(f"Error occurred: {str(e)}", file=f)

# Example 3: Appending to a file
with open('append.txt', 'a') as f:
    # This is equivalent to: echo "Appending this line" >> append.txt
    print("Appending this line", file=f)

# Example 4: Reading input from a file
try:
    # This is equivalent to: cat < input.txt
    with open('input.txt', 'r') as f:
        content = f.read()
        print(f"Content read from file: {content}")
except FileNotFoundError:
    print("input.txt file not found")

# Note: The above examples demonstrate the Python equivalent of shell I/O redirection
# Shell commands would use > for output, 2> for error output, >> for append
# and < for input redirection

