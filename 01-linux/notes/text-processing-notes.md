# Notes

# Text Processing

## Key Concepts

- Filtering
- Sorting
- Searching
- Changing text

## Commands


`awk` - pattern-directed scanning and processing language
`sed` - The sed utility reads the specified files, or the standard input if no files are specified, modifying the input as 
`grep` - Find a matching expression
`sort` - Sort text and numbers in a file
`uniq` - flter text files based on unique characteristics
`wc` - word count 
`tr` - translate
`>` - write to a file / stdin (this overwrites contents in a file)
`>>` - append to a file /stdin (this does not overwrite a file)

## Examples

# Search with grep
grep "error" /var/log/syslog
grep -r "TODO" ~/projects/

# Advanced grep
grep -i "failed" /var/log/auth.log | wc -l  # count failed login attempts

# awk examples
ps aux | awk '{print $1, $11}'  # print user and command
cat /etc/passwd | awk -F: '{print $1, $6}'  # print username and home dir

# sed examples
sed 's/old/new/g' file.txt  # replace text
sed -n '10,20p' file.txt    # print lines 10-20

# Piping chains
cat /var/log/syslog | grep "error" | awk '{print $1, $2, $3}' | sort | uniq

## What I Learned

I learned how to work with text files and use them to find, replace, searc, and filter based on the information I need

## Your Notes
