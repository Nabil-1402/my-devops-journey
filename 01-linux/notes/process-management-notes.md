# Notes

# Process Management

## Key Concepts

- A process is a running instance of a program
- If processes are not monitored/manages properly they can impact system performance by taking up CPU power

## Commands
`ps` - Display processes
`top` - Show sorted information about processes
`htop` - An interactive version of top
`kill` - Kill a process
`fg` - Brings a background or suspended job into the foreground for active terminal interaction
`bg` - Resumes a suspended or stopped job and lets it run in the background.
`pgrep` - Find the PID of a named process
`ps aux` - View all processes on the system and the user they belong to
`jobs` - Lists all the current running jobs


## Examples

# View processes
ps aux
ps aux | grep nginx

# Real-time monitoring
top
htop  # install via: sudo apt install htop

# Background processes
sleep 100 &
jobs
fg %1  # bring to foreground
bg %1  # send to background

# Kill processes
kill <PID>
killall sleep

## What I Learned

I learned what a process is and how it is important to manage them to help mantain system performance. I learned the commands on how to view all processes, kill them and how to monitor them.

## Your Notes
- A process is a running instance of a program.
- Every process has an ID associated with it.
- Processes can run in the foreground (view it running on the terminal) or they can run in the background (you can't see it running on the terminal but it is).
- The default kill command uses sigterm 15 which is a graceful kill, kill -9 is a force kill.


