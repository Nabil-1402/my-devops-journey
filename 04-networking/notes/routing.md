# Notes

# Routing

## Key Concepts

- What is routing?
- Static vs dynamic routing
- Common routing protocols: OSPF and BGP

## What I Learned

I learned what routing is, why it matters, and the differences between static and dynamic routing. I also explored OSPF and BGP.

This built on my existing knowledge of how destination IP addresses match CIDR blocks in routing tables to determine the next hop, and how default gateways are used.

## Your Notes

### What Is Routing?

**Routing** is the process of determining paths for data to travel across networks. It enables traffic to reach its destination and is fundamental to how the internet works.

Routers use **routing tables** to decide where to forward packets next.

> **Memory aid:** Routing = choosing where data goes next.

### Static vs Dynamic Routing

| Feature | Static Routing | Dynamic Routing |
| :--- | :--- | :--- |
| **Configuration** | Routes are manually configured by administrators. | Routing protocols automatically learn and update routes. |
| **Network changes** | Usually requires manual updates. | Adapts automatically when changes are detected. |
| **Complexity** | Simple for small networks. | More complex to configure and troubleshoot. |
| **Scalability** | Harder to maintain as the network grows. | Better suited to larger networks. |

**Static routing** is like giving traffic a fixed map to follow. It is predictable, but administrators usually need to update routes when the network changes.

**Dynamic routing** uses protocols and algorithms to calculate routes and adjust them as the network changes. This makes it more adaptable and scalable.

> **Memory aid:** Static = set manually. Dynamic = discovers and adapts.

### Why Use Routing Protocols?

Routing protocols exchange network information and calculate routes.

They help:

- Automate routing updates
- Select paths using metrics or policies
- Improve resilience by adapting to network changes

### OSPF — Open Shortest Path First

**OSPF** is a routing protocol mainly used **within an organisation's network**.

It uses **link-state information**, including network connections and their costs, to calculate the lowest-cost paths.

OSPF is known for **fast convergence**: it can quickly recalculate routes after network changes.

> **Memory aid:** OSPF = lowest-cost paths inside a network.
>
> “Shortest” means lowest total cost, not necessarily the fewest hops.

### BGP — Border Gateway Protocol

**BGP** is used to exchange routing information **between autonomous systems**.

An **autonomous system (AS)** is a collection of networks managed under a common routing policy, such as an internet provider's network.

BGP uses a **path-vector mechanism**, maintaining path information as routes change. Administrators can define routing policies using different path attributes.

> **Memory aid:** BGP = between networks, guided by policies.

### Quick Recap

- **Routing:** Decides where traffic goes next.
- **Static:** Routes are manually configured.
- **Dynamic:** Routes adapt using routing protocols.
- **OSPF:** Uses link states and costs, mainly within a network.
- **BGP:** Uses path information and policies between autonomous systems.