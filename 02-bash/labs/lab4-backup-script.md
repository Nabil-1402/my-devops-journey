# Labs

# Lab: [Backup Script for Text Files]

## Objective

Create a script that backs up all .txt files from one directory to another.

Requirements:
- Prompt user for source directory
- Create a backup directory if it doesn't exist
- Copy all .txt files to the backup directory
- Add timestamp to backup directory name
- Display count of files backed up


## Commands Used

#!/bin/bash

echo "Enter source directory: "

read -r dir_name

if [ ! -d "$dir_name" ]; then

    echo "$dir_name directory does not exist"

    exit 1

else

    backup_dir="backup_$(date +%Y-%m-%d_%H-%M-%S)"

    mkdir -p "$backup_dir" || exit 1


    echo "Backup directory created: $backup_dir"

    echo "Copying .txt files...."

    count=0

    for file in "$dir_name"/*.txt; do

        [ -f "$file" ] || continue

        if cp "$file" "$backup_dir/"; then

            count=$((count + 1))

        fi

    done

fi

echo "Backup complete! Files backed up: $count"

## Output

For this task I created a directory beforehand called `test/`. I then created 3 files: `t1.xtx t2.txt t3.txt`. Then I used this as my first input and this was the result:

Enter source directory: 

test

Backup directory created: backup_2026-10-06_16-25-17

Copying .txt files....

Backup complete! Files backed up: 3


Then I confirmed by running `ls` on test and the backup directory made.


I then tested with a nonexistent source directory and got the following:

Enter source directory: 

nonexistent

nonexistent directory does not exist
## Challenges

The challenge here was finding out how to iterate over a directory to find files ending in .txt. To resolve this I found out how to do so using stackoverflow. Another challenge was how to add a time stamp and to get over that I searched up how to do that and found the regular expression to add one.

## What I Learned

In this lab I learned how to use for loops, exit code, iterating over a directory and dynamic variables in a bash script. 

