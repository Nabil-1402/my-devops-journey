# Labs

# Lab: [File Checker with Permissions]

## Objective

Create a script that checks if a file exists and displays its permissions.

Requirements:
- Prompt user for a filename
- Check if the file exists
- If it exists, check if it's readable, writable, and executable
- Display appropriate messages for each permission

## Commands Used

#!/bin/bash

echo "Enter filename to check: "

read file_name

if [ -f "$file_name" ]; then

        if [ -r "$file_name" ]; then
                
                readable="File is readable"
        
        else
                
                readable="File is not readable"
        
        fi

        if [ -w "$file_name" ]; then
                
                writable="File is writable"
        
        else
                
                writable="File is not writable"
        
        fi

        if [ -x "$file_name" ]; then
                
                exe="File is executable"
        
        else
                
                exe="File is not executable"
        
        fi
        
        echo "$file_name exists. $readable, $writable, $exe"

else
        
        echo "$file_name does not exist"

fi
## Output

I created a demo.txt file and gave it read permissions only. For this test this was the output:

Enter filename to check: 

demo.txt

demo.txt exists. File is readable, File is not writable, File is not executable


Second test I created a demo2.txt and gave it all permissions. this was the output: 

Enter filename to check: 

demo2.txt

demo2.txt exists. File is readable, File is writable, File is executable

Final test case I entered a random file name that does not exist and it gave this output:

Enter filename to check: 

nonexistentfile

nonexistentfile does not exist


## Challenges

The challenge I faced here was realising this task required nested if statements and I overcame this by trying to solve the problem in python which is a language I am familar with then translating that into bash.

## What I Learned

I learned how to write bash scripts with nested if statements.

