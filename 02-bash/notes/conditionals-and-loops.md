# Notes

# Conditionals and Loops

## Key Concepts

- **Conditionals** choose which code to run based on a condition.
- **Loops** repeat actions or iterate over data.
- **Break and continue** control loop execution.

## Syntax and Operators

### Numeric Comparisons

| Operator | Meaning |
| :--- | :--- |
| `-eq` | Equal to |
| `-ne` | Not equal to |
| `-lt` | Less than |
| `-gt` | Greater than |
| `-le` | Less than or equal to |
| `-ge` | Greater than or equal to |

### Conditions and Loop Controls

| Syntax / Operator | Purpose |
| :--- | :--- |
| `if condition; then ... fi` | Runs code when a condition succeeds. |
| `else` | Provides an alternative when previous conditions are false. |
| `elif condition; then` | Checks another condition if previous conditions are false. |
| `&&` | Logical AND: runs the next command only if the previous command succeeds. |
| `||` | Logical OR: runs the next command only if the previous command fails. |
| `[[ "$a" == "$b" ]]` | Checks whether two strings are equal in Bash. |
| `[[ "$a" != "$b" ]]` | Checks whether two strings are different in Bash. |
| `while condition; do ... done` | Repeats while a condition succeeds. |
| `for variable in items; do ... done` | Iterates over a list of items. |
| `${#arrayName[@]}` | Returns the number of elements in an array. |
| `$(seq 1 5)` | Generates numbers from 1 to 5 using command substitution. |
| `break` | Exits the current loop early. |
| `continue` | Skips the rest of the current iteration. |

> When using `[ ... ]`, spaces are required after `[` and before `]`. Quote variable expansions, for example `[ "$age" -ge 18 ]`.

## Examples

### If Statement

```bash
#!/bin/bash

age=25

if [ "$age" -ge 18 ]; then
    echo "You are an adult"
else
    echo "You are not an adult"
fi
```

### While Loop

```bash
#!/bin/bash

fruits=("apple" "banana" "orange")
index=0

while [ "$index" -lt "${#fruits[@]}" ]; do
    echo "Fruit: ${fruits[$index]}"
    index=$((index + 1))
done
```

### For Loop

```bash
#!/bin/bash

for number in $(seq 1 5); do
    echo "Number: $number"
done
```

## What I Learned

I learned how to create if statements, for loops and while loops, including how to iterate over arrays.

I also learned how to use comparison and logical operators, exit loops early with `break`, and skip iterations with `continue`.

## Your Notes

### If Statements

**If statements** allow a script to branch based on conditions.

- **`if`:** Runs a block when its condition succeeds.
- **`elif`:** Checks another condition if earlier conditions are false.
- **`else`:** Runs an alternative block if none of the conditions succeed.
- **`fi`:** Ends the if statement.

Logical operators and string comparisons allow more detailed conditions. Each `elif` requires a `then`.

You can also **nest if statements** by placing one inside another.

### While Loops

**While loops** repeatedly execute a block of code while a condition succeeds.

They are useful for repeated checks, iterating through data and automating tasks.

The condition must eventually become false, or the loop must be exited explicitly, to avoid an unintended infinite loop.

### For Loops

**For loops** iterate over a list of values, such as array elements or a sequence of numbers.

They are useful for performing the same action on multiple items. The `seq` command can generate a numeric sequence.

### Break and Continue

| Command | Behaviour |
| :--- | :--- |
| **`break`** | Stops the current loop immediately. |
| **`continue`** | Skips the remaining code in the current iteration and moves to the next iteration. |