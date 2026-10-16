# Notes

# Permissions and Ownership

## Key Concepts

- Every file and directory has a permissions based on the owner, group and others
- You want to make sure that the reight permissions are in place to maintain the principle of least priviledge
- The three parts of file permissions are: **read, write and execute**

## Commands

| Command | Description |
| :--- | :--- |
| `chmod` | Modify file permissions |
| `sudo` | Have root user access |
| `chown` | Change ownership of files/directories |
| `useradd` | Create a new user |
| `groupadd` | Create a new group |
| `usermod` | Add or remove users from a group/modify user groups |
| `ls -l` | List all the files/directories in long format (view permissions) |

## Examples

### Create a script

```bash
echo '#!/bin/bash\necho "Hello DevOps"' > hello.sh
```

### Make it executable

```bash
chmod +x hello.sh
```

### Run it

```bash
./hello.sh
```

### Change ownership

```bash
sudo chown root:root hello.sh
```

### Understanding permissions

```bash
ls -l hello.sh
```

**Output:**

```text
-rwxr-xr-x 1 root root 32 Nov 29 10:00 hello.sh
```

**Breakdown:**

| Owner | Group | Others |
| :--- | :--- | :--- |
| `rwx` | `r-x` | `r-x` |

## What I Learned

Being able to manage permissions and ownership is a crucial skill to help you maintain the principle of least priviledge (users only having access to the least amount of authority for a given task). I learned how to create/delete users and groups. How to read the permissions of a file/directory and how to change those permissions and ownerships.

## Your Notes

- File permissions can be changed using numbers aswell as words. **4** is for read (`r`), **2** is for write (`w`), **1** is for execute (`x`).

- When checking the file/directory permissions and ownership they are broken into 4 parts:
  1. 1st part tells you if it is a file (`-`), a directory (`d`), or a link (`l`).
  2. 2nd part takes up 3 characters and represents the permissions for the owner.
  3. 3rd part takes up another 3 characters and represents the permissions for the group.
  4. 4th part takes up the final 3 characters and represents the permissions of other.

- Most of these permissions need sudo access