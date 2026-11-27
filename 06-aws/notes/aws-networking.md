# Notes

# AWS Networking

## Key Concepts

- Point 1
- Point 2

## Commands

`command` - what it does

## Examples

(code examples)

## What I Learned



## Your Notes

### Understanding CIDR - IPv4

CIDR stands for Classless Inter Domain Routing - a method for allocating IP addresses. They help us define IP ranges and they have a lot of flexibility. They are used in security groups rules and AWS networking in general

CIDR has two main components:
- Base IP: this is an IP contained in the range and is usually the start of teh range e.g. 10.0.0.0
- Subnet Mask: this defines how many bits can change in the IP range. For example a `/0` means that all bits can change, `/32` means only one specific IP. The smaller the number after the slash the larger the range of IPs available

### Public vs Private IP (IPv4)
Private IPs can only allow certain values:
- 10.0.0.0 - 10.255.255.255 (10.0.0.0/8) for big networks
- 172.160.0.0 - 172.31.255.255 (172.31.0.0/12) for AWS default VPC
- 192.168.0.0 - 192.168.255.255 (192.168.0.0/16) for home networks

Private IPs cannot be used on the public internet. They are meant only for internal networks. All other IP addresses not in the above ranges are public. 

Public IP addresses can be accessed from anywhere on the internet. 

### Default VPC Walkthrough
All new AWS accounts have a default VPC. If you launch an EC2 instance without specifiying a VPC or subnet, it will be placed in the default VPC by default. The default VPC comes with the internet connectivity by default, which is why any instance that you launch into it can access the internet right away. The EC2 inside the default VPC will also automatically be assigned a public IPv4 address. 

### VPC - Subnet (IPv4)
Subnets are the small networks within your VPC. Each VPC is divided into multiple subnets, which allow you to segment your resources across different AZs. This gives you better redundency and high availabilty. 

Subnets can be public or private depending on whether they have access to the internet. 

AWS reserves 5 IP addresses within each subnet and theyre not available for use by your resources. They are:
- 10.0.0.0: network address
- 10.0.0.1: reserved by AWS for the VPC router
- 10.0.0.2: reserved by AWS for mapping to Amazon prodivded DNS (IP address of DNS server)
- 10.0.0.3: reserved by AWS for future use
- 10.0.0.255: network broadcast address. AWS does not support broadcast in a VPC, therefore the address is reserved.

### Internet Gateway (IGW)
Allows resources inside a VPC to connect to the internet. It scales horizontally, which means it can handle an increasing amount of traffic easily and it is also highly available and redundant. That means there is no single point in failure. 

When you create a VPC an IGW is not created by default. You have to create it separately and then attach it to your VPC. Only one VPC can be attached to an IGW at a time. Just by creating and attaching an IGW to your VPC does not mean you have access to the internet. You need to edit your route tables of your subnets. 


###  Bastion Hosts
A Bastion Host is like a bridge to your private instances. We can use a Bastion Host to SSH into private instances. The bastion is created in the public subnet nd once you are connected to it you can then access the private subnet where each instance is located. It is important to note that security groups on the bastion host needs to be configured to allow inbound SSH from a certain restricted CIDR, which could be the the public IP range of your office or corporation. This adds an extra layer of security in environments where security is critical.

###  NAT Gateway
Stands for Network Address Translation. A NAT gateway is a managed service provided by AWS which allws your instance in a private subnet to connect to the internet, but it blocks any incoming traffic from the internet. This is important for security and ensuring that your private resources stay protected while still having internet access when needed. 

AWS handles all the heavy lifting, giving you higher bandwidth, higher availability and no administration. You pay per hour for usage and bandwidth. They are also AZ specific and they use an elastic IP. If you want redundency across zones you need to create multiple NAT gateways to put one in each zone. It cant be used by EC2 in the same subnet (only from other subnets). It also requires an IGW (internet gateway) to connect to the outside world (private IP -> NAT Gateway -> Internet Gateway). No security groups to manage/ required.

#### Availability
The NATGW is highly available but only in one AZ. However, if you have resources in multiple AZs but they are sharing just one NATGW there is a risk. The risk is if that NATGW goes down then all the resources in other AZs will lose access to the internet. The solution for this is depending on how critical your applcation is and the level of fault tolerance you need, you should create NATGWs in at least 2 AZs. This way you can spread your risk. 

