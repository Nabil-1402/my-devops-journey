# Projects/Hands on Learning

## Over The Wire Bandit Game (Level 0 - 20)
This is a doccument containing all my answers to levels 0 to 20 of the over the wire bandit games to strengthen and reinforce my linux learning.

## Level 0
- ssh bandit0@bandit.labs.overthewire.org -p 2220
- Password: bandit0

**Level Goal**: 

The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

**Solution:**

cat readme

**Explanation:**
Simply just read the file using `cat` command.

**Password:** [6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR]

## Level 1
- ssh bandit1@bandit.labs.overthewire.org -p 2220
- Password: 6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR

**Level Goal**: 

The password for the next level is stored in a file called - located in the home directory

**Solution:**

ls

cat ./-

**Explanation:**

I used `ls` to list the files then used `cat ./-` instead of cat - because using cat - results in nothing as it is expecting inputs. Using ./ indicates that its a file.

**Password:** [PK8fYLZg2hnHSz83plBL1iEPKdD3QToB]

## Level 2
- ssh bandit2@bandit.labs.overthewire.org -p 2220
- Password: PK8fYLZg2hnHSz83plBL1iEPKdD3QToB

**Level Goal**: 

The password for the next level is stored in a file called --spaces in this filename-- located in the home directory

**Solution:**

ls

cat ./--spaces\ in\ this\ filename--

**Explanation:**

Since the file name has spaces in it I cannot just use cat and then the name with spaces, I have to either use `./ filename ` with \ used to indicate spaces. Alternatively I could use cat filename in speech marks to also retrieve the password.

**Password:** [7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME]

## Level 3
- ssh bandit3@bandit.labs.overthewire.org -p 2220
- Password: 7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME

**Level Goal**: 

The password for the next level is stored in a hidden file in the inhere directory.

**Solution:**

ls

cd inhere

ls -a

cat ./...Hiding-From-You 

**Explanation:**

I change directory to enter into the inhere directory using `cd`. Then since I am told the password is in a hidden file i use `ls -a`. The `-a` flag is used to say that I want to list **all** files within the directory including hidden ones. Then I just read from it to get the password.

**Password:** [xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq]

## Level 4
- ssh bandit4@bandit.labs.overthewire.org -p 2220
- Password: xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq

**Level Goal**: 

The password for the next level is stored in the only human-readable file in the inhere directory.

**Solution:**

ls

cd inhere

ls

