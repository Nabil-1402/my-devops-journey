# Notes

# OSI Model

## Key Concepts

- The seven OSI layers
- The TCP/IP model
- Encapsulation and decapsulation
- Ports and protocols
- How an HTTPS request travels through a network

## What I Learned

I learned how the OSI model separates network communication into seven layers, each with a specific responsibility.

I also revisited ports and protocols, compared TCP and UDP, and explored how data travels through the network stack when an application sends a request.

## Your Notes

### What Is the OSI Model?

The **Open Systems Interconnection (OSI) model** is a conceptual framework for understanding how devices communicate over a network.

It divides communication into **seven layers**, from physical signals to application-level services.

### Why Use a Layered Model?

- **Clear responsibilities:** Each layer handles a particular part of communication.
- **Interoperability:** Standard interfaces and protocols help different systems work together.
- **Simpler development:** Applications can use network services without managing physical transmission.
- **Easier troubleshooting:** Problems can be investigated by layer.
- **Independent improvements:** A layer's implementation can change while preserving its interfaces.

> The OSI model is a reference model. Real-world protocols do not always fit neatly into a single layer, especially Layers 5–7.

### The Seven Layers

| Layer | Name | Main Responsibility | Examples |
| :--- | :--- | :--- | :--- |
| **7** | Application | Provides network services used by applications. | HTTP, DNS, SMTP, SSH |
| **6** | Presentation | Handles data representation, encoding, compression and encryption concepts. | Character encoding, JSON representation, JPEG |
| **5** | Session | Establishes, manages and ends communication sessions. | Dialogue control, checkpoints and session coordination |
| **4** | Transport | Provides communication between application endpoints. | TCP, UDP, ports |
| **3** | Network | Handles logical addressing and routing between networks. | IP, ICMP, routers |
| **2** | Data Link | Transfers frames across a local link. | MAC addresses, Ethernet frames, switches |
| **1** | Physical | Transmits bits as signals through a medium. | Copper, fibre, radio, hubs, repeaters |

> **Numbering matters:** Layer 1 is Physical; Layer 7 is Application.

### Layer 7 — Application

The **Application layer** provides network protocols and services used by software.

Examples include:

- **HTTP:** Web requests and responses
- **DNS:** Name resolution and other DNS lookups
- **SMTP:** Email transfer
- **SSH:** Secure remote access
- **FTP:** File transfer

> The application itself, such as a browser, uses Application-layer protocols to communicate.

### Layer 6 — Presentation

The **Presentation layer** concerns how data is represented so the receiving application can interpret it.

Its responsibilities can include:

- **Encoding:** Representing text using formats such as UTF-8
- **Serialisation:** Converting structured data into a transferable representation
- **Compression:** Reducing data size
- **Encryption and decryption:** Protecting data confidentiality

Examples of data formats include **JSON, JPEG and MPEG**.

> TLS provides encryption in real networks, but its position does not map perfectly to a single OSI layer. SSH, FTP and IMAP are normally classified as Application-layer protocols.

### Layer 5 — Session

The **Session layer** concerns establishing, coordinating and ending dialogues between applications.

Its responsibilities can include:

- Starting and ending sessions
- Coordinating ongoing communication
- Managing checkpoints that allow an exchange to resume

In modern internet applications, many of these functions are handled by application protocols and libraries.

> A TCP connection belongs to Layer 4. A website login session is usually managed at the application level. Neither maps directly to the OSI Session layer.

### Layer 4 — Transport

The **Transport layer** provides communication between application endpoints, using **ports** to distinguish them.

The two main protocols are **TCP** and **UDP**.

| Feature | TCP | UDP |
| :--- | :--- | :--- |
| **Connection setup** | Establishes a connection using a handshake. | No transport connection setup. |
| **Delivery** | Uses acknowledgements and retransmissions. | No built-in delivery guarantee. |
| **Ordering** | Presents data to the application in order. | No built-in ordering guarantee. |
| **Data format** | A stream of bytes. | Individual datagrams. |
| **Typical uses** | SSH, email, HTTP/1.1 and HTTP/2 | DNS queries, real-time media, QUIC |

The TCP three-way handshake is:

1. **SYN**
2. **SYN-ACK**
3. **ACK**

> TCP supports reliable delivery, but connections can still fail. UDP has lower transport overhead; it is not automatically faster in every situation.

### Layer 3 — Network

The **Network layer** handles logical addressing and forwarding packets between networks.

Its responsibilities include:

- Adding source and destination **IP addresses**
- Routing packets towards their destination
- Selecting a next hop using a routing table

Examples include:

- **IPv4 and IPv6**
- **ICMP**
- **Routers**

