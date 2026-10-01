# Labs

# Lab: Text Processing 

## Objective

Parse /etc/passwd to list all users with /bin/bash as their shell. Document your command.

## Commands Used

cat /etc/passwd | awk -F ':' '$7 == "/bin/bash" {print $1}'

## Output

_mbsetupuser

## Challenges

The challenge I faced was that I was getting the incorrect name. The reason for this is because i initially did the condition on $3 instead of $7 which is why when I tested what I got with cat /etc/passwd | grep /bin/bash I got something different. The way I solved this was by researching the column that the shell is shown and that gave me $7 and that fixed the problem.

## What I Learned

The shell is shown on the 7th column for /etc/passwd and that awk can be used in a similar way to grep but it has more functionality.

