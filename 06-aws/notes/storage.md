# Notes

# Storage

## Key Concepts

- **EBS volumes:** persistent block storage attached to EC2 instances within the same Availability Zone.
- **Amazon Machine Images (AMIs):** templates used to launch EC2 instances with a preconfigured operating system, software and settings.
- **Amazon EFS:** managed, scalable file storage that multiple instances can access simultaneously.

## What I Learned

In this module, I learned about EBS volumes, AMIs and Amazon EFS. I explored what each service provides, why it is useful, its limitations and when to use it.

## Your Notes

### EBS Volumes

An **Amazon EBS (Elastic Block Store) volume** is like a network drive that you can attach to an EC2 instance. It provides block storage that the instance can use like a disk.

One of the key benefits of EBS is **data persistence**. Data remains on the volume when you stop an instance. When you terminate an instance, whether a volume is preserved depends on its **Delete on Termination** setting. The root EBS volume is normally deleted by default.

EBS volumes are tied to an **Availability Zone (AZ)**. A volume must be in the same AZ as the instance it is attached to. To use its data in another AZ, you can take a snapshot and create a new volume from that snapshot in the destination AZ.

EBS is useful when an instance needs persistent storage, such as for an operating system, application files or a database.

### AMI Overview

**AMI** stands for **Amazon Machine Image**.

You can think of an AMI as a blueprint for launching EC2 instances. It is a preconfigured template containing the information needed to launch an instance, including its operating system and any software or configurations included in the image.

AMIs allow you to reuse an instance configuration instead of setting everything up manually each time. This reduces setup time and helps you launch consistently configured instances.

AMIs are **Region-specific**, but you can copy them to other Regions when needed.

You can launch EC2 instances from:

- **A public AMI:** an image made publicly available by AWS or another provider.
- **Your own AMI:** an image you create and maintain yourself.
- **An AWS Marketplace AMI:** an image offered by a vendor, potentially with additional software charges.

### Amazon EFS

**Amazon EFS (Elastic File System)** is AWS’s managed service for shared file storage.

EFS provides a network file system that multiple instances can mount and access simultaneously. **Regional EFS file systems** store data redundantly across multiple Availability Zones, providing durability and availability. EFS also offers **One Zone** storage, which stores data within a single AZ.

One of the key advantages of EFS is its **scalability**. Storage grows automatically as you add files and shrinks as you remove them, so you do not need to provision a fixed disk size.

Because multiple instances can access the same file system, EFS is useful for applications that need shared files. For example, multiple instances running a content management system could access the same uploaded images and documents.

A drawback is that EFS can be more expensive than other storage options, depending on the workload. It is best suited to applications that need shared file storage across multiple instances.