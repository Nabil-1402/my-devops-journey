# Labs

# Lab: Process Management

## Objective

Start a long-running process in the background, find its PID, and kill it. Document the commands used.

## Commands Used

sleep 90000 &

jobs

pgrep sleep

kill 33058

jobs

## Output

This is what happend at each stage:
    - the first command created a process which was just sleep and immediately ran it in the background using &
    - jobs was used to check that it was running
    - pgrep sleep was to find the PID of the process
    - kill 33058 was used to kill the process
    - jobs was used to confirm that the process was gone as no jobs were running

## Challenges

No challenges were faced

## What I Learned

How to create a process and put it in the background and find its PID to kill it while it is in the background.

