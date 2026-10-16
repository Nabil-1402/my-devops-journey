# Notes


# DNS

## Key Concepts

- What DNS is and why it is useful
- DNS components and record types
- The DNS hierarchy
- How DNS resolution works
- DNS troubleshooting commands
- The `/etc/hosts` file

## Commands

| Command | Purpose |
| :--- | :--- |
| `dig <domain>` | Queries a domain's A records by default and displays detailed DNS information. |
| `dig NS <domain>` | Finds the name servers associated with a domain. |
| `dig +short NS <domain>` | Displays a concise list of the domain's name servers. |
| `dig AAAA <domain>` | Queries a domain's IPv6 addresses. |
| `dig MX <domain>` | Finds the mail servers associated with a domain. |
| `nslookup <domain>` | Queries DNS and displays information such as a domain's IP addresses. |
| `traceroute <domain>` | Investigates the network path towards a destination. Some routers may not respond. |

> **Remember:** `dig` and `nslookup` investigate DNS. `traceroute` investigates the network path.

### Examples

```bash
dig google.com
dig NS google.com
dig +short NS google.com
dig AAAA google.com
dig MX google.com
nslookup google.com
traceroute google.com
```

## What I Learned

I learned how DNS translates domain names into IP addresses and how its hierarchy connects root servers, TLD servers and authoritative name servers.

I also learned how recursive resolvers find and cache DNS records, how to investigate DNS using `dig` and `nslookup`, and how `/etc/hosts` can override name resolution locally for development and testing.

## Your Notes

### What Is DNS?

The **Domain Name System (DNS)** lets us access websites and services using memorable names instead of numerical IP addresses.

For example, DNS can resolve `www.example.com` to an IP address that a client can connect to.

> **Remember:** DNS finds the address. Connecting to the server and loading the website happen afterwards.

### DNS Components

#### Name Servers

Name servers answer DNS queries. Their role depends on whether they are acting as a **recursive resolver** or an **authoritative name server**.

| Type | Role |
| :--- | :--- |
| **Recursive resolver** | Finds DNS answers on behalf of clients, querying other servers when needed and caching results. |
| **Authoritative name server** | Holds DNS records for the zones it serves and provides authoritative answers about those records. |

> A recursive resolver may already have the answer in its cache, allowing it to respond without querying other servers.

#### DNS Zones and Zone Files

A **DNS zone** is a portion of the DNS namespace managed by a particular administrator or organisation.

A **zone file** is a text representation of the records within a zone. DNS providers may also store and manage these records using databases.

Zones contain information such as:

- IP addresses associated with names
- Mail servers
- Authoritative name servers
- Domain verification records

> A domain and a zone are related, but they are not always identical. A subdomain can be delegated to a separately managed zone.

#### Resource Records

DNS information is stored as **resource records**.

| Field | Meaning |
| :--- | :--- |
| **Name** | The name the record applies to, such as `www.example.com`. |
| **TTL** | Time to Live: how long a DNS answer may be cached before it must be refreshed. |
| **Class** | The record's protocol class, usually `IN` for Internet. |
| **Type** | The kind of record, such as `A`, `AAAA` or `MX`. |
| **Data** | The value stored in the record, such as an IP address or another domain name. |

### Common DNS Record Types

| Type | Purpose |
| :--- | :--- |
| **A** | Maps a name to an IPv4 address. |
| **AAAA** | Maps a name to an IPv6 address. |
| **CNAME** | Makes one name an alias of another name, rather than pointing directly to an IP address. |
| **MX** | Identifies mail servers responsible for receiving email for a domain, with preference values. |
| **TXT** | Stores text, commonly used for domain verification and email policies such as SPF. |
| **NS** | Identifies the authoritative name servers for a zone and supports delegation. |
| **SOA** | Stores zone administration information, including its serial number and maintenance timers. |

### The DNS Hierarchy

DNS uses a hierarchy to help resolvers find the servers responsible for a name.

| Level | Role |
| :--- | :--- |
| **Root (`.`)** | Directs resolvers to the name servers for top-level domains. |
| **Top-level domain (TLD)** | Domains such as `.com`, `.org` and `.net`; their servers provide delegations to authoritative servers for registered domains. |
| **Domain** | A name such as `example.com`, whose records are served by its authoritative name servers. |
| **Subdomain or host name** | A name below the domain, such as `www.example.com` or `api.example.com`. |

> Root and TLD servers usually provide referrals to other name servers, rather than the website's final IP address.

### How DNS Resolution Works

Assume you enter `www.example.com` into your browser and no relevant answers are cached:

1. **Local name resolution**
   - The browser and operating system may check caches and local mappings such as `/etc/hosts`.
   - The exact order depends on the application and system configuration.

2. **Query the recursive resolver**
   - The client sends a DNS query to its configured resolver.
   - The resolver checks its own cache before making further queries.

3. **Query a root server**
   - The resolver asks about `www.example.com`.
   - The root server refers it to the `.com` TLD name servers.

4. **Query a `.com` TLD server**
   - The TLD server refers the resolver to the authoritative name servers for `example.com`.

5. **Query an authoritative name server**
   - The authoritative server returns the requested record, such as an A or AAAA record.
   - If it returns a CNAME, the resolver may need to resolve the target name too.

6. **Return and cache the answer**
   - The resolver returns the answer to the client.
   - Results can be cached according to their TTLs.

7. **Connect to the destination**
   - The browser uses the IP address to establish a connection and request the website.

> **Memory aid:** Local checks → Resolver → Root → TLD → Authoritative → Answer → Connection.

### Domain Registrar vs DNS Hosting Provider

| Service | Purpose |
| :--- | :--- |
| **Domain registrar** | Lets you register and renew domain names and manages registration details with the relevant registry. |
| **DNS hosting provider** | Operates authoritative name servers and lets you manage your domain's DNS records. |

The same company can provide both services, but they can also be handled by different providers.

### The `/etc/hosts` File

The `/etc/hosts` file provides **local mappings between IP addresses and host names**.

For applications using the system's name resolution settings, these entries commonly take precedence over DNS. Behaviour can vary depending on system configuration, application behaviour and caching.

#### Example Entry

```text
192.168.1.50    app.test
```

This maps `app.test` to `192.168.1.50` on your machine.

#### Common Uses

- **Development:** Point a test name to a local application.
- **Testing:** Check a new server before updating public DNS.
- **Troubleshooting:** Test whether an incorrect DNS answer is causing a connection problem.

> Changes to `/etc/hosts` affect your machine only. They do not update public DNS or configure the destination server.

### Troubleshooting Reminders

- **Unexpected DNS answer:** Use `dig` or `nslookup` to inspect the returned records.
- **Suspected resolver issue:** Query a specific resolver, for example `dig @1.1.1.1 example.com`.
- **Network path issue:** Use `traceroute`, remembering that missing replies do not necessarily mean traffic is being dropped.
- **Website works but CSS returns `404`:** Check the stylesheet URL and server configuration; DNS has already resolved the host serving that response.

> **Note:** `dig` and `nslookup` query DNS directly and generally do not use `/etc/hosts`, so their results can differ from applications using system name resolution.