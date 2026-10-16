# Notes

# Functions and Piping

## Key Concepts

- Functions organise reusable blocks of code.
- Functions accept arguments and return an exit status.
- User input makes scripts interactive.
- Pipes connect the output of one command to another.

## Syntax and Parameters

| Syntax / Parameter | Purpose |
| :--- | :--- |
| `function_name() { ...; }` | Defines a function. |
| `function_name p1 p2` | Calls a function with arguments. |
| `local variable_name="value"` | Creates a local variable inside a function. |
| `$1`, `$2` | Access the first and second positional arguments. |
| `$#` | Holds the number of positional arguments. |
| `$0` | Usually contains the script's invocation name; it does not become the function name. |
| `read -r name` | Reads user input into a variable without interpreting backslash escapes. |
| `return 1` | Ends a function with a failure status. |
| `command1 \| command2` | Passes the first command's standard output to the second command's standard input. |

## Examples

### Defining and Calling a Function

```bash
#!/bin/bash

hello_world() {
    echo "Hello World"
}

hello_world
```

### Reading User Input

```bash
#!/bin/bash

greet_user() {
    local name

    echo "What is your name?"
    read -r name

    echo "Hello, $name!"
}

greet_user
```

### Using Arguments or User Input

```bash
#!/bin/bash

greet() {
    local name

    if [ "$#" -eq 0 ]; then
        echo "What is your name?"
        read -r name
    else
        name="$1"
    fi

    if [[ -z "$name" ]]; then
        echo "Error: Name cannot be empty." >&2
        return 1
    fi

    echo "Hello, $name!"
}

greet "Nabil"
```

### Counting Files with a Pipe

```bash
#!/bin/bash

get_file_count() {
    local directory="${1:-.}"
    local file_count

    if [[ ! -d "$directory" ]]; then
        echo "Error: Directory does not exist." >&2
        return 1
    fi

    file_count=$(
        find "$directory" -maxdepth 1 -type f -exec printf 'x\n' \; |
            wc -l
    )

    echo "Number of files in $directory: $file_count"
}

get_file_count "./"
```

This counts regular files directly inside the directory, including hidden files, without counting subdirectories.

## What I Learned

I learned how functions organise scripts into reusable sections and accept arguments or user input.

I also learned how to validate input using conditionals, return a failure status when necessary, and use pipes to combine commands.

## Your Notes

### Functions

**Functions** group related commands into reusable blocks, helping keep scripts organised and easier to maintain.

Call a function by writing its name followed by any arguments. Use **local variables** to keep function-specific values separate from the rest of the script.

> In Bash, `return` supplies a numeric exit status, not a general data value. Functions commonly output data using `printf` or `echo`, which callers can capture with `$(...)`.

### Positional and Special Parameters

- **Positional parameters**, such as `$1` and `$2`, access arguments passed to a script or function.
- **Special parameters**, such as `$#`, provide information about the current execution context.
- Inside a function, `$#` counts that function's arguments, while `$0` still refers to the script or shell.

### User Input

The **`read`** command stores input entered through the terminal in a variable.

This allows scripts to respond to users rather than relying only on fixed values.

### Input Validation

Invalid or unexpected input can cause errors or unwanted behaviour.

Use conditionals to check input before using it. If a function cannot continue, provide a helpful message and use `return 1`.

**Validation** checks whether input is acceptable. **Sanitisation** transforms or cleans input when appropriate.

### Piping

A **pipe**, written as `|`, passes one command's standard output into another command's standard input.

For example:

```bash
printf '%s\n' "apple" "banana" "orange" | wc -l
```

Here, `printf` produces three lines and `wc -l` counts them.