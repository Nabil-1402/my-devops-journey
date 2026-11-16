# Notes

# Load Balancing and Scalability

## Key Concepts

- Point 1
- Point 2

## Commands

`command` - what it does

## Examples

(code examples)

## What I Learned



## Your Notes

### Scalability and High Availability
Scalability means that an application / system can handle greater loads by adapting.

There are two kinds of scalability:
- Vertical Scalability
- Horizontal Scalability (= elasticity)

Vertical scalability means that when you add more power to your existing system like adding more cpu, RAM or storage. The machine gets more powerful but stays the same. This is common for non distributed systems such as a databse.  RDS and ElastiCache are services that can scale vertically. There is usually a limit to how much you can vertically scale (hardware limits). 

Horizontal is when you add more intsances of a resource to handle the load. Instead of making one server bigger you add more servers. Horizontal scaling implies distributed systems. This is very common for web applications / modern applications. It is easy to horizontally scale because of services like EC2. It is also easier to manage in the long run becasue if one sytem fails you have got others to cover. This means that resilience is also added to your system. 

Scalability is linked but different to High Availability. Scalability is about handling different level of loads while availability is about your system is up and running even when parts of it fail. 

High availability refers to running your application or system in multiple locations to ensure that if one part of your infrastructure fails another part can take over. You typically achieve this in AWS by running your application across at least two AZs. The goal of HA is to survive data centre loss. The high availability can be passive (for RDS
Multi AZ for example). The high availability can be active (for horizontal scaling). 

### Load Balancing
Load balancing is a way to distribute traffic across multiple servers. 

AWS has a service called ELastic Load Balancer (ELB). When traffic comes in it forwards the request to EC2 instances forward downstream. This means that it constantly checks which instances are healthy and it directs traffic to the instances that can handle it. This process keeps your application available and responsive even when one instance/ server is down. 


### Reverse Proxy
This is similar to a load balancer but with a little extra functionality. It also sits in between users and your servers, handling requests but it can do more than just direct traffic. Using AWS Application Load Balancer allows you to use reverse proxy feature such as routing traffic based on things like content of the request, route traffic to different services/microservices. A reverse proxy can also be used to protect the backend. 


#### Why use a load balancer
- Spread load across multiple downstream instances
- Expose a single point of access (DNS) to your application
- Seamlessly handle failures of downstream instances
- Do regular health checks to your instances
- Provide SSL termination (HTTPS) for your websites
- Enforce stickiness with cookies
-  High availability across zones
- Separate public traffic from private traffic

An Elastic Load Balancer is a managed load balancer
- AWS guarantees that it will be working
- AWS takes care of upgrades, maintenance, high availability
- AWS provides only a few configuration knobs

#### Health Checks
Health Checks are crucial for Load Balancers
They enable the load balancer to know if instances it forwards traffic to are available to reply to requests
The health check is done on a port and a route (/health is common)
If the response is not 200 (OK), then the instance is unhealthy

Health checks are automated 

#### Types of Load Balancers
AWS has 4 kinds of managed Load Balancers
• Classic Load Balancer (v1 - old generation) - 2009 - CLB
- HTTP, HTTPS, TCP, SSL (secure TCP)

• Application Load Balancer (v2 - new generation) - 2016 - ALB
- HTTP, HTTPS, WebSocket

• Network Load Balancer (v2 - new generation) - 2017 - NLB
- TCP, TLS (secure TCP), UDP

• Gateway Load Balancer - 2020 - GWLB
- Operates at layer 3 (Network layer) - IP Protocol

Overall, it is recommended to use the newer generation load balancers as they provide more features. Some load balancers can be setup as internal (private) or external (public) ELBs.

If you are running a traditional web application then you would most likely want to use ALB as you want to be able to take advantage of its content based routing and modern protocols like websockets. Unless your application requires handling large volumes of TCP traffic with minimal latency then use NLB. Then for things like network applications, firewalls, and more advanced networking setups then use a gateway load balancer. 


#### Load Balancer Security Groups
It is very important you have the right security group rules for your load balancer to make sure traffic is routed safely. The goal is to allow users to reach the load balancer fromanywhere on the internet. Then typically for our application(EC2 instance) we want to accept only inbound traffic from the load balancer and not the public internet. 


#### Application Load Balancer
ALB opperates at layer 7 (Application layer) specifically HTTP and HTTPS

It understands the content within the request such as headers, cookies, URLs, etc. 

It has the ability to load balance traffic to multiple HTTP applications across machines (target groups). It can also load balance traffic to multiple applications on the same machine. It also has support for HTTP/2 and websockets. 

ALBs route traffic to differnet trarget groups, these target groups can be instances and lambda functions. With ALBs you can route based on the path of the URL making it perfect for microservice architecture. It also has host based routing, where you can request data by using the host name. This allows you to run multiple domains on the same ALB. It also lets you route traffic based on on things like query strings and headers. This gives you a lot more ocntrol over how traffic is routed, making it ideal for personalised or device specific experiences. ALB also has a port mapping feature to redirect to a dynamic port in ECS. How we use an ALB if we were to use an CLB (class load balancer) we would need multiple CLBs instead of one ALB. 

**Good to knows:**
- ALB gives each load balancer a fixed host name in the format XXX.region.elb.amazonaws.com
- The application servers don't see the IP of the client directly
    - The true IP of the client is inserted in the header X-Forwarded-For
    - We can also get Port (X-Forwarded-Port) and proto (X-Forwarded-Proto)

