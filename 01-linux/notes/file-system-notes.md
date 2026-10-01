# Notes

# File Systems

## Key Concepts

- In linux everything is treated as a file
- Files are stored as a tree structure

## Commands

`cd` - Change directory
`ls` - List all files and directories
`pwd` - Print working directory
`touch` - Create a file
`mkdir` - Create a directory
`cp` - Copy a file or directory
`mv` - Move or rename a file/directory 
`rm` -Remove a file
`cat` - Concatenate files or read from files
`less` - Display contents of a file
`head` - Display n amount of lines from the beginning of a file
`tail` - Display n amount of lines from the end of a file


## Examples

# Navigation
cd /var/log
ls -lah
pwd

# File operations
touch test.txt
mkdir -p projects/demo
cp test.txt projects/demo/
mv projects/demo/test.txt projects/demo/backup.txt
rm projects/demo/backup.txt

# Viewing files
cat /etc/passwd
less /var/log/syslog
head -n 20 /etc/services
tail -f /var/log/auth.log

## What I Learned
File systems are a crucial topic to learn in linux. Everything is linux is treated as a file which is why it's so important to learn. In this topic I learnt how to navigate around the file system, create and delete files/directories. Aswell as how to move, copy and rename files/directories. Also how to read from files/directories.

## Your Notes
`/usr` - stores Unix System Resources
`/bin` - stores essential command binaries
`/srv` - stores site-specific data served by the system
`/dev` - stores device files
`/boot` - stores system boot loader files
`/etc` - stores host-specific system-wide configuration files
`/tmp` - stores temporary files
`/lib` - stores shared library modules
`/run` - stores runtime program data
`/sys` - stores virtual directory providing info about this system
`/proc` - stores the interface to kernel data structures
`/mnt` - stores temporary mounted file systems
`/opt` - stores add-on application software packages
`/home` - stores user home directory
`/root` - stores home directory for root user
`/var` - stores file that is expected to continously change
`/sbin` - stores system binaries
`/media` - stores media file such as CD-ROM