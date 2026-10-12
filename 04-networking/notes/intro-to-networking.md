# Notes


# Intro to Networking

## Key Concepts

- Computer networks
- LAN and WAN
- Switches, Routers and Firewall
- IP and Mac adresses
- Ports and Protocols: TCP, UDP

## Commands

`command` - what it does

## Examples

(code examples)

## What I Learned



## Your Notes
A computer network is a group of connected devices over a network which can share information and resources with eachother. There are two types of networks: LAN and WAN

`LAN` stands for Local Area Network and this is a computer network which covers a very small geographic area, for example your househould devices are part of a LAN. 

`WAN` stands for Wide Area Network and this is a computer network which covers a large geographical area, for example the internet. WANs are used to connect multiple LANs, enabling communication and data transfers over long distances.

Networking in DevOps:
- Server Interaction: enables communication between servers and applications
- Deployment: critical for launching and updating applications
- Management: crucial in monitoring and managing infrastructure
- Optimisation: enhance troubleshooting, performance and scalability

Key networing components:
- Switches
- Routers
- Firewalls

A switch is like a manager for your local network. It connects multiple devices within the same network. The switch makes sure that data flows smoothly between devices on a network, preventig congestion and ensuring efficient communication. Switches are crucial for two things mainly - connecting devices within the same network and managing data flow within a LAN. 

Routers are like traffic cops for you network. It's main job is to direct traffic between different networks. For example directing traffic from your home to the internet. It ensures that data gets to the right place. Routers are crucial for two things, directing traffic between networks and connecting different networks. 

A firewall acts like a security guard for your network. It monitors incoming and outgoing network traffic based on predetermined security rules. They are vital for two things, protecting a network from unauthorised access and monitoring and controling incoming and outgoing network traffic.

Switches, routers and firewalls form the backbone of any network.

An `IP address` is a unique identifier for a device on a network. It allows devices to locate and communicate with eachother. There are two types of IP addresses: v4 and v6. IPv4 is the most common and look something like - `192.168.0.5`. They are a 32 bit address which means they consist of 4 8 bit sections. Due to the rapid growth of the internet and devices, in addition to the fact that IP addresses are unique, IPv4 addresses are becoming scarce. This is why IPv6 was introduced, to be able to represent many more devices.

IPv6 addresses are 128bits longs and are separated by colons. They look like this - `2001:0db8:85a3:0000:0000:8a2e:0370:7334`. Another notable difference is that IPv6 addresses are hexadecimals. IPv6 also includes enhancements like simplified addresss assignment and improved security features.


A `MAC address` is a unique identifier assigned to network interfaces. Each device on a network has its own unique MAC address. A MAC address is hardcoded directly into a device's Network Interface Controller (NIC) by the manufacturer. They look like this - `00:1A:2B:3C:4D:5E`. They are a 48 bit long address and in a hexadecimal format. The function of a MAC address is to operate at the data link layer of the OSI model. The data link layer is responsible for node to node transfer. This means that they help facilitate device identification within a local network. It is essential for network communication and security. 

`Ports` are logical endpoints for communication. When your computer wants to send or recieve data, it uses these ports to make sure data goes to the right place. `Protocols` are rules governing data transmission. They define how data is formatted and transmitted across a network. Common protocols include: HTTP, HTTPS, ICMP, SMTP. Ports and protocols are important because without them our network communication would be a mess. Ports ensure that data gets to the right application on your device. While protocols ensure that the data is understandable and properly formatted, they are essential for smooth and efficient communication. 

`TCP` (Transmission Control Protocol) ensures that data sent from one device reaches another device accurately and in the correct order. Key characteristics of TCP include: connection-orientted (before any data is sent a connection is established between the two devices), requires a handshake (SYN, ACK, SYN ACK), and finally realiable data transfer (ACK messeages). Some of the functions of TCP includes: ensuring data is delivered in order, error checking and flow control, and any bidirectional communication. 

`UDP` (User Datagram Protocol) is used to send and recieve data. Unlike TCP, UDP is connectionless. Characteristics include: simple protocol to send and recieve data, prior communication not required, connectionless, and fast but less reliable. Common functions of UDP include: suitable for real-time applications (e.g. video streaming), DNS related uses, VPNs. 