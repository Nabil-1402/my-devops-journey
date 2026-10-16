# Notes


# Intro to Networking

## Key Concepts

- Computer networks
- LANs and WANs
- Switches, routers and firewalls
- IP and MAC addresses
- Ports and protocols
- TCP and UDP
- Why networking matters in DevOps

## What I Learned

I learned how devices communicate within local networks and across the internet, and how switches, routers and firewalls support that communication.

I also explored the differences between IP and MAC addresses, how ports identify application endpoints, and when TCP or UDP is appropriate.

## Your Notes

### What Is a Computer Network?

A **computer network** is a group of connected devices that can exchange information and share resources.

Examples include sharing files, accessing websites and connecting to a network printer.

Two common categories are **LANs** and **WANs**.

### LAN vs WAN

| Feature | LAN | WAN |
| :--- | :--- | :--- |
| **Full name** | Local Area Network | Wide Area Network |
| **Coverage** | A limited area, such as a home, office or building. | A large geographical area, connecting networks across locations. |
| **Purpose** | Connects nearby devices so they can communicate and share resources. | Connects networks over longer distances. |
| **Example** | Your home network. | A company network connecting offices in different countries. |

> **Remember:** A LAN connects devices locally; a WAN connects networks over distance. The internet is a global network of interconnected networks.

### Why Networking Matters in DevOps

- **Server communication:** Enables applications, servers and services to communicate.
- **Deployment:** Supports delivering applications and updates to infrastructure.
- **Monitoring:** Allows monitoring tools to collect logs, metrics and health information.
- **Troubleshooting:** Helps identify DNS problems, blocked ports and connection failures.
- **Performance and scalability:** Supports load balancing and efficient traffic routing.
- **Security:** Helps control access to applications and infrastructure.

### Key Networking Components

| Component | Main Role | How It Works |
| :--- | :--- | :--- |
| **Switch** | Connects devices within a LAN. | A typical Layer 2 switch forwards Ethernet frames using MAC addresses. |
| **Router** | Connects different IP networks. | Forwards packets using destination IP addresses and its routing table. |
| **Firewall** | Controls which traffic is permitted. | Allows or blocks traffic according to security rules. |

#### Switches

A **switch** connects devices within a local network.

It learns which MAC addresses are reachable through its ports and uses this information to forward frames towards the correct destination.

If the destination MAC address is unknown, it typically floods the frame within the relevant VLAN.

#### Routers

A **router** forwards traffic between different networks.

For example, your home router connects your local network to your internet provider's network. It uses a **routing table** to choose where to send packets next.

> When contacting a device outside your local network, your computer normally sends traffic to its **default gateway**.

#### Firewalls

A **firewall** filters network traffic according to configured rules.

Rules can consider information such as:

- Source and destination IP addresses
- Source and destination ports
- Network protocols
- Connection state

Firewalls can run on individual devices or protect networks at their boundaries.

> **Memory aid:** Switch = local delivery. Router = between networks. Firewall = access control.

### IP Addresses

An **IP address** is a logical address assigned to a network interface. It allows packets to be addressed and routed between networks.

An interface can have multiple IP addresses, and addresses can change over time.

The two IP versions are **IPv4** and **IPv6**.

#### IPv4

IPv4 addresses are **32 bits** long, written as four decimal numbers separated by dots.

```text
192.168.0.5
```

- Each section is **8 bits**, also called an octet.
- Each octet ranges from **0 to 255**.
- IPv4 provides approximately **4.3 billion** possible addresses.
- Private addresses can be reused across separate networks.
- NAT commonly allows multiple private devices to share a public IPv4 address.

#### IPv6

IPv6 addresses are **128 bits** long, written in hexadecimal with groups separated by colons.