#### Target Groups
These are the groups of resources like EC2, Lambda, and ECS that your ALB routes traffic to. They are destionations for load balancing requests. Each target group is usually tied to a certain service appplciation to scale different parts of your system independently. 

EC2 can be managed and scaled automatically using ASG (Auto Scaling Group). This adds or remove instances based on the amount of traffic recieved. 


#### Network Load Balancer
These are optimised for handling extreme performance and high traffic with low latency

This operates at layer four of the OSI model (Transport Layer) meaning it handles TCP and UDP traffic.

Network load balancers (Layer 4) allow to:
- Forward TCP & UDP traffic to your instances
- Handle millions of request per seconds
- Less latency ~100 ms (vs 400 ms for ALB)

NLB has one static IP per AZ, and supports assigning Elastic IP (helpful for whitelisting specific IP)
NLB are used for extreme performance, TCP or UDP traffic
Not included in the AWS free tier

It i sdesigned for high performance use cases where you want to manage millions of requests per second. 

Key benefits:
- Low letency
- Handles millions of requests per second - making it highly desireable for application with high throughput

The NLB works with raw TCP traffic and forwards this with rules that you defined such as certain ports or protocols. It routes this traffic to different target groups, each handling a different type of application. Eventhough the NLB works at the TCP level it can still handle HTTP as a protocol within the TCP transport layer. However it does not inspect HTTP headers of even handle SSL termination which is different from what you would see within ALB. This makes NLBs great for scenarios where you need raw network performance such as real time applications like gaming servers, streaming services application and so on. Any traffic that depends heavily on latency and connection speed will benefit from being routed via an NLB. 

This setup is especially useful to handle different applciations that depend on different protocols. The user applciation in this case might need to handle pure TCP traffic, while their search application may work with HTTP. 

### Sticky Sessions (Session Affinity)
Sticky sessions ensure that a client is always routed to the same instance behind the load balancer. It works across load balancers.

Behind the scenes the load balancer uses "cookies" to keep track which instance the client is connected to. You can control how long the cookie and stickiness lasts by setting up an expiration date. This cookie is what binds a user to a certain server. 

A typical use case is when your application stores seesion data that is not shared across instances. For example, if a user is interacting with an e-commerce site and the cart data is only specific to one instance you would want them to stick to that instance so that they do not lose that session. By keeping the user on that instance, you avoid situations where they might lose their cart or session information. 

Trade offs include:
- when stickiness is enabled you an potentially overload one server if too many clients are stuck to it, leading to imbalanced traffic distribution
- Usesful for session heavy apps but impacts the app's performance


### SSL / TLS (Basics)
SSL and TLS certificates are crucial when dealing with security over the internet. 

#### SSL
Stands for `Secure Socket Layer`. SSL certificates ensure that traffic between your clients and your load balancer to be encrypted in transit. Often called inflight encryption. 

#### TLS 
Stands for `Transport Layer Security`. It is the more modern version of SSL. These certificates are issued by Certificate Authorities (CAs). They are trustued 3rd parties that verify the identity of a website and some common CAs are:
Comodo, Symantec, GoDaddy, Globalsign, Digicert, Letsencrypt. 

Certificates have an expiration date. When you set them up you get to choose how long they last. After that time frame they need to be renewed. If they are expired then when clients visit a website they do get a big warning letting them know. 

#### Load Balancer - SSL Certificate
The load balancer is the middle man making sure that traffic between your clients and instances are encrypted. This is done by using a X.905 certificate (an SSL/TLS certificate). 

AWS makes it easy to manage certificates by providing a service called AWS Certificate Manager (ACM). Here you can create, renew and manage certificates. When you are setting up a HTTPS listener on your load balancer, this is how we ensure that traffic is encrypted. 

Things you need to know:
- Specifiy a default certificate. This is what is used when no other rules are matched. 
- You can add an optional list of certs to support multiple domains
- Clients can use SNI (Server Name Indication) to specify the hostname they reach
- Ablility to specify a security policy to support older versions of TLS/SSL

#### SSL - Server Name Indication (SNI)
SNI solves the problem of loading multiple SSL certificates onto one web server (to serve multiple websites.)
It's a newer protocol, and requires the client to indicate the hostname of the target server in the initial SSL handshake.The server will then find the correct certificate, or return the default one.

Only works for ALB & NLB (newer generation), CloudFront. Does not work for CLB (older gen). 


#### Elastic Load Balancers - SSL
Classic Load Balancer (v1)
- Support only one SSL certificate
- Must use multiple CLB for multiple hostname with multiple SSL certificates.

Application Load Balancer (v2)
- Supports multiple listener with multiple SSL certificates
- Uses server name indication (SNI) to make it work

Network Load Balancer (v2)
- Supports multiple listeners with multiple SSL certificates.
- Uses server name indication (SNI) to make it work.

### Connection Draining
In AWS this is also known as `deregistration delay`

Feature Naming
- Connection Draining - for CLB
- Deregistration Delay - for ALB & NLB

When you are deregistrating an instance (getting rid of it) in the ALB, maybe because it is unhealthy or you are scaling down, you do not want to cut off any ongoing connections instantly. 

So what happens is, inflight requests to the instance are allowed to complete. The load balancer stops sending new requests to that instance but it waits for the active request to finish up. You can control how long this process takes. 

