# Labs

# Lab: [Challenge 1: Basic Arithmetic Calculator]

## Objective

Create a script that takes two numbers as input and performs basic arithmetic operations (addition, subtraction, multiplication, division).

Requirements:
- Prompt user for two numbers
- Perform all four operations
- Display the results
- Handle division by zero

## Commands Used

#!/bin/bash

echo "Enter your first number: "

read num1

echo "Enter your second number: "

read num2

echo "$num1 + $num2 = $(($num1 + $num2))"

echo "$num1 - $num2 = $(($num1 - $num2))"

echo "$num1 * $num2 = $(($num1 * $num2))"

if [ "$num2" -eq 0 ]

then
        echo "Cant perform division as second number is 0"

else
        echo "$num1 / $num2 = $(($num1 / $num2))"

fi


## Output

I ran the script twice one with the second one as non 0 and one with the second number as zero.

First time I ran it with 10 and 2 and it followed:

Enter your first number: 

10

Enter your second number: 

2


10 + 2 = 12

10 - 2 = 8

10 * 2 = 20

10 / 2 = 5

Second time I ran it with 10 and 0 and it followed:

Enter your first number: 

10

Enter your second number: 

0


10 + 0 = 10

10 - 0 = 10

10 * 0 = 0

Cant perform division as second number is 0


## Challenges

The main issue I ran into was my if statement not running. I first found out that I didn't use `""` when calling the variable but then it still was not working. I then realised that I needed the spaces inside the square brackets so that the syntax of the if statement was correct.

## What I Learned

In this lab I learned how to take in user inputs and combine that with error handling using an if statement to provide useful output to the user.

