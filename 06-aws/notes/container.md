# Containers, Docker, and AWS

## Key Concepts

- **Containers and images** — An image packages an application and its dependencies. A container is an instance of that image.
- **Dockerfile** — A set of instructions Docker uses to build an image.
- **Container isolation** — Containers run in isolated environments while sharing the host kernel and resources such as CPU and memory.
- **Containers and virtual machines** — Containers share a kernel, while each virtual machine runs its own guest operating system.
- **Container registries** — Docker Hub and Amazon ECR store and distribute container images.
- **Container orchestration** — Amazon ECS and Amazon EKS help deploy, manage, and scale containerised applications.
- **AWS Fargate** — Runs supported ECS and EKS workloads without requiring you to manage the underlying servers.
- **ECS operations** — IAM roles, load balancers, and service auto scaling control permissions, traffic routing, and task capacity.

## What I Learned

I learned how Docker packages an application and its dependencies into an image so it can run consistently across compatible environments. I can follow the workflow from writing a Dockerfile to building an image, running it as a container, and pushing it to a registry. I also learned why containers typically start faster than virtual machines and how sharing the host kernel reduces overhead.

I learned how AWS services fit together when deploying containers. Amazon ECR stores the images, while Amazon ECS or Amazon EKS runs and manages the workloads. With ECS on EC2, I can customise and manage the underlying instances. With Fargate, I specify the resources my tasks need and AWS provides the compute capacity. I also learned which IAM role to check when a task cannot pull an image or when the application itself cannot access an AWS service.

## Docker Fundamentals

### What Is a Container?

A container packages an application with the files, libraries, and other dependencies it needs to run. This helps solve the “it works on my machine” problem by making the application environment consistent across compatible hosts.

An **image** is the template used to create containers. You can start multiple containers from the same image, each with its own running processes.

Docker lets you run multiple applications on the same host in separate containers. The containers share the host kernel and physical resources, while Docker provides isolation for their processes and filesystems. You can also set CPU and memory limits for individual containers.

### Containers vs. Virtual Machines

| Feature | Containers | Virtual machines |
| --- | --- | --- |
| What they virtualise | The operating system environment | Hardware |
| Operating system | Share the host kernel | Each VM runs its own guest OS |
| Management | Docker Engine manages containers in a Docker setup | A hypervisor manages VMs |
| Startup and overhead | Typically faster to start and lighter to run | Typically take longer to boot and use more resources |
| Portability | Images can run on compatible container platforms | VMs can run on compatible hypervisors |

### Container Registries

A **registry** hosts repositories. A **repository** groups related images, and tags such as `v1` or `v2` identify specific builds or releases.

- **Docker Hub** supports public and private repositories.
- **Amazon Elastic Container Registry (ECR)** provides private repositories and a public registry through Amazon ECR Public.

Use `docker push` to upload a tagged image and `docker pull` to download one.

## Getting Started with Docker

A Dockerfile describes how to build an image and what command its containers run by default.

| Instruction | Purpose |
| --- | --- |
| `FROM` | Selects the base image. |
| `WORKDIR` | Sets the working directory for subsequent instructions. |
| `COPY` | Copies files from the build context into the image. |
| `RUN` | Executes a command during the image build, such as installing dependencies or compiling code. |
| `CMD` | Specifies the default command to run when a container starts. |

### Example: Package a Python Script

Create an `app.py` file:

```python
print("Hello from Docker!")
```

Create a `Dockerfile` in the same directory:

```dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY app.py .

CMD ["python", "app.py"]
```

Build and run the image from that directory:

```bash
docker build -t app .
docker run --rm app
```

The `.` tells Docker to use the current directory as the build context. The container prints its message and exits. For a long-running application such as a web server, use `docker run -d --name app app` to start it in the background.

## AWS Container Services

| Service | What it does |
| --- | --- |
| **Amazon ECS** | AWS-managed container orchestration. It schedules and runs containers as tasks. |
| **Amazon EKS** | Managed Kubernetes on AWS. AWS manages the Kubernetes control plane. |
| **AWS Fargate** | Provides serverless compute for supported ECS tasks and EKS pods. |
| **Amazon ECR** | Stores and distributes container images through public or private repositories. |

## Amazon ECS

