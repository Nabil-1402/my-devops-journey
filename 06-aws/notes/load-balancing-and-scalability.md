# Load Balancing and Scalability

## Key Concepts

- **Vertical scaling:** Increasing the CPU, RAM or storage capacity of an existing server.
- **Horizontal scaling:** Adding or removing instances to match demand.
- **Elasticity:** Adjusting resources as demand rises and falls, often automatically.
- **High availability:** Keeping an application available when infrastructure components fail.
- **Elastic Load Balancing (ELB):** AWS's managed service for distributing traffic across targets.
- **Load balancer types:** Application, Network, Gateway and Classic Load Balancers.
- **Listeners and target groups:** Rules for accepting connections and selecting the resources that receive traffic.
- **Health checks:** Checks that help a load balancer determine whether targets can serve requests.
- **Sticky sessions:** Keeping a client's requests associated with a particular target.
- **TLS termination and SNI:** Handling encrypted connections and selecting certificates for different hostnames.
- **Deregistration delay:** Allowing existing work to finish when a target is removed.
- **Auto Scaling Groups (ASGs):** Maintaining and adjusting the number of EC2 instances.
- **Scaling policies and CloudWatch:** Using metrics or schedules to control capacity.

## What I Learned

In this module, I learned how scalability, high availability and load balancing work together to keep applications responsive as demand changes. I explored the difference between vertical scaling, which increases the resources of an existing server, and horizontal scaling, which adds more instances. I also learned how deploying across multiple Availability Zones can help an application continue running if one location fails.

I learned how AWS load balancers distribute traffic, check target health and route requests to different services. I explored when to use an Application Load Balancer for HTTP-based routing, a Network Load Balancer for transport-layer traffic, and a Gateway Load Balancer for network appliances. I also covered security groups, sticky sessions, TLS certificates, SNI and deregistration delay. Finally, I learned how Auto Scaling Groups use minimum, desired and maximum capacity settings alongside scaling policies to adjust EC2 capacity as demand changes.

## Detailed Notes

### 1. Scalability and High Availability

**Scalability** is the ability of an application or system to handle a greater workload by increasing its resources.

#### Vertical Scaling

Vertical scaling means increasing the resources of an existing server, such as its CPU, RAM or storage capacity.

- The server becomes more powerful, but the number of servers stays the same.
- It is common for workloads running on a single machine, such as a database.
- Services such as Amazon RDS and ElastiCache offer options to use larger instance or node sizes.
- There are limits to how large an individual machine can become.
- Depending on the service and configuration, resizing can involve interruption.

**Example:** Moving an application from an EC2 instance with 2 vCPUs to one with 8 vCPUs.

#### Horizontal Scaling

Horizontal scaling means adding more instances to share the workload. Removing instances when demand falls is called scaling in.

- It is common for distributed systems and web applications.
- Traffic can be spread across instances using a load balancer.
- Multiple instances can improve resilience if the application is designed to tolerate instance failures.
- Shared state and data must be handled carefully so requests can be served by different instances.

**Example:** Increasing an application's capacity from two EC2 instances to four.

> **Scalability and elasticity are related:** Scalability describes the ability to handle increased demand; elasticity describes adjusting capacity as demand changes.

#### High Availability

**High availability** means designing a system to remain available when components fail.

In AWS, a common approach is to deploy across at least two **Availability Zones (AZs)**. This reduces reliance on one location.

- **Active/passive:** One component serves traffic while another is available to take over, such as a traditional RDS Multi-AZ DB instance deployment.
- **Active/active:** Multiple components serve traffic simultaneously, such as application instances spread across AZs behind a load balancer.

| Concept | Main purpose |
| --- | --- |
| Scalability | Handle a larger workload. |
| Elasticity | Adjust resources as demand changes. |
| High availability | Continue serving users when components fail. |

### 2. Load Balancing

A **load balancer** distributes incoming traffic across multiple backend resources, called **targets**.

AWS provides **Elastic Load Balancing (ELB)** as a managed service. Depending on the load balancer type, targets can include EC2 instances, IP addresses and other supported resources.

#### Why Use a Load Balancer?

- Spread traffic across multiple targets.
- Provide a single DNS endpoint for an application.
- Detect unhealthy targets and normally route traffic to healthy ones.
- Support availability across multiple AZs.
- Terminate TLS connections where supported.
- Support session affinity where needed and supported.
- Provide an internet-facing or internal entry point.

AWS manages the load balancer infrastructure, maintenance and service scaling. You still configure listeners, targets, security settings and application availability.

#### Reverse Proxies

A **reverse proxy** receives requests on behalf of backend servers and forwards them to the appropriate destination. Load balancing is one function a reverse proxy can perform.

An ALB acts as a reverse proxy for HTTP applications. It can inspect request information and route traffic to different services based on paths, hostnames or headers.

For example:

- `/users` can route to a user service.
- `/orders` can route to an order service.
- `api.example.com` can route to an API service.

### 3. Health Checks

Health checks help the load balancer determine whether a target can respond to requests.

For HTTP-based checks, you configure settings such as:

