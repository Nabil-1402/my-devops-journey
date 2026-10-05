# Notes

# Scripting Basics

## Key Concepts

- Help automate tasks
- Help with large repetitive tasks
- They need to state the interpreter stated at the first line
- Scripts are executable files

## Commands

`#!` - This is the shebang and is the first line in any bash script and says to the system how to interpret the script

`#` - Used for adding single line comments in your script

` :' '` - Used for adding multiline comments

`chmod +x (name)` - Used to make the script executable

`./name.sh` - Used to run the script

`variable_name=` - Used to create a variable

`$@` - Usings all parameters in the same line

`(())` - Used to perform arithmetic expanision


## Examples

#!/bin/bash

length="$1"

width="$2"

area=$((lentgh * width))

perimeter=$((2 * (length + width)))

echo "parameters used: $@"

echo "area: $area"
echo "perimeter: $perimeter"

:'

This script calculates the area and perimtier given the parameters passed in the CLI and prints out all the parameters used as well as the area and perimeter.

'

## What I Learned

I learned the basics of bash scripting including: the shebang, how to comment, variables, parameters and also arithmetic expansion.

## Your Notes

You can run a script from anywhere by placing it inside of PATH. A commone place to put it is inside the /usr/local/bin path. To do this run `sudo mv name.sh /usr/loacal/bin/name`. The you can use whatever you called the file in the path to run it instead of using `./` notation.

You can have variables which are places to store and manipulate data. To call on a variable place `$` infront of the variable name. Variables are not constrained to a single data type. They can be strings, intergers, floats and arrays. Arrays are created with brackets e.g. `fruits=("apple" "banana" "orange")`. Variable interpolation is using variables within a string e.g. `echo "Hello, $name"`.

Bash scripts can recieve arguments from the command line and these are known as parameters. Parameters are passed in after the script name e.g. `./script.sh parameter1 parameter2`. You can access parameters inside the script by using `$` followed by the number of the parameter. `$@` can be used to access all paramters passed into your script.

To perform arithmetic expansion in bash use `$(())`. This allows us to perform calculations using variables and parameters which provides us with a way of incorporating calculations into our scripts. These make scripts more dynamic and flexible.