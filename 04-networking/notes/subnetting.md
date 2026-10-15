# Notes

# Subnetting

## Key Concepts

- Subnetting and CIDR
- Binary
- Calculating subnets
- NAT (Network Address Translation)

## What I Learned

I learned what a subnet is and why its useful to have them. I also leanred that a CIDR is a method for allocating IP addresses and packets and how to understand CIDR notation. This lead me to also learn about the binary number system and how iP addresses use it, including how to convert between binary and denary. I also learned what a NAT is, how it works and why they are important.

## Your Notes

Subnetting is dividing a network into smaller networks. This imporves network management and efficiency. 

CIDR is a method for allocating IP addresses and routing IP packets. The format is `IP_address/prefix_length`.
Example: `192.168.1.0/24`

The first part is the IP address/network address and the /24 indicates the first 24 bits are the network part of the address.
The remaining bits are for the host address. 

Binary is a base 2 number system and uses only 1s and 0s. A bianry address is made up of 4 8 bit binary numbers. 

A subnet mask is used to divide an IP address into a network and host portions. It helps routers determine which part of an IP address and which part is the host address. 

There are some reserved addresses. When the host address has all its bits set to 0 this is known as the Network address, it identifies the subnet itself. When all the host address' bits are set to 1, this is known as the broadcast address. It is used to send data to all devices on that subnet simultaneously.

**Formulas:**
- Usable Host Addresses per subnet: 2^h - 2, where h = hosting bits remiaining
- Host bits: h = 32 - CIDR prefix length

A NAT translates private IP addresses to a public IP address. Facilitates communication between internal network and the internet. Without NAT each of your devices would need its own public IP address to access the internet which is not practical given the limited number of public IP addresses. 


**NAT Process:**
- You have internal devices which use private IP addresses. 
- Your router translates private IP to public IP
- Faciliates communication with external networks


**Types of NAT:**
- Static NAT: maps a single private IP address to a single public IP address
- Dynamic NAT: maps a private IP address to one of many public IP addresses from a pool 
- PAT (Port Address Translation): known as NAT overload and is super efficient because it allows multiple devices on a local network to be mapped to a single public iP address but with different port numbers. 