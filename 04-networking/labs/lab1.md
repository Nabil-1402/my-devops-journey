# Labs

# Lab: [Understanding nslookup and dig]

## Objective

1) Use nslookup to query your own domain or query youtube.com
2) Use dig to query youtube.com domain and explore the output

## Commands Used

**Part 1:**
nslookup youtube.com

**Part 2:**
dig youtube.com

## Output

**Part 1:**
Server:		192.168.0.1
Address:	192.168.0.1#53

Non-authoritative answer:
Name:	youtube.com
Address: 192.178.223.136
Name:	youtube.com
Address: 192.178.223.91
Name:	youtube.com
Address: 192.178.223.93
Name:	youtube.com
Address: 192.178.223.190


**Part 2:**
; <<>> DiG 9.10.6 <<>> youtube.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6614
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;youtube.com.			IN	A

;; ANSWER SECTION:
youtube.com.		133	IN	A	142.250.151.93
youtube.com.		133	IN	A	142.250.151.136
youtube.com.		133	IN	A	142.250.151.190
youtube.com.		133	IN	A	142.250.151.91

;; Query time: 14 msec
;; SERVER: 192.168.0.1#53(192.168.0.1)
;; WHEN: Wed Oct 14 17:22:38 BST 2026
;; MSG SIZE  rcvd: 104


## Challenges

No challenges

## What I Learned

I learned how you can use both nslookup and dig to learn more about a domain and how to find a domains IP addrees.


