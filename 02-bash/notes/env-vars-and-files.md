# Notes

# Environment Variables and File Handling

# 📂 Environment Variables and File Handling

## Key Concepts

- Environment variables and common examples
- Reading files line by line
- Writing and appending to files
- Generating and comparing file checksums

## Variables and Commands

### Common Variables

| Variable | Purpose |
| :--- | :--- |
| `$HOME` | The current user's home directory. |
| `$USER` | The current user's username in typical shell environments. |
| `$LOGNAME` | The user's login name. |
| `$SHELL` | The user's configured login shell, not necessarily the shell currently running. |
| `$PWD` | The current working directory. |
| `$PATH` | A colon-separated list of directories searched for executable commands. |
| `$LANG` | The default locale, including language and character encoding settings. |
| `$OSTYPE` | A Bash variable describing the operating system. |

### File Handling

| Command / Operator | Purpose |
| :--- | :--- |
| `read -r line` | Reads a line into a variable without interpreting backslash escapes. |
| `cat <file>` | Prints a file's contents. |
| `<` | Redirects a file into a command's standard input. |
| `>` | Redirects output to a file, creating it or overwriting its contents. |
| `>>` | Appends output to a file, creating it if needed. |
| `md5sum <file>` | Generates an MD5 checksum. |
| `sha256sum <file>` | Generates a SHA-256 checksum. |

> On macOS, use `shasum -a 256 <file>` for SHA-256 or `md5 <file>` for MD5.

## Examples

### Accessing Variables

```bash
#!/bin/bash

my_home="$HOME"
my_user="$USER"
my_os="$OSTYPE"

echo "Home directory: $my_home"
echo "Current user: $my_user"
echo "OS type: $my_os"
```

### Reading a File Line by Line

```bash
#!/bin/bash

read_file() {
    local file_path="$1"
    local line

    while IFS= read -r line || [[ -n "$line" ]]; do
        printf '%s\n' "$line"
    done < "$file_path"
}

read_file "./log.txt"
```

- **`IFS=`** preserves leading and trailing whitespace.
- **`-r`** preserves backslashes.
- **`|| [[ -n "$line" ]]`** handles a final line without a trailing newline.

### Writing to a File

```bash
# Create or overwrite a file
printf '%s\n' "First entry" > log.txt

# Append another line
printf '%s\n' "Another entry" >> log.txt
```

### Comparing Checksums

```bash
#!/bin/bash

compare_checksums() {
    local checksum1="$1"
    local checksum2="$2"

    if [[ "$checksum1" == "$checksum2" ]]; then
        echo "Checksums match."
    else
        echo "Checksums differ. The file contents may have changed."
    fi
}

compare_checksums "123" "123"
```

> This example compares supplied strings. Use a checksum command to calculate actual file hashes first.

## What I Learned

I learned how environment variables provide information about the system and user, and how to reference them in Bash scripts.

I also learned how to read files, write and append content, and compare checksums to check file integrity.

## Your Notes

### Environment Variables

**Environment variables** pass configuration and information to processes.

Their names conventionally use **UPPERCASE**, although this is not required. Shell variables can store their values for later use.

Use `export` when a variable needs to be available to child processes:

```bash
export APP_ENV="development"
```

### Reading Files

Reading files lets scripts access and process stored information.

- Use **`read`** in a loop to process a file line by line.
- Use **`cat`** to print a file's contents.

### Writing Files

Output redirection lets scripts create files and store information.

- **`>`** creates or overwrites a file.
- **`>>`** appends to a file.

### File Checksums

A **checksum** is a value calculated from a file's contents. Cryptographic hashes such as **SHA-256** act as fingerprints for detecting changes.

- Identical file contents produce identical hashes with the same algorithm.
- Different contents are overwhelmingly likely to produce different SHA-256 hashes.
- A mismatch indicates different content, not necessarily malicious activity.
- A match supports integrity verification when compared against a trusted expected hash.

Checksums are useful for comparing files across systems or checking whether a file has changed over time.

> A checksum alone does not prove authenticity. SHA-256 is preferred over MD5 for security-sensitive integrity checks.