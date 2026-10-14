# Notes

# OSI Model

## Key Concepts

- The 7 layers
- TCP/IP Model
- Ports and Protocols


## What I Learned

I learned what the OSI Model is and what happens at each of the 7 layers. I recaped the importance of using ports and protocols as well as the difference between TCP and UDP and when you would prefer to use one over another.

## Your Notes

The OSI model is used to understand how data travels from one device to another

We need a communication model because this provides a standard framework that simplifies the way devices and applications communicate over a network. 

Without a standard model, applications would need to understand the specifics of the underlaying network. With a communication model, applications can work idependently of the network making development and coding much simpler and more efficient. 

With a standard communication model, it is easier to upgrade and manage network gear because everything speaks the same language. This standardisation makes maintainence and upgrading smoother and less prone to issues. 

An additional benefit is that innovations can happen in each layer independently without affecting the entire system (decoupled innovation).

**Layer 1 - Application**
- The top layer is the application layer
- This is where network services are given directly to applications
- End to end user layer
- HTTP, FTP, IRC, SSH, DNS

**Layer 2 - Presentation**
- This is where data is trabslated to a readable format
- Encryption is also handled at this layer
- Syntax user layer
- SSL, SSH, IMAP, FTP, MPEG, JPEG

This is somethimes known as the Syntax layer because it ensures data being sent is in a usable or readable format. This layer also handles encryption to handle data security.


**Layer 3 - Session**
- Can manage sessions between different applications
- Synch and send to port
- API's, Sockets, Winsock

This layer is responsible for three things, establishing, managing and terminating sessions. By establishing sessions that means getting a session started and maintaining a session means keeping the session alive, ensuring that any conversation and every request can continue smoothly. Some example components of this layer are session management protocols like RPC, NetBIOS. 


**Layer 4 - Transport**
- End to end communication and data integrity is managed
- TCP, UDP

This layer is responsible providing reliable data transfer services to the lower layers. It used to ensure that data packets arrive safely and in the right sequence. The two components that allow it to do this job are TCP and UDP. TCP provides reliable, ordered and error free data. UDP is much faster but less reliable. 

**Layer 5 - Network**
- Where routing data packets are managed
- IP, ICMP, IPSec, IGMP

This layer is responsible to determine how data is sent to a recipient. Ontop of that, it manages packet forwarding, including routing through different routers. It decides the best path for data to travel across different networks, ensuring that it gets to the right place. Some of the compents of this are IP addresses and routers. In this layer data is organised into packets which are things that carry data from one device to another. The IP addresses handle where packets go to and the routers are the component that allows it to do this job. 


**Layer 6 - Data Link**
- Node to node transfer and error detection is managed
- Frames
- Ethernet, PPP, Switch, Bridge

As mentioned above, this layer is responsible for node to node data transfer. This means ensuring data packets are sent and recieved correctly between different network nodes. It is all about maintaining a reliable link between all devices. This layer puts your data packets into frames where it's actually organised. Frames are like the envelopes that carry the data and endure it gets to the right place. Some of the components that do the job here are Mac addresses, switches and bridges.


**Layer 7 - Physical**
- Physical connection between devices
- Coax, Fibre, Wireless, Hubs, Repeaters

The layer transmits raw bit streams over a physical medium. This deals with the hardware connection. Some of the components of this layer includes: cables, switches and network interface cards. There is no device addressing here meaning all data is processed by all devices. This is also the limitation.


**TCP/IP Model**
This is made of 4 layers:
1) Application Layer

    This is where network applications and their products operate like HTTP, TLS, and DNS.  

2) Transport Layer

    This layer is where end to end communication and data trasfer happen between devices. The key protocols here are TCP and UPD.

3) Internet Layer

    This layer is responsible for logical addressing and routing data across different networks. IP is the primary protocol. 

4) Network Access Layer

    This layer encompasses the data link and physical layer of the OSI model.


**Example Flow of POST Request (For Sender):**

1) Starting at application layer, the POST request with JSON data is sent to the HTTPS server. 

2) In presentation layer, you JSON needs to be serialised (converting data to flate byte data strings)

3) In session layer, you request to establish TCP connection/TLS

4) In transport layer, you send SYN request to target port 443 which is HTTPS

5) In network layer, SYN in an IP packet(S) and adds the source/destination IP

6) In data link layer, each packet goes into a single frame and adds the source/destination MAC addresses 

7) Finally in physical layer, each frame becomes a string of bits which is converted into either radio signal (wifi), electrical signal (ethernet), or light (fibre)





Ports are logical endpoints for communication. When your device wants to send or recieve data, it uses these ports to make sure that data goes to the right place. 

Protocols are rules governing data transmission. The importance of ports and protocls is that they facilitate communication between devices. 