- A health check port.
- A path, such as `/health`.
- Expected response codes.
- Check intervals and timeouts.
- Healthy and unhealthy thresholds.

A target becomes unhealthy after the configured number of consecutive failures. It can become healthy again after enough successful checks.

> HTTP `200 OK` is a common success response, but success codes are configurable. NLB also supports TCP health checks, which do not use HTTP paths or response codes.

If all targets fail health checks, load balancer behaviour can differ from normal healthy-target routing. Health checks should therefore be combined with monitoring and sufficient application capacity.

### 4. Types of AWS Load Balancers

| Type | Layer | Main purpose |
| --- | --- | --- |
| **Application Load Balancer (ALB)** | Layer 7: Application | HTTP and HTTPS applications requiring request-based routing. |
| **Network Load Balancer (NLB)** | Layer 4: Transport | High-throughput network traffic, including TCP, TLS and UDP. |
| **Gateway Load Balancer (GWLB)** | Layer 3: Network | Distributing traffic to virtual network appliances such as firewalls. |
| **Classic Load Balancer (CLB)** | Layers 4 and 7 | Older-generation load balancing for existing architectures. |

ALB and NLB are common choices for new application architectures. GWLB serves a different purpose: integrating network appliances into traffic paths.

### 5. Load Balancer Security Groups

For a typical internet-facing ALB architecture:

1. Allow client traffic to the ALB on the required listener ports, such as HTTPS port `443`.
2. Allow application instances to receive traffic on their application port from the ALB's security group.
3. Allow the required health check traffic.
4. Configure the ALB's outbound rules so it can reach its targets.

This allows users to reach the application through the ALB while restricting direct access to the backend instances.

### 6. Application Load Balancer (ALB)

An ALB operates at **Layer 7**, primarily handling **HTTP and HTTPS** traffic. It also supports features such as HTTP/2 and WebSocket connections.

Because it understands HTTP requests, it can route traffic using request attributes.

#### Routing Options

- **Path-based routing:** Route `/users` and `/orders` to different services.
- **Host-based routing:** Route `api.example.com` and `shop.example.com` separately.
- **Header-based routing:** Route using specified HTTP header values.
- **Query-string routing:** Route using query parameters.

An ALB can route to multiple applications on different machines or to applications using different ports on the same machine. This is useful for microservices and container workloads.

With Amazon ECS, dynamic host port mapping can allow tasks on the same EC2 instance to be registered using different ports.

#### Useful Details

- An ALB provides a DNS hostname; its underlying IP addresses can change.
- The backend normally sees the ALB connection rather than a direct client connection.
- The `X-Forwarded-For` header carries client IP information.
- `X-Forwarded-Port` identifies the destination port used by the client.
- `X-Forwarded-Proto` identifies the client protocol, such as HTTP or HTTPS.

### 7. Target Groups

A **target group** defines a set of destinations and associated settings, including health checks.

ALB target types include:

- EC2 instances.
- IP addresses, including those used by supported container workloads.
- Lambda functions.

A target group often represents a particular service. Listener rules determine which target group receives a request.

An Auto Scaling Group can automatically register new EC2 instances with an attached target group and deregister instances when they are removed.

### 8. Network Load Balancer (NLB)

An NLB operates at **Layer 4**, handling connections using configured protocols and ports. It is designed for high throughput and low latency.

#### Key Features

- Support for TCP, TLS and UDP traffic, among other supported protocols.
- A static IP address for each enabled AZ.
- Optional Elastic IP addresses for internet-facing deployments.
- Suitability for applications requiring stable IP addresses or transport-layer load balancing.

An NLB can carry HTTP traffic over TCP, but it does not provide ALB-style routing based on HTTP paths and headers.

**TLS termination is supported through a TLS listener.** Alternatively, a TCP listener can pass encrypted traffic through to the backend, where the application terminates TLS.

Potential use cases include gaming backends, network services and applications requiring static IP addresses.

> Avoid relying on fixed ALB-versus-NLB latency figures. Actual performance depends on workload, configuration and network conditions.

### 9. Sticky Sessions (Session Affinity)

Sticky sessions associate a client's traffic with a particular target for a period of time.

- **ALB and CLB:** Support cookie-based stickiness for supported HTTP configurations.
- **NLB:** Uses source-IP-based stickiness where supported; it does not use HTTP cookies.

For example, a shopping application might store a user's cart in one instance's memory. Routing that user back to the same instance helps preserve access to that local session.

#### Trade-offs

- Traffic may become unevenly distributed.
- A busy client or group of clients can place extra load on one target.
- Stickiness does not protect local session data if that target fails.

Using a shared session store can allow different instances to serve the same user without relying on local session state.

### 10. SSL and TLS

**SSL** stands for **Secure Sockets Layer**. It is an older protocol that has been superseded by **TLS**, which stands for **Transport Layer Security**.

The term “SSL certificate” is still commonly used, although modern HTTPS connections use TLS.

TLS provides encryption in transit, helps detect tampering and authenticates the server using a certificate. Certificates are issued by trusted **Certificate Authorities (CAs)** and must be renewed before they expire.

#### Certificates on Load Balancers

