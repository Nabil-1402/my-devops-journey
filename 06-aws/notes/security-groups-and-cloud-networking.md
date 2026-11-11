# Notes

# Security Groups and Cloud Networking

## Key Concepts

- Security groups
- Stateful filtering
- Ports and protocols
- Security group references
- Private and public IPv4 addresses
- Network Address Translation (NAT)
- Internet gateways
- Elastic IP addresses

## What I Learned

In this module I learned the importance of security groups, how to use them, aswell as networking in the cloud. Additionally I built on top of my networking knowledge from the networking module and explored how private IP addresses use internet gateways to translate their IP into a public IP (via NAT) to communicate with external websites and services. I also learned about elastic IPs and their uses. Furthermore I learned about inbound and outbound rules and how to edit them for your EC2 isntance.

## Your Notes

### Security Groups

Security groups are a fundamental part of network security in AWS. They control how traffic is allowed into and out of EC2 instances and act like virtual firewalls.

Security groups contain **allow rules only**. Their rules can reference IP addresses or other security groups.

Security groups are **stateful**, meaning that if inbound traffic is allowed, the corresponding response traffic is automatically allowed outbound, and vice versa.

Security groups control which ports can be accessed on your instances.

They regulate:

- Access to ports.
- Authorised IP ranges — IPv4 and IPv6.
- Inbound network traffic — traffic coming into the instance.
- Outbound network traffic — traffic leaving the instance.

**Ports to know:**

| Port | Protocol | Purpose |
|---|---|---|
| 22 | SSH — Secure Shell | Log into a Linux instance. |
| 21 | FTP — File Transfer Protocol | Establish an FTP control connection; file transfers also use additional ports. |
| 22 | SFTP — SSH File Transfer Protocol | Transfer files securely using SSH. |
| 80 | HTTP | Access websites without TLS encryption. |
| 443 | HTTPS | Access websites using TLS encryption. |
| 53 | DNS — Domain Name System | Perform DNS queries and resolve domain names. |
| 3389 | RDP — Remote Desktop Protocol | Log into a Windows instance remotely. |

It is good practice to keep your security groups as restrictive as possible. Only open the ports you need and limit access to trusted IP addresses.

**Security Groups — Good to Know:**

- Can be attached to multiple instances.
- Belong to a particular Region and VPC.
- Filter traffic outside the EC2 instance — blocked traffic does not reach the instance’s operating system.
- A separate security group for SSH access can make administration easier.
- If your application times out, check security groups alongside routing, network ACLs and host firewall settings.
- If your application returns a **“connection refused”** error, the application may not be running or listening on the requested port.
- Newly created security groups block all inbound traffic by default.
- Newly created security groups allow all outbound traffic by default, unless their rules are changed.

You can reference other security groups instead of individual IP addresses. This makes rules easier to manage because instance IP addresses can change, reducing the need for manual updates.

This is useful in dynamic environments and for microservices. Referencing another security group does not copy its rules.

### IPv4

At **Layer 3 — the Network Layer — of the OSI model**, routers direct traffic between different networks.

Private IP addresses are not routable over the public internet, so devices cannot use these addresses directly to communicate with public websites or services. In a typical home or office network, a router translates private IP addresses into a public IP address. This process is called **Network Address Translation (NAT)**.

In AWS, an internet gateway provides internet connectivity for a VPC and maps an instance’s public IPv4 address to its private IPv4 address. Instances in private subnets can use a public NAT gateway for outbound internet access without having their own public IPv4 addresses. Appropriate routes and security rules are also required.

Private IP addresses can be reused across separate networks, while public IP addresses must be globally unique while in use. A public IP address can indicate an approximate geographical location, although this is not always accurate.

Only specific ranges are reserved for private IPv4 addresses:

- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

When you **stop and start** an EC2 instance, its automatically assigned public IPv4 address normally changes. Rebooting the instance normally preserves it. A changing address can be an issue when you need a fixed public IP.

When you need a fixed public IPv4 address, you can use an **Elastic IP address**. It remains allocated to your AWS account until you release it and can be associated with only one resource at a time.

Elastic IP addresses are useful when external services need a static IP address to reach your instance, such as when a partner must add your address to an allowlist.

An Elastic IP address can also help with recovery by allowing you to rapidly reassociate the address with another instance or network interface in your account.

Elastic IP allocations are subject to quotas, and you can request a quota increase.

Use Elastic IP addresses when a static public IPv4 address is required. Depending on your architecture, alternatives include:

- Using an automatically assigned public IP address with a DNS name, updating the DNS record when the address changes.
- Using a load balancer as the application’s entry point so clients do not depend on individual instances’ public IP addresses.