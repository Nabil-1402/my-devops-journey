# Notes


# DNS

## Key Concepts

- What is DNS
- DNS Components
- DNS Components: Records
- How Does DNS Work
- Network Debugging tools
- /etc/hosts File

## Commands

`dig ns <name>` - finds the name servers associated with the name you entered. 

`dig +short ns <name>` - recieve a shorter version which just shows the name servers

`nslook` - used for query DNS servers. You can find information about DNS records for that certain domain. 

## Examples

dig ns google.com

dig +short ns google.com

nslookup google.com

## What I Learned


## Your Notes

DNS allows us students to keep track of websites and hosts by name instead of an IP address. 
The DNS translates domain names to IP addresses.
The role of the DNS in networking is to simplify navigation on the internet, essential for accessing websites and services.

**DNS Components:**
- Name servers
    without them DNS would not work properly. They load DNS settings and configurations, and also respond to your queries from clients or other servers about domain names. 

    - Authoritative
        Hold the actual DNS records. When queried they provide the definitive answers such as the IP address for a domain name. 

    - Recursive
        These servers do not hold the final answer, instead they query the other na,e servers on behalf of the client to find the correct DNS record.  They can also cache the information they retrieve to speed up future queries. 

- Zone Files
    These are stored inside your name servers and they contain information about the domain. They help name servers answer queries about how to get to a domain if the name server does not know the answer directly. 

    They organise your DNS inormation in a readable and managed way, making it easier to handle DNS records. 

- Records
    A zone file is comprised of multiple resource records. Each record contains specific information about hosts, name servers, and various other resources. Some components of resource records are record names, TTL, Class, Type and Data. The record name being the domain name being queried. TTL being how long the record is valid (before refresh is required), Class being the namespace of the record information, Type being the type of record (A, or MX, or AAAA). Then there is also NS being Name server Record and Data being the actual information corresponding to the record type. Like IP address for an A record. 

    - **Types of Records:**
        - A: Maps a domain name to an IPv4 address
        - AAAA: Maps a domain name to an IPv6 address
        - CNAME: Alias of one name to another. It allows you to point to multiple domain names to hsare the same IP address
        - MX: Specifies the mail server responsible for recieving email for the domain
        - TXT: Allows domain administrators to instert any text into DNS. Commonly used for verification purposes and to hold SPF (Sender Policy Framework) data. 


DNS resolution is the process of converting domain names into IP addresses. 

**DNS Hierarchy**
1) DNS Root,keeps high level information about how to find the top level domains underneath it. 
2) TLDs (Top Level Domains), these include familiar extensions like .com, .org, .net. Each TLD stores information about domains within the scope.
3) Authoritative name service, each authoritative name server hosts zones for domains, meaning they have the detailed DNS records for those domains. 
4) Domain, each domain has a zone and a zone file. This is where all the specific information like IP addresses, mail servers of the domains are stored. 


**DNS Resolution Process**
1) As a user you type www.google.com into your browser, which results in your browser sending a request to a DNS resolver that is local to you.
2) The DNS resolver does a query, it recieves a request and starts looking for the IP address. First it checks it's local cache to see if it knows the IP address. If not, it moves to the next step. The resolver then queries a root server for the IP address. Now the root server does not yet know the IP of the domain but knows where to find the .com top level domain server.
3) Go to name server for .com TLD
4) The resolver then queries a .com TLD server. A TLD server does not know the exact IP address of google.com either, but it knows which authoritative name server to ask. 
5) It goes to the name server
6) The resolver queries the authoritative name server for google.com, This server has a definitibe IP address. 
7) Then the IP address is returned to your DNS resolver
8) The DNS resolver then send sthe IP address back to your browser



Domain Registrar is an entity that allows you to purchase and register domains. They have a relationship with the TLD registries for various TLDs. The registrar communicates with the TLD registry to manage domain registrations. 


A DNS hosting provider is an entity that operates DNS name servers that host DNS zones. They allow you to manage these DNS records within these DNS zones. 

**DNS Query Process**
1) First the client, like your computer, wants to visit a website. It starts by checking the local cache and the host file (/etc/hosts) to see if it already knows the IP address. 
2) If the IP address is not cache locally then the client sends a query to their configured DNS resolver. 
3) The resolver is like a librarian who knows where to find inormation. Now the DNS resolver checks its own cache. I fit finds the IP address there it returns the result to the client if not it goes to the next step
4) The resolver first asks the DNS root server for a .com TLD. 
5) The root server then responds with the address of the .com registry name server. 
6) The The resolver then asks the websites authoritative name server for the website for the DNS record of the website. 
7) Returns the website's name server, results are cached
8) Returns the DNS record for the website to the websites DNS name server
9) Returns DNS record tp the resolver


**How to use local host file (/etc/hosts)**

The /etc/hosts file is a local file on your computer that maps domain names to IP addresses. These files take precedence over DNS for specific entries. 

When you type a domain name into your browser, your computer first checks the /etc/hosts file. If the domain is listed in this file then it uses the provided IP address instead of querying the DNS server. This can be useful for testing, development and even troubleshooting. 