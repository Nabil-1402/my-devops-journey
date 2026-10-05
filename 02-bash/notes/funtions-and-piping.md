# Notes

# Functions and Piping

## Key Concepts

- Functions blocks of code that can be repeatedly called upon
- Functions return a value and can take in parameters

## Commands

`function_name(){.....}` - Function syntax
`function_name p1 p2` - Call a function with parameters
`local varaiable_name=` - Create a local variable
`$#` - special variable that holds the count of arguments
`$0` - variable containing the name of the script
`read` - capture the users input and store it

## Examples

#!/bin/bash

hello_world(){

    echo "Hellow World"

}

#!/bin/bash

greet_user(){

    echo "What is your name?"

    read name

    echo "Hello, $name!"

}

#!/bin/bash

greet(){

    local name

    if [ $# -eq 0]; then

        echo "What is your name?"

        read name
    
    else

        name=$1

    fi

    echo "Hello name!"

}

#!/bin/bash

get_file_count(){

    local directory=$1
    
    local file_count

    file_count=$(ls "$directory" | wc -l)

    echo "Number of files in $director: $file_count

}

get_file_count "./"

## What I Learned

Functions are useful to organise and modularising your script. You can pass in parameters to your functions and even use user input as parameters. You should use conditional statements to filter out bad data that is entered and you can make scripts more powerful using piping.


## Your Notes

Functions allow us to modularise and organise our scripts. Functions can use local variables. You can call a variable by typing out its name along with any parameters. 

There are two types of parameters, positional and special parameters. Positional parameters allow us to pass in data to functions and allow us to access them using numbered variable such as $1 and $2. Special parameters provide additional information about the script such as the full name of the script and the number of arguments.

User inputs allow our scripts to interact with users and make the script dynamic and responsive. You use the read followed by a variable to store what the user types from the CLI.

Bad data refers to invalid or unexpected user inputs that may cause errors or undesired behaviour in our scripts. You can use conditional statements to validate user inputs. When an error condition is met type `return 1` to return a non zero exit code. Input sanitization can be used to clean input data.

Piping allows us to pass the output of one command as the input to another. 