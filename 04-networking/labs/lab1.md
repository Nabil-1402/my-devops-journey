# Labs

# Lab: [Understanding nslookup and dig]

## Objective

1. Use `nslookup` to query your own domain or `youtube.com`.
2. Use `dig` to query `youtube.com` and explore the output.

## Part 1: Querying with nslookup

### Command

```bash
nslookup youtube.com
```

### Output

```text
Server:     192.168.0.1
Address:    192.168.0.1#53

Non-authoritative answer:
Name:   youtube.com
Address: 192.178.223.136
Name:   youtube.com
Address: 192.178.223.91
Name:   youtube.com
Address: 192.178.223.93
Name:   youtube.com
Address: 192.178.223.190
```

### Understanding the Output

- **Server:** The DNS resolver that answered the query.
- **Address:** The resolver's IP address and port, `53`.
- **Non-authoritative answer:** The response came from a resolver rather than directly from the domain's authoritative name server.
- **Name and Address:** The queried domain and its returned IPv4 addresses.

## Part 2: Querying with dig

### Command

```bash
dig youtube.com
```

### Output

```text
; <<>> DiG 9.10.6 <<>> youtube.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6614
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;youtube.com.           IN  A

;; ANSWER SECTION:
youtube.com.        133 IN  A   142.250.151.93
youtube.com.        133 IN  A   142.250.151.136
youtube.com.        133 IN  A   142.250.151.190
youtube.com.        133 IN  A   142.250.151.91

;; Query time: 14 msec
;; SERVER: 192.168.0.1#53(192.168.0.1)
;; WHEN: Wed Oct 14 17:22:38 BST 2026
;; MSG SIZE  rcvd: 104
```

## Challenges

No challenges encountered.

## What I Learned

I learned how to use `nslookup` and `dig` to query a domain's IP addresses.

I also learned how to interpret key parts of the output, including the responding DNS resolver, record type, TTL and query time.