### NAT Gateway vs. NAT Instance

| Feature | NAT Gateway | NAT Instance |
|---|---|---|
| **Availability** | Highly available within an Availability Zone (AZ). Create additional gateways in other AZs for redundancy. | Requires a script to manage failover between instances. |
| **Bandwidth** | Up to 100 Gbps. | Depends on the EC2 instance type. |
| **Maintenance** | Fully managed by AWS. | Managed by you (software updates, OS patches, etc.). |
| **Cost** | Charged per hour and amount of data processed. | Charged per hour based on EC2 instance type, size and network costs. |
| **Public IPv4** | ✅ | ✅ |
| **Private IPv4** | ✅ | ✅ |
| **Security Groups** | ❌ | ✅ |
| **Use as Bastion Host** | ❌ | ✅ |

### Networking Access Control List (NACL)
These are like a big filter at the subnet level that checks whether traffic should be allowed or denied. They do this based on a set of rules you define. 

Key characteristics:
- You have one NACL per subnet 
- These are stateless (do not automatically return traffic, have to define both inbound and outbound rules explicitly)

NACL rules:
- Rules have a number (1-32766), higher precidence with a lower number
- First rule match will drive the decision
- The last rule in a NACL is an asterik (*) and denies a request in the case of no rules matching
- AWS recommends addding rules by increment of 100

Newly created NACLs will deny everything and they are a great way of blocking specific IP addresses at a subnet level.

### Security Groups & NACLs
SGs operate at the instance level, they control traffic to and from your instances. NACLs operate at the subnet level, they control the traffic at the boundary of the subnet affecting all resources inside the subnet.

#### Incoming request
SGs are stateful meaning if you allow an incoming request, the response request is automatically allowed back. NACLs are stateless which means that if you allow traffic in one direction it is not automatically allowed the other way unless specified. 

1) The NACL filters any traffic coming into the subnet based on the inbound rules. If traffic is permitted into the subnet you perceed to the next step, otherwise traffic is blocked here.
2) Then you have the security inbound rules. After traffic passes through the NACL, it hits the SG of the instance. If the SG allows traffic then it is accpeted if not it is blocked. Also since it is stateful, traffic allowed in is also allowed out. 
3) Then you finally have the NACL outbound rules. Since NACLs are stateless, even though the SG might allow traffic the NACLs outbound rule has to allow it to say yes it can go out. So you need to have outbound rules confgured on the NACL.

#### Outgoing request
1) When an instance inside the VPC wants to send traffic out, the SG outbound rules come first. If it allows the traffic, the data leaves teh instance and moves forward to the NACL. 
2) Since NACLs are stateless they will only allow outbound rules if they are explicitly configured to allow it. If the NACL allows the traffic then the data can leave the subnet.
3) Then when traffic is coming in, if the NACL inbound rules allows the traffic then it can enter the subnet, which is then passed to the SG which is stateful which will then allow the traffic into the instance. 

### VPC Peering
This is a way to privately connect to VPCs using AWS' internet network. When you set up a VPC peering connection, the two VPCs behave as if they are part of the same network, alolowing them to communicate with each other without having to use the internet. 

key features:
- They have a private connection
- They cannot have any overlapping CIDRs 
- Non transitive
- After creating the peering connection, you need to update the route tables in each VPCs subnet to ensure that traffic can flow between the two VPCs

#### Good To Knows
You can create a VPC peering connection between VPCs in different AWS accounts/regions. This is especially useful when your infrastructure for different teams and departments that need to communicate securely whilst keeping things separate.

You can reference SGs in peered VPCs as long as both VPCs are in teh same region. 

#### VPC Endpoints (AWS PrivateLink)
By default all AWS resources are publicly exposed, meaning that they have a public URL that your resources need to access by the internet. If you wanted to keep thing sprivate structly for security reasons here you would use VPC Endpoints.

They are powered by AWS PrivateLink. They allow you to connect to AWS services like S3 using a private network instead of going over the internet. This keeps your data traffic securely inside the AWS netwrok. 

You would use this because it is a big security advantage, as you are not exposing the VPC to the internet just to acces AWS services. The set up is also redundent and scales horizontally, meaning it is super reliable and can handle an increasing load without you having to worry. There is also no need for having an IGW or NATGW. 

In case of issues:
- DNS setting resolution in your VPC
- Check route tables

