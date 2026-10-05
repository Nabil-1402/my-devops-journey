# Notes

# Conditionals and Loops

## Key Concepts

- Conditionals are used to help with branching in a script
- Loops are used to repeat a certain action multiple times

## Commands

`if [condition] then ... fi` - Create a if statement

`eq` - equals

`ne` - not equals

`lt` - less than

`gt` - greater than

`le` - less than or equal to

`ge` - greater than or equal to

`&&` - logic AND

`||` - logic OR

`==` - check strings are equal to each other

`!=` - check strings are not equal to each other

`else` - alternative code block when if condition is flase

`elif` - add another condition if the first condition is false

`while [condition] do ... done` - While loop syntax

`${#arrayName[@]}` - get the length of an array

`for variable in sequence do ... done` - For loop syntax

`$(seq 1 5)` - Generate numbers 1 to 5

`break` - Interrupt a loop, use to exit prematurely

`continue` - skip an iteration of the loop

## Examples

#!/bin/bash

age=25

if [ $age -gt 18 ]

then

    echo "You are an adult"

else

    echo "Your are not an adult"

fi


#!bin/bash

fruits=("apple" "banana" "orange")
index=0

while [ $index -lt ${#fruits[@]}]

do
    echo "Fruit: ${fruits[$index]}"

    ((index++))

done 


## What I Learned

I learned how to create if statements, for loops and while loops. I also leanred how to iterate over data structures such as arrays and also how to prematurely stop a loop and also how to skip an iteration of a loop.

## Your Notes

If statements are used to help with branching in code. It used a conditional statement and if that condition is met then certain code is ran. If statements become more powerful when you use logic operators. You can also use string comparison operators. To make if statements more flexible you use else and elif clauses. Else clause provdes an additional block if the condition is false. Elif allows us to add another condition if the first condition is false. Elif also needs a then. Additionally you can have nested if statements. This means embedding if statements inside other if statements. 

While loops allow you to repeatedly execute a block of code as long as a condition is being met. Good for iterating over data. While loops are also good for automating tasks.

For loops allow you to iterate over data a specific number of times. Powerful tool for automating tools and operating on data. You can generate a sequence of numbers using the `seq` command.

Break and continue commands allow you more control over loops. They allow you to interrupt or skip iterations when necessary.