> Routers select routes according to their routing tables and policies. The chosen route is not necessarily the geographically shortest or fastest path.

### Layer 2 — Data Link

The **Data Link layer** transfers data across a local network link using **frames**.

Its responsibilities include:

- Encapsulating network-layer packets into frames
- Using link-layer addresses, such as **MAC addresses**
- Controlling access to the transmission medium
- Detecting frame corruption

Examples include:

- **Ethernet framing**
- **Wi-Fi framing**
- **PPP**
- **Layer 2 switches and bridges**

> Error detection does not always mean error correction or retransmission. Ethernet can detect and discard corrupted frames; higher layers may handle recovery.

### Layer 1 — Physical

The **Physical layer** transmits bits as signals through a physical medium.

Examples include:

- **Electrical signals** over copper
- **Light pulses** through fibre
- **Radio signals** over wireless links
- **Connectors, hubs and repeaters**

This layer defines characteristics such as signalling, timing and transmission rates. It does not interpret IP or MAC addresses.

> Ethernet and Wi-Fi include both Physical-layer and Data Link-layer specifications. A network interface card therefore performs functions across more than one layer.

### Remembering the Layers

From **Layer 7 down to Layer 1**:

**All People Seem To Need Data Processing**

| Word | Layer |
| :--- | :--- |
| **All** | Application |
| **People** | Presentation |
| **Seem** | Session |
| **To** | Transport |
| **Need** | Network |
| **Data** | Data Link |
| **Processing** | Physical |

### Encapsulation and Decapsulation

As data moves down the sender's network stack, each layer adds the information needed for delivery. This is called **encapsulation**.

| Stage | Common Name |
| :--- | :--- |
| **Application data** | Data or message |
| **TCP transport** | Segment |
| **UDP transport** | Datagram |
| **IP network** | Packet |
| **Data Link** | Frame |
| **Physical** | Bits transmitted as signals |

At the receiver, the stack interprets and removes the relevant headers as data moves upwards. This is called **decapsulation**.

> **Memory aid:** Data → Segment/Datagram → Packet → Frame → Signals.

### The TCP/IP Model

The **TCP/IP model** describes the internet protocol suite using four layers.

| TCP/IP Layer | Approximate OSI Equivalent | Examples |
| :--- | :--- | :--- |
| **Application** | Layers 7, 6 and 5 | HTTP, DNS, SMTP, application data formats |
| **Transport** | Layer 4 | TCP, UDP |
| **Internet** | Layer 3 | IP, ICMP |
| **Network Access / Link** | Layers 2 and 1 | Ethernet, Wi-Fi, physical transmission |

> The mapping is approximate. Internet applications commonly combine responsibilities that the OSI model separates.

### Example: Sending an HTTPS POST Request

This example assumes **HTTPS over TCP**, such as HTTP/1.1 or HTTP/2, with a new connection.

1. **Resolve the server's address**
   - The client obtains an IP address using local configuration, cached information or DNS.

2. **Establish a TCP connection**
   - The client connects to the server, typically on port **443**.
   - TCP uses the **SYN → SYN-ACK → ACK** handshake.

3. **Establish TLS**
   - The client and server negotiate a secure connection.
   - The client normally validates the server's certificate.

4. **Prepare the HTTP request**
   - The application serialises its data, for example as JSON.
   - It creates a POST request containing headers and the request body.

5. **Encrypt and transport the request**
   - TLS encrypts the HTTP data.
   - TCP carries the encrypted bytes, dividing the stream into segments as needed.

6. **Add IP addressing**
   - IP packets carry the transport data with source and destination IP addresses.

7. **Send over the local link**
   - Packets are carried inside frames.
   - On Ethernet or Wi-Fi, the destination MAC normally belongs to the next hop, such as the default gateway.

8. **Transmit physical signals**
   - The interface sends bits using electrical, radio or optical signals.

9. **Process the request at the destination**
   - The server's network stack processes the incoming data.
   - TLS decrypts it, and the application handles the HTTP request.

> These are conceptual stages, not a separate operation for every OSI layer. Existing connections can be reused, and HTTP/3 uses QUIC over UDP instead of TCP.

### Ports and Protocols

**Ports** identify transport endpoints, helping the operating system deliver traffic to the appropriate application.

**Protocols** define the rules and message formats used for communication.

| Item | Example |
| :--- | :--- |
| **IP address** | Identifies the destination interface, such as `192.168.1.10`. |
| **Port** | Identifies a transport endpoint, such as TCP port `443`. |
| **Protocol** | Defines communication rules, such as HTTP, TCP or IP. |

> **Remember:** IP identifies where traffic is going; ports help identify the application endpoint; protocols define how communication works.