```text
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

This can be shortened to:

```text
2001:db8:85a3::8a2e:370:7334
```

- Leading zeros within groups can be omitted.
- One consecutive sequence of all-zero groups can be replaced with `::`.
- The much larger address space addresses IPv4 scarcity.
- IPv6 supports automatic address configuration, including SLAAC.

> IPv6 is not automatically more secure than IPv4. Both require appropriate security configuration.

### MAC Addresses

A **MAC address** identifies a network interface at the **Data Link layer — Layer 2** of the OSI model.

Ethernet and Wi-Fi MAC addresses are typically **48 bits**, written as six hexadecimal pairs.

```text
00:1A:2B:3C:4D:5E
```

Manufacturers commonly assign MAC addresses, but software can override them. Devices may also use randomised MAC addresses for privacy.

MAC addresses support frame delivery on the local network. Routers replace the link-layer addressing as they forward traffic between network links.

### IP vs MAC Addresses

| Feature | IP Address | MAC Address |
| :--- | :--- | :--- |
| **Purpose** | Addresses interfaces for communication within and between IP networks. | Identifies interfaces for local link-layer delivery. |
| **OSI layer** | Layer 3 — Network | Layer 2 — Data Link |
| **Example** | `192.168.0.5` | `00:1A:2B:3C:4D:5E` |
| **Assignment** | Configured manually or automatically. | Commonly manufacturer-assigned, but can be overridden or randomised. |

> **Example:** When contacting a remote website, the destination IP identifies the remote server, while the destination MAC on your local link normally identifies your gateway.

### Ports and Protocols

#### Ports

**Ports** are numbered identifiers used by transport protocols such as TCP and UDP to distinguish communication endpoints.

Port numbers range from **0 to 65535**.

A server commonly listens on a known port, while a client usually uses a temporary **ephemeral port**.

#### Protocols

**Protocols** define the rules and message formats devices use to communicate.

Examples include:

- **HTTP:** Transfers web requests and responses.
- **HTTPS:** Protects HTTP communication using encryption.
- **DNS:** Resolves names and provides other DNS records.
- **SMTP:** Transfers email.
- **ICMP:** Carries network control and diagnostic messages.

> Not every protocol uses ports. ICMP, used by `ping`, does not use TCP or UDP ports.

### Common Ports

| Service | Typical Transport | Default Port |
| :--- | :--- | :--- |
| **SSH** | TCP | 22 |
| **DNS** | UDP and TCP | 53 |
| **HTTP** | TCP | 80 |
| **HTTPS** | TCP; UDP for HTTP/3 | 443 |
| **SMTP server-to-server transfer** | TCP | 25 |

> These are defaults. Services can be configured to use other ports.

### TCP — Transmission Control Protocol

TCP provides a **reliable, ordered stream of bytes** between applications.

Its main characteristics include:

- **Connection-oriented:** Establishes a connection before normal application data transfer.
- **Ordered delivery:** Presents received data to the application in the correct order.
- **Retransmission:** Retransmits lost data.
- **Error detection:** Uses checksums to detect corruption.
- **Flow control:** Helps prevent overwhelming the receiver.
- **Congestion control:** Adjusts transmission in response to network conditions.
- **Bidirectional communication:** Supports sending and receiving over the same connection.

If delivery cannot continue, TCP eventually reports failure rather than guaranteeing that all data will always arrive.

#### TCP Three-Way Handshake

1. **SYN:** The client requests a connection.
2. **SYN-ACK:** The server acknowledges the request and sends its own synchronisation request.
3. **ACK:** The client acknowledges the server's response.

> **Memory aid:** SYN → SYN-ACK → ACK.

Common uses include SSH, email transfer and HTTP/1.1 or HTTP/2 web traffic.

### UDP — User Datagram Protocol

UDP sends individual messages called **datagrams** without establishing a transport connection first.

Its main characteristics include:

- **Connectionless:** No UDP handshake is required.
- **Low overhead:** Uses a small header and minimal transport-level processing.
- **No delivery guarantee:** Datagrams may be lost.
- **No ordering guarantee:** Datagrams may arrive out of order.
- **No built-in retransmission:** Applications decide how to handle missing data.

Common uses include:

- DNS queries
- Voice and video calls
- Online gaming
- Some VPN protocols
- QUIC, the transport used by HTTP/3

> Applications can build reliability and security on top of UDP. UDP itself does not provide them.

### TCP vs UDP

| Feature | TCP | UDP |
| :--- | :--- | :--- |
| **Connection setup** | Uses a handshake. | No transport handshake. |
| **Data format** | A stream of bytes. | Individual datagrams. |
| **Delivery** | Uses acknowledgements and retransmissions. | No built-in delivery guarantee. |
| **Ordering** | Delivers data to the application in order. | No built-in ordering guarantee. |
| **Overhead** | More connection management and tracking. | Less transport-level overhead. |
| **Typical uses** | SSH, email and many web connections. | DNS, real-time communication and QUIC. |

> **Remember:** TCP handles reliable, ordered transport. UDP leaves more decisions to the application.