# Notes

# Networking

## Key Concepts

- Networking commands in linux are vital for DevOps engineers
- These commands will help in future learning in modules such as docker and kubernetes
- These are very important to learn for troubleshooting and security

## Commands

`ip` - Inspect IP addresses, interfaces and routes

`ifconfig`- Configure network interface parameters, assign an address to a network interface.

`ping` - Test wether a host responds to ICMP

`curl` - Make requests to an application, especially useful for HTTPS APIs and websites

`dig` - Investigae DNS by querying

`getent` - Checks resultions through your system's configured sources

`ssh` - Access serves remotely

`openssl` - Open a TLS connection 

`scp` - Copy files securely between machines

`nmap` - Discover reachable ports

`nc` / `netcat` - Test ports and send raw data

`ss` - Inspect sockets and listening ports

`tracepaths` / `traceroute` - Investigate the path towards a destination

`lsof` - List open files / identify processes using sockets


## Examples

nc -lvp 9999

ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme

nmap -sV localhost -p 31000-32000

openssl s_client -connect localhost:31790 -quiet

ip addr

## What I Learned

Network commands in linux are very important as they assist in configuration, troubleshooting and security. Using commands like `dig`, `curl` and `ping` are very helpful when debugging or testing applications and DNSs on a network. `ifconfig` and `ip` are also useful as they give you information about your devices own network configurations and this can be useful when trying to set up a connnection or when trying to communicate with other devices.


## Your Notes

Devices on a network need an identifier and this can be an IP address, this is to help with routing packages on a network.

Two types of IP: IPv4 (older) and IPv6 (newer)

/etc/resolv.conf this contains DNS configuration data

/etc/host is a file that is consulted before the DNS is consulted

Networking commands are used for testing, troubleshooting and configuring




