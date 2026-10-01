# Labs

# Lab: Permission and Ownership

## Objective

Create a file that only you can read/write, but others can only read. Document the command.

## Commands Used

touch test_file.txt 

sudo chmod 644 test_file.txt

ls -l test_file.txt

## Output

After running the above I got this as the output: -rw-r--r-- 

This shows that the owner (me) can read and write while the others can only read.

## Challenges

The only issue I faces was initially writing the wrong numbers for permissions. I first put 622 instead of 644 which meant that while I can read and write the others can only write and not only read.

## What I Learned

4 is reading, 2 is for writing and 1 is for executing

