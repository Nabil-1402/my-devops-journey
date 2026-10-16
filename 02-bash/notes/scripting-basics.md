# Notes

# Scripting Basics

## Key Concepts

- Scripts help automate tasks, especially large or repetitive ones.
- A shebang specifies the interpreter when running a script directly.
- Scripts can be made executable.

## Syntax and Commands

| Syntax / Command | Purpose |
| :--- | :--- |
| `#!/bin/bash` | The shebang: tells the system to run the script using Bash. |
| `#` | Starts a single-line comment. |
| `: ' ... '` | A common workaround for multiline comments, using the no-op command `:`. |
| `chmod +x name.sh` | Makes the script executable. |
| `./name.sh` | Runs an executable script from the current directory. |
| `variable_name=value` | Assigns a value to a variable. |
| `"$@"` | Expands to all arguments, preserving each as a separate argument. |
| `$((expression))` | Performs integer arithmetic expansion. |

## Example

```bash
#!/bin/bash

length="$1"
width="$2"

area=$((length * width))
perimeter=$((2 * (length + width)))

echo "Parameters used: $@"
echo "Area: $area"
echo "Perimeter: $perimeter"

: '
This script calculates the area and perimeter using
the arguments passed through the command line.
It prints the arguments, area and perimeter.
'
```

## What I Learned

I learned the basics of Bash scripting, including shebangs, comments, variables, command-line parameters and arithmetic expansion.

## Your Notes

### Running Scripts from Anywhere

You can run a script from anywhere by placing it in a directory listed in **`$PATH`**.

A common location is `/usr/local/bin`:

```bash
sudo mv name.sh /usr/local/bin/name
```

Once executable, the script can be run using `name` instead of `./name.sh`.

### Variables

**Variables** store values that scripts can reference and manipulate.

Use `$` before a variable's name to access its value:

```bash
name="Nabil"
echo "Hello, $name"
```

Using a variable inside a string is called **variable interpolation**.

Bash variables can hold strings, integers and arrays. Decimal values can be stored as text, but Bash does not support floating-point arithmetic natively.

Arrays are created using parentheses:

```bash
fruits=("apple" "banana" "orange")
```

### Command-Line Parameters

Scripts can receive arguments after the script name:

```bash
./script.sh parameter1 parameter2
```

- **`$1`** accesses the first argument.
- **`$2`** accesses the second argument.
- **`"$@"`** accesses all arguments while preserving their boundaries.

### Arithmetic Expansion

Use **`$((expression))`** to perform integer calculations with variables and parameters.

```bash
area=$((length * width))
```

This allows calculations to be incorporated into scripts, making them more dynamic and flexible.