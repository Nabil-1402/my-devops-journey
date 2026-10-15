# Notes


# Troubleshooting

## Key Concepts

- Common Network Issues
- Identifying Symptons

## Commands

`ping <ip address/name>` - Sends an ICMP request to the IP you want to reach, used to test if something is reachable

`traceroute <name>` - Tracks the path of your data takes to reach a certain destination

`nslookup <name>` - Query DNS

## Examples

ping google.com

traceroute google.com

nslookup google.com

## What I Learned

I learned why we need to do network troubleshooting as well as the common network issues. Additionally I learned what symptons could potentially be identified and steps on how to troubleshoot a website you cannot reach.

## Your Notes

The reason for troubleshooting is to: esnure smooth operation, identify and fix network problems and minimise downtime. 

**Common Network Issues:**
- Connectivity loss (suddenly losing connection), could happen due to hardware failures, cable issues or even problems on your network.
- Slow network performance
- IP address conflicts, when two devices on the same network end up with the same IP address. 
- DNS resolution failures, 


**Identifying Symptons:**
- Observe the problem
- Check physical connections
- Verify network configuration
- Test with ping command


**Practical Example:**

"I cant reach a website, how can I troubleshoot?"

1) Check network connectivity, ensure your machine has a working internet, try using ping
2) Do a dig or nslookup to verify that there is no issue with your DNS
3) Check your host file to make sure there is no overriding entries
4) Check firewall rules to make sure that a firewall is not blocking any outgoing or incoming traffic
5) Browser might have issues so try closing it and opening it again
6) Check your DNS cache, if you have to clear it
7) Check your system logs, do a traceroute 
