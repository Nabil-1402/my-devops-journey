# Labs

# Lab: [File Operations Script]

## Objective

Create a script that automates directory and file creation.

Requirements:
- Create a directory called bash_demo
- Navigate into the directory
- Create a file called demo.txt
- Write text to the file (include current date)
- Display the file contents

## Commands Used

#!/bin/bash

dir_name="bash_demo"

mkdir "$dir_name"

echo "Directory $dir_name created"

cd "$dir_name"

file_name="demo.txt"

touch "$file_name"

echo "File $file_name created"

date > "$file_name"

echo "File contents: "

cat "$file_name"

## Output
This was the output from the terminal:

Directory bash_demo created

File demo.txt created

File contents: 

Tue  6 Oct 2026 15:32:38 BST

## Challenges

No challenges were faced in this project.

## What I Learned

In this lab I learned how to comfortably use local variables in bash scripts mixed with basic commands.

