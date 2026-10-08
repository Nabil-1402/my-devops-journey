# Bash Battle Arena

The "Bash Battle Arena" is a command-line game I've designed to teach and improve Bash scripting skills in a fun and interactive way. The game presents players with a series of increasingly complex challenges that they must solve by writing Bash scripts. Each challenge is structured like a level in a game, and as players progress, they learn new Bash concepts and best practices.

## Objective

Players must complete various tasks or "missions" using Bash scripts. These tasks range from simple file manipulations to more complex system operations. The goal is to "defeat" each level by correctly solving the problem, with the ultimate aim of becoming a "Bash Master.

## Level 1: The Basics

### Mission:

Create a directory named Arena and then inside it, create three files: warrior.txt, mage.txt, and archer.txt. List the contents of the Arena directory.

## Solution:

#!/bin/bash

mkdir Arena
cd Arena
touch warrior.txt mage.txt archer.txt
ls

## Explanation:

`mkdir Arena` - Make a directory called "Arena"
`cd Arena` - Enter into the Arena directory
`touch warrior.txt mage.txt archer.txt` - Create the 3 files the task asked for
`ls` - List everything inside Arena directory


## Level 2: Variables and Loops

### Mission:

Create a script that outputs the numbers 1 to 10, one number per line

## Solution:

#!/bin/bash

for i in {1..10}; do
    echo "$i"
done

## Explanation:

`for i in {1..10}; do` - Create a for loop starting at 1 and ending at 10
`echo "$i"` - Print out the current number
`done` - Finish the for loop


## Level 3: Conditional Statements

### Mission:

Write a script that checks if a file named hero.txt exists in the Arena directory. If it does, print Hero found!; otherwise, print Hero missing!.

## Solution:

#!/bin/bash

if [ -f "Arena/hero.txt" ]; then
    echo "Hero found!"
else
    echo "Hero missing!"
fi

## Explanation:

`if [ -f "Arena/hero.txt" ]; then` - Check if hero.txt file exists inside Arena
`echo "Hero found!"` - Message printed if it is
`else echo "Hero missing!"` - Message for if condition not being met

## Level 4: File Manipulation

### Mission:

Create a script that copies all .txt files from the Arena directory to a new directory called Backup.

## Solution:

#!/bin/bash

