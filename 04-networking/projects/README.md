# Projects

## Project Objective

Deploy NGINX on an AWS EC2 instance and make the default landing page accessible through a hostname.

For this project, I used a **free DuckDNS subdomain** instead of purchasing a domain. This allowed me to practise connecting DNS to a publicly accessible web server.

## Tools Used

- **Amazon EC2** — hosts the web server.
- **Amazon Linux 2023** — operating system.
- **NGINX** — serves the default landing page.
- **DuckDNS** — maps my hostname to the instance’s public IPv4 address.
- **SSH** — provides secure terminal access to the instance.

## 1. Launching the EC2 Instance

I launched an Amazon Linux 2023 instance with a public IPv4 address and created a key pair for SSH access.

I configured the security group with these inbound rules:

| Type | Protocol | Port | Source | Purpose |
|------|----------|------|--------|---------|
| SSH | TCP | 22 | My public IP/32 | Restrict administration to my connection |
| HTTP | TCP | 80 | 0.0.0.0/0 | Allow public access to the website |

## 2. Connecting Through SSH

On my Mac, I restricted the private key’s permissions:

```bash
chmod 400 ~/Downloads/nginx-lab-key.pem
```

I then connected to the instance:

```bash
ssh -i ~/Downloads/nginx-lab-key.pem ec2-user@EC2_PUBLIC_IP
```

I used the EC2's public IP address after the @

## 3. Installing and Starting NGINX

Inside the EC2 instance:

I installed NGINX:

```bash
sudo dnf install -y nginx
```

I started NGINX and enabled it to start automatically when the instance boots:

```bash
sudo systemctl enable --now nginx
```

## 4. Verifying the Web Server

I checked the NGINX service:

```bash
sudo systemctl status nginx --no-pager
```

The expected status was:

```text
Active: active (running)
```

I checked the HTTP response locally on the instance:

```bash
curl -I http://localhost
```

A successful response included:

```text
HTTP/1.1 200 OK
```

I then opened the following address in my browser to test public access:

```text
http://EC2_PUBLIC_IP
```

This tested the web server and network access before introducing DNS.

## 5. Configuring DuckDNS

I created a free DuckDNS subdomain and set its IPv4 address to the EC2 instance’s public IPv4 address.

DuckDNS managed the DNS record, so I did not need a Route 53 hosted zone.

## 6. Verifying DNS and HTTP Access

From my Mac, I checked the hostname’s A record:

```bash
dig +short YOUR_SUBDOMAIN.duckdns.org A
```

The returned IPv4 address should match the EC2 instance’s public IPv4 address.

I then checked the HTTP response through the hostname:

```bash
curl -I http://YOUR_SUBDOMAIN.duckdns.org
```

A successful response included:

```text
HTTP/1.1 200 OK
```

Finally, I opened the hostname in my browser:

```text
http://YOUR_SUBDOMAIN.duckdns.org
```

The NGINX landing page confirmed that DNS resolution and HTTP access were working together. I used HTTP because HTTPS and a TLS certificate were outside this project’s scope.

## How the Connection Works

1. The browser requests the DuckDNS hostname.
2. DNS resolves the hostname to the EC2 public IPv4 address.
3. The browser connects to that address over TCP port 80.
4. The security group permits the HTTP connection.
5. NGINX receives the request and returns the landing page.

## Screenshots

Project evidence is stored in the [`screenshots`](./screenshots/) folder, located in the same directory as this README.

The screenshots document the configuration and verification steps for this project.

## Key Learning

- An A record maps a hostname to an IPv4 address.
- Security groups control which traffic can reach an EC2 instance.
- SSH and HTTP use different ports and require separate inbound rules.
- `systemctl` checks and manages the NGINX service.
- `dig` verifies DNS resolution, while `curl` checks the HTTP response.
- Testing the public IP before the hostname helps distinguish network or server issues from DNS issues.
