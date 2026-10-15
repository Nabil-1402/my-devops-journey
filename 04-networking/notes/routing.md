# Notes

# Routing

## Key Concepts

- What is routing?
- Static vs Dynamic routing
- Common routing protocols


## What I Learned

I learned what routing is and why it is important. I also learned the difference between static and dynamic routing and also learned about OSPF and BGP protocols. From my previous knowledge I know that routes can be decided by matching IP cidr blocks which tell you where the next jump is to go to and also what a default gateway is.

## Your Notes
Routing is the process of determining paths for data to travel across networks. It's importance is that it ensures data reaches its destination efficiently. It is fundemental for internet functionality.

Routers determine the best path by using routing tables to make decisions.

Static routing is where routes are manually set up by network admins. It is like giving your data a fixed map to follow. It is reliable but does not adapt well if there are changes or issues on the route, if the route changes, you have to update it manually. It is simple to set up but not scalable. 

Dynamic routing uses algorithms and more complex protocols to automatically find the best path for data. It is more flexible and adapt to network changes. The routes are automatically adjusted. This is much more scalable and adaptable. 


Routing protocols are essential becuase they automate the process of deterining the best route for datato travel across the network. They also enhance network efficiency. Routing protocols use algorithms to figure out the best paths for data. The importance is that they automate routing updates and improve entwork resilience. 

`OSPF` - stands for Open Shortest Path First. This protocol finds the shortest path for data  to travel. It is used mainly for within large organisations. It uses somethings called **link state information**. It uses this to make routing decisions. Which means it uses the status of the network and the links and the cost to use them. This protocol is known for its fast convergence. That means it can quickly recalculate routes when there are changes in the network. 

`BGP` - stands for Broder Gateway Protocol. It is used to route data between different autonomous systems. Autonomous systems are like large networks managed by single organisations. This protocol uses a path vector mechanis, which means that it maintains the path information that gets updated dynamically as the network topology changes. BGP allows network admins to define routing policies based on various attributes. 