mkdir -p Backup
cp Arena/*.txt Backup/

## Explanation:

`mkdir -p Backup` - Create a new directory called "Backup"
`cp Arena/*.txt Backup/` - Copy all the .txt files from Arena to Backup


## Level 5: The Boss Battle - Combining Basics

### Mission:

Combine what you've learned! Write a script that:

1. Creates a directory names 'Battlefield'
2. Inside Battlefield, create files named knight.txt, sorcerer.txt, and rogue.txt.
3. Check if knight.txt exists; if it does, move it to a new directory called Archive.
4. List the contents of both Battlefield and Archive.

## Solution:

#!/bin/bash

mkdir Battlefield

cd Battlefield
touch knight.txt sorcerer.txt rogue.txt

cd ..

if [ -f "Battlefield/knight.txt" ]; then
        mkdir Archive
        mv Battlefield/knight.txt Archive/
fi

ls Battlefield Archive

## Explanation:

`mkdir Battlefield` - Create a directory called "Battlefield"

`cd Battlefield` - Enter into the directory
`touch knight.txt sorcerer.txt rogue.txt` - Create the files

`cd ..` - Leave current directory to go back up one level

`if [ -f "Battlefield/knight.txt" ]; then` - Check if knight.txt exists inside Battlefield
`mkdir Archive` - Create a directory called "Archive"
`mv Battlefield/knight.txt Archive/` - Move knight.txt from Battlefield to archive
`ls Battlefield Archive` - List all the files in both directories

## Level 6: Argument Parsing

### Mission:

Write a script that accepts a filename as an argument and prints the number of lines in that file. If no filename is provided, display a message saying 'No file provided'.

## Solution:

#!/bin/bash

file_name="$1"

if [ "$#" -ne 1 ]; then
        echo "No file provided."

elif [ -f "$file_name" ]; then
        count=$(wc -l < "$file_name" | tr -d '[:space:]')
        echo "$file_name has $count lines"
else
        echo "File does not exist"
fi

## Explanation:

`file_name="$1"` - Stores the argument passed in into a variable

`if [ "$#" -ne 1 ]; then echo "No file provided."` - If the number of arguments passed in is not 1 the print this message

`elif [ -f "$file_name" ]; then count=$(wc -l < "$file_name" | tr -d '[:space:]') echo "$file_name has $count lines"` - If the file exists count the number of lines in the file and print out suitable message and trim excess white spaces

`else echo "File does not exist"` - Print message for if file does not exist


## Level 7: File Sorting Script

### Mission:

Write a script that sorts all .txt files in a directory by their size, from smallest to largest, and displays the sorted list.

## Solution:

#!/bin/bash

echo "Enter directory name to sort: "
read dir_name

if [ -d "$dir_name" ]; then
        sorted=$(ls -lSh "$dir_name" | awk 'NR > 1 {print $9, $5}')
        echo "$sorted"
else
        echo "Directory does not exist"
fi

## Explanation:

This asks the user to enter the name of a directory that they want to see sorted. Then if the directory exists I run `ls -lSh "$dir_name" | awk 'NR > 1 {print $9, $5}'` to list out the contents and order them by size and printing out the name of the file with its size. If the directory does not exist then an appropriate message is displayed.


## Level 8: Multi-File Searcher

### Mission:

Create a script that searches for a specific word or phrase across all .log files in a directory and outputs the names of the files that contain the word or phrase.

## Solution:

#!/bin/bash

echo "Enter a directory to search: "
read dir

if [ ! -d "$dir" ]; then
	echo "Directory $dir does not exist"
    exit 1
fi

echo "Enter word or phrase you want to find from $dir: "
read string

for file in "$dir"/*.log; do
    if [ -f "$file" ]; then
        search=$(grep "$string" < "$file"  2>/dev/null)
        if [ "$?" -eq 0 ]; then
            echo "$file"
        else
            continue
        fi
    else
        continue
    fi
done

## Explanation:

This asks the user to enter the name of a directory they want to search. Then checks if the directory exists, if it does not then program is stopped. If it does then it asks the user to enter the name of a word/phrase they are searching for. Then all the files ending with .log inside the directory are itterated over and the word/phrase is searched for. If it is found then the file is printed out to the user.

## Level 9: Script to Monitor Directory Changes

### Mission:

Write a script that monitors a directory for any changes (file creation, modification, or deletion) and logs the changes with a timestamp.

## Solution:

#!/bin/bash

DIRECTORY="Arena"
LOG_FILE="change_log.txt"

if [ ! -d "$DIRECTORY" ]; then
    echo "Directory does not exist."
    exit 1
fi

fswatch -r "$DIRECTORY" | while read event; do
    if [ -e "$event" ]; then
        echo "$(date +'%Y-%m-%d %H:%M:%S') File modified/created: $event" >> "$LOG_FILE"
    else
        echo "$(date +'%Y-%m-%d %H:%M:%S') File deleted: $event" >> "$LOG_FILE"
    fi
done



## Explanation:

This script checks if the directory Arena exists. Then the `fswatch` command is used with the `-r` to watch for any modifications made to the directory and any subdirectories. Then whule this is running, any changes noticed are read and stored in the event variable. If the event exists then the event and the timestap are appended to a log file.

## Level 10: Boss Battle 2 - Intermediate Scripting

### Mission:

Write a script that:

1. Creates a directory called Arena_Boss.
2. Creates 5 text files inside the directory, named file1.txt to file5.txt.
3. Generates a random number of lines (between 10 and 20) in each file.
4. Sorts these files by their size and displays the list.
5. Checks if any of the files contain the word 'Victory', and if found, moves the file to a directory called Victory_Archive.

## Solution:

#!/bin/bash

mkdir -p Arena_Boss

for num in {1..5}; do
        lines=$((RANDOM % 11 + 10))
        file="Arena_Boss/file$num.txt"

        > "$file"

        for ((i=1; i<=lines; i++)); do
                echo "This is line: $i" >> "$file"
        done
done

sorted=$(ls -lSh Arena_Boss/ | awk 'NR > 1 {print $9, $5}')
echo "$sorted"

echo "Victory" >> Arena_Boss/file3.txt

mkdir -p Victory_Archive

for file in Arena_Boss/*.txt; do
    if grep -q "Victory" "$file"; then
        mv "$file" Victory_Archive/
        echo "$file contains 'Victory' and has been moved to Victory_Archive."
    fi
done



## Explanation:

This script creates the Arena_Boss directory then runs a for loop to quickly create 5 .txt files and also during this creates a variable called lines which stores the number of lines (randomly generated between 10-20) to be in each file. Then the files are sorted by their size and printed out. then just to test that it works, "Victory" is added to a file and then a new archive is made and all files within Arena_Boss are searched to find the word "Victory". If it is found then the file containing it is moved to Victory_Archive directory.













