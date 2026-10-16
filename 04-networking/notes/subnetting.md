# Notes

# Subnetting

## Key Concepts

- Subnetting and CIDR
- Binary
- Calculating subnets
- NAT — Network Address Translation

## What I Learned

I learned what subnets are and how they help organise networks. I also explored CIDR notation, how it represents network and host portions of an address, and how to calculate usable host addresses.

This included understanding binary and converting between binary and decimal. Finally, I learned how NAT works and how it helps conserve public IPv4 addresses.

## Your Notes

### What Is Subnetting?

**Subnetting** divides a network into smaller networks called **subnets**. This helps improve network organisation, management and address allocation.

### CIDR Notation

**CIDR — Classless Inter-Domain Routing** is a method for allocating IP addresses and routing IP packets.

Its notation is `IP_address/prefix_length`.

For example: `192.168.1.0/24`

- **Network portion:** The first 24 bits.
- **Host portion:** The remaining 8 bits.

### Binary and IPv4 Addresses

**Binary** is a base-2 number system that uses only **0s and 1s**.

An IPv4 address contains **32 bits**, divided into four **8-bit octets**.

For example:

| Format | Address |
| :--- | :--- |
| **Decimal** | `192.168.1.0` |
| **Binary** | `11000000.10101000.00000001.00000000` |

### Subnet Masks

A **subnet mask** identifies which bits of an IPv4 address represent the network and which represent the host.

- **1s** identify the network portion.
- **0s** identify the host portion.

For example, `/24` corresponds to the subnet mask `255.255.255.0`.

### Reserved Addresses

In a typical IPv4 subnet, two addresses are reserved:

| Address | Host Bits | Purpose |
| :--- | :--- | :--- |
| **Network address** | All `0`s | Identifies the subnet itself. |
| **Broadcast address** | All `1`s | Addresses all hosts on the subnet. |

### Subnetting Formulas

- **Host bits:** `h = 32 - CIDR prefix length`
- **Total addresses:** `2^h`
- **Usable host addresses:** `2^h - 2`

> The usable-host formula applies to typical IPv4 subnets. `/31` point-to-point networks and `/32` host routes are exceptions.

### NAT — Network Address Translation

**NAT** translates IP addresses between networks. It is commonly used to let devices with private IPv4 addresses communicate with the internet using public IPv4 addresses.

With **PAT**, multiple devices can share one public IPv4 address, helping conserve the limited public IPv4 address space.

### NAT Process

1. An internal device sends traffic using its **private IP address**.
2. The router translates the source address to a **public IP address**, and may also translate the source port.
3. The router keeps a mapping so returning traffic can be translated and forwarded to the correct internal device.

### Types of NAT

| Type | Description |
| :--- | :--- |
| **Static NAT** | Uses a fixed mapping between one private IP address and one public IP address. |
| **Dynamic NAT** | Maps a private IP address to an available public IP address from a pool. |
| **PAT — Port Address Translation** | Allows multiple devices to share one public IP address by tracking connections using port numbers. Also called **NAT overload**. |