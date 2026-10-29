# AWS Global Infrastructure

## Key Concepts

- AWS Regions
- Choosing an AWS Region
- AWS Availability Zones (AZs)
- AWS Points of Presence (Edge Locations)

## What I Learned

I learned about AWS’s foundational infrastructure, including Regions, Availability Zones and edge locations. I explored why they are important and how they can guide infrastructure decisions for my own projects, particularly when considering users, performance and reliability.

## Notes

### AWS Regions

An **AWS Region** is a separate geographical area containing multiple Availability Zones.

Each Region has a unique identifier, such as `eu-west-1` or `eu-west-2`. It is important to know which Region you are working in, particularly when setting up services.

Most AWS services are **Region-scoped**, meaning resources such as EC2 instances and S3 buckets are created in a chosen Region. The location of these resources can affect performance, costs and compliance with data residency requirements.

### How to Choose an AWS Region

Consider the following factors:

- **Compliance and data residency:** Choose a Region that meets relevant legal and data governance requirements. Check the data handling behaviour of the services you use.
- **Proximity to customers:** Hosting resources closer to users can reduce latency.
- **Service availability:** Some services and features are only available in certain Regions.
- **Pricing:** Costs vary between Regions, so compare the relevant service pricing pages.

### AWS Availability Zones (AZs)

An **Availability Zone** consists of one or more discrete data centres within an AWS Region, with independent power, networking and connectivity.

Each Region contains multiple AZs. They are physically separated to reduce the risk of a single event affecting several zones, while remaining connected through low-latency networking.

Distributing infrastructure across multiple AZs can improve:

- **High availability:** Services can remain accessible if an AZ becomes unavailable.
- **Fault tolerance:** Applications can continue operating when part of the infrastructure fails.

Achieving these benefits also depends on how the application and its resources are configured.

### Edge Locations

**Edge locations** are sites used by services such as Amazon CloudFront to deliver content closer to end users.

CloudFront can cache content at edge locations, reducing the distance requests need to travel back to the original server.

Benefits include:

- Reduced latency
- Faster content delivery
- Reduced load on the origin server

Think of edge locations as local warehouses that keep copies of content closer to customers.

### Global and Regional AWS Services

#### Examples of Global Services

- **AWS Identity and Access Management (IAM):** Manages access to AWS resources.
- **Amazon Route 53:** Provides DNS and traffic routing.
- **Amazon CloudFront:** Delivers content through a global network of edge locations.

#### Examples of Region-Scoped Services

- **Amazon EC2:** Provides virtual servers.
- **Amazon S3:** Stores objects in buckets located in a chosen Region.
- **AWS Elastic Beanstalk:** Deploys and manages applications.
- **AWS Lambda:** Runs code without requiring you to manage servers.
- **Amazon Rekognition:** Analyses images and videos.

> **Note:** AWS WAF supports both regional resources and global CloudFront distributions, so its scope depends on the resource being protected.