file ./*

cat ./-file07

**Explanation:**
I need to find the only human readable file in the directory and to do that I need to find the file which is in ASCII text. To do this I use `file ./*` to find the type of all the files in the directory.

**Password:** [6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG]

## Level 5
- ssh bandit5@bandit.labs.overthewire.org -p 2220
- Password: 6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG

**Level Goal**: 

The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

human-readable
1033 bytes in size
not executable

**Solution:**

ls

cd inhere

find -type f -size 1033c ! -executable

cat ./maybehere07/.file2

**Explanation:**

Using the `find` command to look for a file which matches the requirements is what was needed at this level. `-type` flag indicates what type of object I am looking for, `-size `is the size of the file with the c with the number indicates bytes, and `! -executable` to exclude executable files from the search.

**Password:** [pXa26xhMWaC2SvDotA4r9EgZkulOeSBW]

## Level 6
- ssh bandit6@bandit.labs.overthewire.org -p 2220
- Password: pXa26xhMWaC2SvDotA4r9EgZkulOeSBW

**Level Goal**: 

The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7
owned by group bandit6
33 bytes in size

**Solution:**

find / -type f -user bandit7 -group bandit6 -size 33c 2> /dev/null

cat /var/lib/dpkg/info/bandit7.password

**Explanation:**

Using `find` but starting at the root (/) to search the entire server and then filter it based on user, group and size. Finally `2> /dev/null` is used to redirect and permission denied / error messages into /dev/null to just show the files we can access.


**Password:** [Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3]

## Level 7
- ssh bandit7@bandit.labs.overthewire.org -p 2220
- Password: Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3

**Level Goal**: 

The password for the next level is stored in the file data.txt next to the word millionth

**Solution:**

cat data.txt | grep millionth

**Explanation:**

Here I used `cat` to read the file and using `|` (pipe) to use that as in input into my second command `grep` which I used to look for the word "millionth".

**Password:** [VR1ljMayciFxbnUokuQmJFw6QC9VKtub]

## Level 8
- ssh bandit8@bandit.labs.overthewire.org -p 2220
- Password: VR1ljMayciFxbnUokuQmJFw6QC9VKtub

**Level Goal**: 

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

**Solution:**

sort data.txt | uniq -u

**Explanation:**

Here I need to find a unique line in the text. To do this I use `uniq -u` to find a unique line but before I do that I need to sort the text in the file first using `sort`.

**Password:** [EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl]

## Level 9
- ssh bandit9@bandit.labs.overthewire.org -p 2220
- Password: EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl

**Level Goal**: 

The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

**Solution:**

strings data.txt | grep "==="

**Explanation:**

Here I use the `strings` command to use the list of all human readable strings in the file then use that as the input to find all the cases with multiple =s.

**Password:** [B0s2khmbT9u0geKuOoVGW3JZKhndE3BG]

## Level 10
- ssh bandit10@bandit.labs.overthewire.org -p 2220
- Password: B0s2khmbT9u0geKuOoVGW3JZKhndE3BG

**Level Goal**: 

The password for the next level is stored in the file data.txt, which contains base64 encoded data

**Solution:**

base64 -d data.txt

**Explanation:**

I use `base64 -d` because I am told the file is encoded in base64 and the -d flag is use to decode it.

**Password:** [pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro]

## Level 11
- ssh bandit11@bandit.labs.overthewire.org -p 2220
- Password: pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro

**Level Goal**: 

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

**Solution:**

cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'

**Explanation:**

To do this I need to use the `tr` command to translate the rotations. 13 positions make A to go N. Need to do this translation for upper case and lower case letters. The difficult part here was understanding the syntax of the command.

**Password:** [GROozWPO8QyN0mGrjUkID0WCYkZiQxrN]

## Level 12
- ssh bandit12@bandit.labs.overthewire.org -p 2220
- Password: GROozWPO8QyN0mGrjUkID0WCYkZiQxrN

**Level Goal**: 

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

**Solution:**

cd /tmp

mktemp -d

cd tmp.2DOE2e8Y5m/

cp ~/data.txt /tmp/tmp.2DOE2e8Y5m

mv data.txt hexdump.txt

head hexdump.txt

xxd -r hexdump.txt compressed_data

mv compressed_data compressed_data.gz

gzip -d compressed_data.gz 

xxd compressed_data 

mv compressed_data compressed_data.bz2

bzip2 -d compressed_data.bz2 

xxd compressed_data

mv compressed_data compressed_data.gz

gzip -d compressed_data.gz 

xxd compressed_data 

mv compressed_data compressed_data.tar

tar -xf compressed_data.tar 

xxd data5.bin 

tar -xf data5.bin

xxd data6.bin

bzip2 -d data6.bin

xxd data6.bin.out

tar -xf data6.bin.out

xxd data8.bin

gzip -d data8.bin

xxd data8.bin

mv data8.bin data8.gz

gzip -d data8.gz

head data8

**Explanation:**

This task took a long time as I had to wrap my head around understanding how files are compressed and decompressed and the different types of files. Key things to not in this task is that if the first line of the hex dump contains **18fb 08** then I can decompress the file using `gzip -d` given the file has a suffix of `.gz`. If the first line contains **425a** then you can decompress with `bzip2 -d` given the file has a suffix of `.bz2`. Finally if the first line contains **6461** then you can use `tar -xf` given it is a tar file (ending in `.tar`). In this task you repeated encode/decode the hexdump and also decompress given the file type.

**Password:** [qQYQiHOBPR8zR61qxYqX45quvihF2uzk]

## Level 13
- ssh bandit13@bandit.labs.overthewire.org -p 2220
- Password: qQYQiHOBPR8zR61qxYqX45quvihF2uzk

**Level Goal**: 

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.
If you need help with this level: a hint file can be found in the home directory.
Make sure to read the error messages as they are informative.

**Solution:**

ls

exit

scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .

ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220

**Explanation:**

I need to use the password given to access level 14. First thing I need to do is do a send a file safely onto a remote host. This is done using `scp`. With this command I copy the file over to the remote host using openSSH which is secure. Then I SSH into level14 using `-i` flag to allow login with a private key

**Password:** [No password]

## Level 14
- ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
- Password: No password

**Level Goal**: 

The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

**Solution:**

cat /etc/bandit_pass/bandit14

nc localhost 30000

aaWecNkG4FhxJQxz07uiwzVP6bJiYS65 (password)

**Explanation:**

First thing you need to do is use the information given in level 13 to find the password stored on level 14. Then using `nc` or `netcat` I can read and write data over a network connection. I just enter the hostname along with the port it's listening on to read and write to/from it.

**Password:** [pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7]

## Level 15
- ssh bandit15@bandit.labs.overthewire.org -p 2220
- Password: pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7

**Level Goal**: 

The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption

**Solution:**

openssl s_client -connect localhost:30001

pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7 (password)

**Explanation:**

openssl s_client is the implementation of a simple client that connects to a server using SSL/TLS. Since the task states that the password can be retrieved using SSL encryption, I connect to the localhost server with the OpenSSL client and send the password from this level. The server then sends back the password for the next level.

**Password:** [kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V]

## Level 16
- ssh bandit16@bandit.labs.overthewire.org -p 2220
- Password: kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V

**Level Goal**: 

The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

**Solution:**

nmap -sV localhost -p 31000-32000

openssl s_client -connect localhost:31790 -quiet


**Explanation:**

I use `nmap` to scan all services ports between port number 31000 and 32000. When I find the open ones I look for service `ssl/unknown`. Then I open a connection with this service and enter this level's password to get the private key.


**Password:** [RSA private key]

## Level 17
- ssh -i sshkey17.private bandit17@bandit.labs.overthewire.org -p 2220

**Level Goal**: 

There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

**Solution:**

diff passwords.old passwords.new 


**Explanation:**

Use the `diff` command to find the difference between the two files


**Password:** [kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd]

## Level 18
- ssh bandit18@bandit.labs.overthewire.org -p 2220
- Password: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

**Level Goal**: 

The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

**Solution:**

ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme


**Explanation:**

The .bashrc is a file that is ran when a shell is open and our usual way of sshing into this level involves loading a shell but now this .bashrc will prevent us from loading/using the shell. Instead what we do is write the command we want to perform in the same line we open the ssh connection to recieve the output of the file.

**Password:** [IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x]

## Level 19
- ssh bandit19@bandit.labs.overthewire.org -p 2220
- Password: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

**Level Goal**: 

To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

**Solution:**

./bandit20-do cat /etc/bandit_pass/bandit20

**Explanation:**

Suid is a special permission. It will replace the x of the user permission. It means the binary will be run as the owner of the binary, not the one executing it. This gives temporary access to being able to do what bandit20 can do.

**Password:** [GbKksEFF4yrVs6il55v6gwY5aVje5f0j]

## Level 20
- ssh bandit20@bandit.labs.overthewire.org -p 2220
- Password: GbKksEFF4yrVs6il55v6gwY5aVje5f0j

**Level Goal**: 

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21)

**Solution:**

open another terminal and use nc -lvp 9999

on original terminal type in ./suconnect 9999

on other terminal enter password for level 20

original terminal recieves it and send new password to new terminal.

**Explanation:**

In order to get the passsword I needed to set up an extra terminal. In this terminal I ssh into bandit20 but here what I do is make it listen on any port using `nc -lvp 9999`. Now this terminal has port 9999 open and listening, able to recieve data. In my original terminal I use the setuid binary and call it with the port number that is listening on the new terminal.
As a result the new terminal is prompted and I enter level 20's password. This data is sent back and acknowledged by the original terminal and the new password is sent back to the new terminal.

**Password:** [gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr]