Load balancers use **X.509 certificates**. AWS Certificate Manager (**ACM**) helps provision and manage supported certificates.

- An ALB uses an **HTTPS listener** for TLS termination.
- An NLB uses a **TLS listener** for TLS termination.
- Traffic from the load balancer to the backend is a separate connection; its encryption depends on the backend protocol configuration.

Terminating TLS at the load balancer does not automatically encrypt the backend connection.

#### Certificate Configuration

- Configure a default certificate for the listener.
- Add additional certificates where supported to serve different hostnames.
- Use SNI to select the appropriate certificate.
- Choose a security policy that controls supported TLS versions and cipher suites.

#### Server Name Indication (SNI)

**SNI** is a TLS extension that lets a client include its intended hostname during the handshake. The server can then select a matching certificate.

If the client does not supply SNI, or no certificate matches, the listener uses its default certificate.

| Load balancer | Certificate support |
| --- | --- |
| CLB | One certificate per secure listener; no SNI certificate selection. |
| ALB | Multiple certificates on an HTTPS listener using SNI. |
| NLB | Multiple certificates on a TLS listener using SNI. |

### 11. Connection Draining and Deregistration Delay

This feature helps avoid interrupting work when a target is removed.

| Load balancer | Feature name |
| --- | --- |
| CLB | Connection draining. |
| ALB and NLB | Deregistration delay. |

When a target is deregistered, the load balancer stops assigning new work to it and allows time for existing requests or connections to finish, subject to the configured behaviour and timeout.

This is useful during deployments, instance replacement and scaling in. Choose a delay appropriate to the application's request or connection duration.

Deregistration is different from simply failing a health check: the exact handling of existing connections depends on the load balancer and its settings.

### 12. Auto Scaling Groups (ASGs)

An **Auto Scaling Group** maintains a collection of EC2 instances and can adjust capacity as demand changes.

Its goals include:

- **Scaling out:** Adding instances when more capacity is needed.
- **Scaling in:** Removing instances when less capacity is needed.
- Maintaining the desired number of instances within configured limits.
- Registering instances with attached load balancer target groups.
- Replacing instances that are considered unhealthy.

#### Capacity Settings

| Setting | Meaning |
| --- | --- |
| Minimum capacity | The lowest permitted capacity. |
| Desired capacity | The capacity the ASG currently aims to maintain. |
| Maximum capacity | The highest permitted capacity. |

**Example:** With a minimum of `2`, desired capacity of `3` and maximum of `6`, the ASG initially aims for three instances and can scale between two and six.

### 13. Using an ASG with a Load Balancer

The load balancer and ASG have different responsibilities:

- The **load balancer** distributes incoming traffic across registered targets.
- The **ASG** maintains or changes the number of instances.

As demand increases, a scaling policy can increase desired capacity. The ASG launches instances, registers them with the attached target group, and the load balancer begins routing traffic once the targets are ready and healthy.

If you enable Elastic Load Balancing health checks for the ASG, it can use that health information to replace unhealthy instances. Load balancer health checks alone do not automatically configure ASG replacement behaviour.

### 14. Launch Templates and ASG Configuration

A **launch template** defines how EC2 instances are launched. It can specify settings such as:

- Amazon Machine Image (AMI).
- Instance type.
- EC2 user data.
- EBS volume configuration.
- Security groups.
- SSH key pair.
- IAM instance profile.
- Supported network interface settings.

The **ASG configuration** separately defines settings such as:

- Subnets and Availability Zones.
- Minimum, desired and maximum capacity.
- Attached load balancer target groups.
- Health check settings.
- Scaling policies.

Launch templates are the preferred approach for new configurations; launch configurations are the older mechanism.

### 15. CloudWatch Alarms and Scaling

Amazon CloudWatch monitors metrics that scaling policies can use to adjust capacity.

Examples include:

- Average CPU utilisation across the ASG.
- ALB requests per target.
- Custom application metrics.

A CloudWatch alarm can trigger a scaling action when a metric crosses a configured threshold.

- A **scale-out policy** adds capacity.
- A **scale-in policy** removes capacity.

### 16. Scaling Policies

#### Target Tracking Scaling

Target tracking adjusts capacity to keep a supported metric close to a chosen target.

**Example:** Keep average ASG CPU utilisation near `40%`.

AWS creates and manages the associated CloudWatch alarms.

#### Simple Scaling

Simple scaling applies a configured capacity adjustment when an alarm triggers, then uses a cooldown period before further simple scaling activity.

**Example:** Add two instances when CPU utilisation exceeds `70%`.

#### Step Scaling

Step scaling chooses an adjustment based on how far a metric exceeds an alarm threshold.

**Example:**

- CPU between `70%` and `85%`: add one instance.
- CPU above `85%`: add three instances.

Target tracking, simple scaling and step scaling are forms of **dynamic scaling**.

#### Scheduled Scaling

Scheduled scaling changes capacity settings at specified times based on predictable demand.

**Example:** Increase minimum capacity to ten instances at `17:00` every Friday before an expected traffic increase.

Scheduled scaling is separate from dynamic scaling because it responds to a timetable rather than a metric crossing a threshold.