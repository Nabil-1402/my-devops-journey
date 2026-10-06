# Notes

# Environment Variables and File Handling

## Key Concepts

- What are environment variables and the standard ones
- How to read a file and lines in a file
- How to write to a file
- What a file checksum is and how to compare two file's checksum

## Commands

`$LOGNAME` - Standard env variable which represents the login name of the current user

`$SHELL` - Standard env variable which stores the path of the current user's shell

`$PWD` - Standard env variable which represents the current working directory

`$PATH` - Standard env variable which prints out the different types of executable search paths and where the binaries are located

`$LANG` - Standard env variable which represents the default language settings

`read` - Read lines from a file

`md5sum` - used to generate a file checksum

`sha256sum` - used to generate a sha256 checksum

## Examples

#!/bin/bash

my_home="$HOME"

my_user="$USER"

my_os="$OSTYPE"

echo "Home Director: $my_home"

echo "Current user: $my_user"

echo "OS Type: $my_os"


#!/bin/bash

read_file(){

    local file_path=$1

    while IFS= read -r line; do

        echo "$line"

    done < "$file_path"

}

read_file "./log.txt"

#!/bin/bash

compare_checksums(){

    local checksum1="$1"

    local checksum2="$2"

    if [[ "$checksum1" == "$checksum2" ]]; then

        echo "checksums match. File hask kept integrity"

    else

        echo "checksums do not match. File compromised"

    fi

}

compare_checksums "123" "123"

## What I Learned

I learned what environment variables are, their naming convention and the standard environment variables. I also learned about file handling operators such as reading a file and writing to a file. Additionally I learned what a file checksum is and what it is used for.

## Your Notes

Environment variables are notated with fully upper case characters. Environment variables can also be assigned to local variables making it easier to reference them later. 

Standard environment variables give us insights into various aspects of the system, user and runtime environment. They provide information that can help us create more robust and adaptable bash scripts. 

Reading files is an important task in scripting, it allows us to access and extract valuable information from various types of files. You use the `read` command to read each line in the file. You can also use the `cat` command to read files.

Writing files allow us to create, modify and store information in various formats. You can use the `>` or `>>` symbol to store the contents from one parameter to another. 

File checksums are cryptographic hashes that provide a unique fingerprint for a file which allows us to verify the authenticity of the file. Every file has a file checksum that is different from another file. Another commonly used algorithm for file checksums is SHA256. Checksums are especially useful when we need to compare the integrity of a file over time or across different systems. So we can use it to compare two different checksums and see if their values match. 