# Notes

# Error Handling and Exit Codes

## Key Concepts

- Error handling is useful in preventing errors crashing a script or resulting in unexpected errors
- You should use `set` commands to help with error handling and debugging

## Commands

`exit 0` - Exit code with success

`exit 1` - Exit code with error

`echo $?` - Print out the exit code of the last command ran

`command` - checks if a command exists in a system

`set -e` - Stop the script when any command returns a non zero exit code

`set -u` - Stop the script when you come across any uninitialised variable

`set -x` - Print all the executed commands to the terminal before it is actually executed (useful for debugging)

`set +x` - To not print out anything after a certain point for debugging

`set -o nounset` - equivalent to set -u, helps you catch uninitialised variables 

`set -o errexit` - Works the same was as set -e, causes shell to exit if any invoked command fails

`set -o pipefail` - Useful setting that causes the pipline to return the exit status of the last command in the pipeline that exited with a non zero status

## Examples

#!/bin/bash

num1=10

num2=0

if [$num2 -eq 0]; then

    echo "Error: Division by zero is not allowed"

    exit 1

fi

result=$(($num1 / num2))

echo "The result is: $result"


#!/bin/bash

set -eux

echo "This is a test."

x=10

echo "This value of x is: $x"

nonexistentcommand

## What I Learned

I learned that error handling is very useful tool to use when writing your scripts. This is done with if statements to catch the errors. Also I learned how to make scripts more robust and helpful with debugging by learning about `set` commands.


## Your Notes

Error handling is about foreseeing where things can go wrong and dealing with these issues. This can make scripts more reliable and trustworthy. An error causes a script to just stop and this can be a problem when the script is large. For error handling you use if statements and an exit code of 1. This can give the user helpful error messages.

Whenever a command or script ends it returns an exit code to the system. This is a numerical value which represents whether a command or script ended successfully or not. `0` represents success and non zero represents there was an error. 

When we include `set -e` the script will stop executing when any command returns a non zero exit code. This command can help us spot errors as soon as they come and avoid unexpected behaviour. However not all non zero exit codes are indicative of errors that should stop your script.

When we include the `set -u` we force the bash script to stop executing when we come across a non initialised variables. This is helps you prevent scenarios where missing data could lead incorrect results or unexpected behavior. 

When a script is not behaving as expected, debugging comes in handy. One powerful tool for this is the `set -x` command. This prints each command that will be executed to the terminal before it is executed. You can treat this with `set +x` as breakpoints in your script for debugging. 

You can combine all of them with the command `set -eux`. 