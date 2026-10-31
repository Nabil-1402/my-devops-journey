# Notes

# EC2 & Compute

## Key Concepts

- EC2
- Containers — EC2 and EKS
- Serverless — Lambda
- High availability and scalability

## Commands

`command` — What it does.

## Examples

(code examples)

## What I Learned

## Your Notes

### EC2

EC2 stands for **Elastic Compute Cloud** and is part of **Infrastructure as a Service (IaaS)**.

This means that you are renting virtual machines or services from AWS.

EC2 is one of the most popular AWS services because of how flexible it is. You can scale up and down as needed and only pay for what you use.

Its main capabilities include:

- Renting virtual machines (EC2).
- Storing data on virtual drives (EBS/Elastic Block Storage).
- Distributing load across machines (ELB/Elastic Load Balancer).
- Scaling services using an auto-scaling group (ASG/Auto Scaling Group).

#### Instance Configuration

When spinning up an EC2 instance, there are several things you can configure. One is the **operating system**. The OS you choose depends on what your application needs and what you are comfortable managing.

You can also configure how much **compute power, how many cores and how much RAM** you need.

You have options for **storage** too. You can have network-attached storage, such as EBS or EFS (Elastic File System). You can also have hardware-level storage that is physically attached to the host machine. This is fast but temporary.

Other configurations include **networking**. You can configure the speed of the network card depending on how much traffic you expect. You can also choose to get a public IP address, which makes your instance accessible from the internet.

Then you have **firewalls/security groups (SGs)**. You can set up rules specifying who can access your instance and which traffic can get through. This is very important for securing your instance.

You also have something called a **bootstrap script**, also known as **EC2 User Data**. This is a script that runs automatically when the instance launches for the first time. You can use it to install software, run updates or set up tasks when the instance starts.

### EC2 User Data

When you launch an EC2 instance, you can provide something called **user data**. This is a script that runs automatically when the instance starts up for the first time. This is a good way to bootstrap your instance. **Bootstrapping** means running commands when a machine starts.

EC2 user data is used to automate boot tasks such as:

- Installing updates.
- Installing software.
- Downloading common files from the internet.
- Anything you can think of.

The EC2 user data script runs as the **root user**, meaning that it has full control over the system. This makes it powerful, so you should be careful about what you put in the script.

### EC2 Instance Types

Not all instances are created equal. AWS offers different instance types depending on what you are trying to do.

#### General Purpose

These are your go-to, well-rounded instances. They work for lots of different use cases, including basic web servers, small databases and other general workloads.

#### Compute Optimized

If you need lots of processing power, these are useful. They give you extra CPU resources for tasks such as heavy calculations, batch processing or high-performance computing.

#### Memory Optimized

These are useful when your application needs a lot of memory. Workloads such as in-memory databases, big data processing and high-performance computing can all benefit from memory-optimized instances.

#### Storage Optimized

These are designed for fast, high-throughput storage. If you are dealing with large datasets or running databases that require quick access to storage, these instances are the right choice.

#### Accelerated Computing

These are good for GPU-intensive applications. If you are doing machine learning, video processing or scientific simulations, these are what you need.

#### HPC Optimized

HPC stands for **high-performance computing**. These instances are designed for intensive computing tasks that require powerful processing and fast networking.

#### Naming Convention

Using `m5.2xlarge` as an example:

- **`m` — Instance class:** This tells you the general type or purpose of the instance. For example, `m` stands for general purpose, `c` is for compute optimized, `r` is for memory optimized and `t` is for general-purpose instances.
- **`5` — Generation:** This is the generation of the instance.
- **`2xlarge` — Size:** This is the size within the instance class. Instances come in different sizes. The bigger the size, the more resources, such as CPU and memory, the instance has, and the more expensive it is.

### EC2 Instance Purchasing Options

| Purchasing Option | Description |
|---|---|
| **On-Demand Instances** | Short workloads, predictable pricing, pay by the second. |
| **Reserved (1 and 3 years)** | Reserved Instances and Convertible Reserved Instances. |
| **Reserved Instances** | Long workloads. |
| **Convertible Reserved Instances** | Long workloads with flexible instances. |
| **Savings Plans (1 and 3 years)** | Commitment to an amount of usage for long workloads. |
| **Spot Instances** | Short workloads; cheap, but you can lose instances, making them less reliable. |
| **Dedicated Hosts** | Book an entire physical server and control instance placement. |
| **Dedicated Instances** | No other customers share your hardware. |
| **Capacity Reservations** | Reserve capacity in a specific AZ for any duration. |