### EC2 and Fargate Launch Types

A **task definition** describes how to run one or more containers, including their images, CPU, memory, and IAM roles. A **task** is a running instance of a task definition. An **ECS service** maintains the desired number of tasks for an application.

| Launch type | How it works | When to use it |
| --- | --- | --- |
| **EC2** | You provide and manage the EC2 instances. The ECS agent registers each instance with the cluster so ECS can place tasks on it. | When you need control over instance types, host configuration, or specific performance and compliance requirements. |
| **Fargate** | You specify the CPU and memory requirements in the task definition. AWS provides the underlying compute when ECS starts each task. | When you want to run containers without managing EC2 instances. |

With either launch type, you can scale an ECS service by changing its desired task count. With EC2, the cluster also needs enough instance capacity to place the extra tasks.

### IAM Roles

| Role | Who uses it | Typical permissions |
| --- | --- | --- |
| **EC2 instance role** | The ECS agent on an EC2 container instance, through its instance profile | Registering the instance and communicating with ECS. |
| **Task execution role** | ECS when preparing and running a task | Pulling private images from ECR, sending logs to CloudWatch Logs, and retrieving secrets referenced by the task definition. |
| **Task role** | The application running inside the container | Calling AWS APIs the application needs, such as reading from an S3 bucket. |

If ECS reports an `AccessDenied` error while pulling a private image or retrieving a secret at startup, check the **task execution role**. If the application starts but receives `AccessDenied` when it calls an AWS API, check the **task role**.

### Load Balancer Integrations

| Load balancer | Layer | Common use |
| --- | --- | --- |
| **Application Load Balancer (ALB)** | Layer 7 | HTTP and HTTPS applications. It can route requests to different services based on the hostname or URL path. |
| **Network Load Balancer (NLB)** | Layer 4 | Transport-level traffic such as TCP or UDP, high-throughput or low-latency workloads, and AWS PrivateLink integrations. |
| **Classic Load Balancer (CLB)** | Layer 4 or 7 | Legacy ECS configurations. CLB is unsupported with Fargate. |

### ECS Service Auto Scaling

ECS Service Auto Scaling uses AWS Application Auto Scaling to adjust the desired task count. Common metrics include CPU utilisation, memory utilisation, and ALB requests per target.

- **Target tracking** adjusts capacity to keep a metric near a target, such as 60% average CPU utilisation.
- **Step scaling** adds or removes capacity in steps based on how far a metric breaches a CloudWatch alarm threshold.
- **Scheduled scaling** adjusts capacity at specified times for predictable demand.

With Fargate, AWS provides the compute capacity for additional tasks. With EC2, task scaling and instance capacity both need to be considered.

## Amazon ECR

Amazon ECR stores container images that services such as ECS can pull when they start workloads. IAM controls access to private repositories.

- **Image tags** give builds or releases recognisable names such as `v1.0`.
- **Image scanning** helps identify known vulnerabilities in container images.
- **Lifecycle policies** automatically expire images that match rules based on criteria such as age or image count.

If an image push or pull fails with an authorisation error, check the registry login and the IAM permissions of the user or role performing the operation.

## Amazon EKS

Amazon Elastic Kubernetes Service runs Kubernetes on AWS. AWS manages the control plane, while you choose how to provide compute for your workloads. EKS can suit teams already using Kubernetes on-premises or in another cloud because they can carry over familiar Kubernetes tooling and workflows.

EKS clusters are regional. For a multi-region deployment, you can run a cluster in each region. CloudWatch Container Insights can help collect and monitor cluster and workload metrics and logs.

### EKS Compute Options

| Option | How it works | When to use it |
| --- | --- | --- |
| **Managed node groups** | EKS manages the provisioning and lifecycle of EC2 worker nodes in an Auto Scaling group. Groups can use On-Demand or Spot Instances. | When you want AWS to handle routine node management while retaining EC2 flexibility. |
| **Self-managed nodes** | You provision and manage EC2 worker nodes, often with an Auto Scaling group and an EKS-optimised AMI. | When you need more control over node configuration, updates, or maintenance. |
| **AWS Fargate** | AWS provides compute for eligible pods that match a Fargate profile. | When your workloads can run on Fargate and you want to avoid managing worker nodes. |