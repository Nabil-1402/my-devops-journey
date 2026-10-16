# Notes

# Error Handling and Exit Codes

# 🛠️ Error Handling and Exit Codes

## Key Concepts

- Error handling helps scripts respond predictably when something goes wrong.
- Exit codes indicate whether commands succeeded.
- `set` options support error detection and debugging.

## Commands

| Command | Purpose |
| :--- | :--- |
| `exit 0` | Exits the script successfully. |
| `exit 1` | Exits the script with a general failure status. |
| `echo "$?"` | Prints the exit status of the previous command. |
| `command -v <command>` | Checks whether a command can be found. |
| `set -e` | Exits on an unhandled command failure, subject to Bash's exceptions. |
| `set -u` | Treats expansion of unset variables as an error. |
| `set -x` | Prints expanded commands to standard error before executing them. |
| `set +x` | Disables command tracing. |
| `set -o nounset` | Equivalent to `set -u`. |
| `set -o errexit` | Equivalent to `set -e`. |
| `set -o pipefail` | Makes a pipeline return the rightmost non-zero status, or zero if all commands succeed. |
| `set -eux` | Enables `-e`, `-u` and `-x` together. |

## Examples

### Handling Division by Zero

```bash
#!/bin/bash

num1=10
num2=0

if [ "$num2" -eq 0 ]; then
    echo "Error: Division by zero is not allowed." >&2
    exit 1
fi

result=$((num1 / num2))

echo "The result is: $result"
```

> `>&2` sends the error message to standard error.

### Enabling Error Checks and Debugging

```bash
#!/bin/bash

set -eux

echo "This is a test."

x=10
echo "The value of x is: $x"

nonexistentcommand

# This line is not reached because the previous command fails.
echo "Script complete."
```

## What I Learned

I learned how to use conditionals and exit codes to handle failures and provide helpful error messages.

I also learned how Bash's `set` options can detect problems earlier and show which commands are being executed when debugging.

## Your Notes

### Error Handling

**Error handling** means anticipating possible failures and deciding how the script should respond.

A failed command does not normally stop a Bash script automatically. Without appropriate checks, the script may continue and produce unexpected results.

Use conditionals to detect problems, explain what happened and exit with a suitable status when necessary.

### Exit Codes

Commands and scripts return an **exit status** when they finish.

- **`0`:** Success.
- **Non-zero:** Failure or another command-specific outcome.

Use `echo "$?"` immediately after a command to inspect its status.

> A non-zero status is not always an unexpected error. For example, `grep` returns `1` when it finds no matches.

### Stopping on Failures with `set -e`

`set -e` can stop a script when an unhandled command fails, helping prevent later commands from running with incorrect assumptions.

However, it has exceptions, including commands tested in `if` conditions and many uses of `&&` or `||`.

It supports explicit error handling rather than replacing it.

### Detecting Unset Variables with `set -u`

`set -u` treats attempts to expand unset variables as errors and normally exits a non-interactive script.

This helps catch spelling mistakes and missing values.

> An unset variable is different from a variable deliberately assigned an empty value.

### Debugging with `set -x`

`set -x` enables command tracing, showing expanded commands before execution.

Use `set +x` to turn tracing off. These commands mark the start and end of tracing; they do not pause execution like breakpoints.

> Tracing can expose passwords, tokens and other sensitive values. Avoid tracing commands that handle secrets.

### Checking Pipelines with `pipefail`

Normally, a pipeline returns the exit status of its final command.

With `set -o pipefail`, it returns the status of the **rightmost failed command**, making earlier failures easier to detect.

### Combining Options

Use the following to enable failure checks, unset-variable checks and tracing together:

```bash
set -eux
```

To also check for failures earlier in pipelines:

```bash
set -euxo pipefail
```