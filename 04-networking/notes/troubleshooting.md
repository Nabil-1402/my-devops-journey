# Notes


# Troubleshooting

## Key Concepts

- Common network issues
- Identifying symptoms
- Troubleshooting an unreachable website

## Commands

| Command | Purpose |
| :--- | :--- |
| `ping <IP_or_domain>` | Sends ICMP Echo Requests to test reachability and measure round-trip time. |
| `traceroute <domain>` | Shows responding routers along the path towards a destination. |
| `nslookup <domain>` | Queries DNS to check name resolution. |
| `dig <domain>` | Displays detailed DNS query results. |

> A failed `ping` does not always mean a device is unreachable: ICMP may be blocked. Similarly, missing replies in `traceroute` do not necessarily indicate a broken connection.

## Examples

```bash
ping google.com
traceroute google.com
nslookup google.com
dig google.com
```

## What I Learned

I learned why network troubleshooting matters, how to recognise common network issues, and how to investigate their symptoms.

I also explored a practical process for troubleshooting a website that cannot be reached, including checking connectivity, DNS, local configuration and firewall rules.

## Your Notes

### Why Troubleshoot Networks?

Network troubleshooting helps to:

- Ensure services operate smoothly
- Identify and fix network problems
- Minimise downtime

### Common Network Issues

| Issue | Description |
| :--- | :--- |
| **Connectivity loss** | A connection stops working, potentially because of hardware failures, cable problems or network faults. |
| **Slow performance** | Network communication takes longer than expected. |
| **IP address conflicts** | Two devices on the same network use the same IP address. |
| **DNS resolution failures** | A domain name cannot be resolved to the required address. |

### Identifying Symptoms

- **Observe the problem:** Identify what is failing and whether it affects one device, one website or multiple services.
- **Check physical connections:** Verify cables, Wi-Fi connectivity and network equipment.
- **Verify network configuration:** Check the IP address, subnet mask, default gateway and DNS settings.
- **Test connectivity:** Use `ping`, keeping in mind that some destinations block ICMP.

### Practical Example: “I Cannot Reach a Website”

1. **Check network connectivity**
   - Confirm your device is connected to the network.
   - Try another website and use `ping` to test connectivity.

2. **Check DNS resolution**
   - Use `dig` or `nslookup` to see whether the domain resolves successfully.
   - Check whether the returned address is the expected one.

3. **Check the hosts file**
   - Look for entries in `/etc/hosts` that could override the domain with an incorrect IP address.

4. **Check firewall rules**
   - Verify that relevant traffic is permitted, including outgoing connections and their responses.

5. **Check the browser**
   - Restart the browser or try another browser to see whether the issue is browser-specific.

6. **Check cached DNS information**
   - If you suspect a stale DNS entry, clear the relevant cache and retry.

7. **Inspect logs and the network path**
   - Check relevant system logs for errors.
   - Use `traceroute` to investigate the path towards the destination.

> `dig` and `nslookup` query DNS directly and generally do not check `/etc/hosts`. Successful DNS resolution does not rule out an incorrect hosts-file entry.