# Notes


# Intro to Docker

## Key Concepts

- What are containers and their benefits
- What is Docker
- Images
- VMs vs Container
- Docker Files

## What I Learned

I learned what docker is and it's components. I learned what conatiners and images are and what makes containers different to VMs. I learned how the set up of a VM is different to containers and the pros and cos of each of them and when you might want to use one over the other. Additionally I learned the basics of what a dockerfile contains and how they are used to create an image.

## Your Notes

### What Are Containers?

Containers are **lightweight, portable units for running applications**. They package an application with its dependencies, helping it run consistently across compatible environments.

Each container has its own isolated processes and filesystem while sharing the underlying **host OS kernel**. This reduces overhead compared with running a separate operating system for each application.

### How Containers Fit Together

| Layer | Purpose |
| :--- | :--- |
| **Containers** | Run applications with their required binaries, libraries and dependencies. |
| **Docker Engine** | Builds images and creates, runs and manages containers. |
| **Host OS** | Provides the kernel and operating system resources used by Docker. |
| **Infrastructure** | The underlying compute, memory and storage, such as your local machine or a cloud server. |

> **Note:** On macOS and Windows, Docker Desktop typically runs Linux containers inside a Linux virtual machine.

### Benefits of Containers

- **Isolation:** Helps prevent applications and their dependencies from interfering with one another.
- **Consistency:** Packages the application and its dependencies together, reducing “it works on my machine” problems.
- **Resource efficiency:** Shares the host kernel, using fewer resources than a full virtual machine.
- **Fast startup:** Starts application processes without booting a separate guest OS.
- **Portability:** Makes applications easier to move between compatible development, testing and production environments.

### Key Components of Docker

| Component | Purpose |
| :--- | :--- |
| **Docker Engine** | The core software that builds images and runs and manages containers. |
| **Docker Hub** | A registry for finding, storing and sharing container images. |
| **Docker Compose** | Defines and runs applications made up of multiple containers using a YAML configuration file. |

### Dockerfiles, Images and Containers

- **Dockerfile:** A text file containing instructions for building an image.
- **Image:** An immutable template containing the application, its dependencies and configuration defaults. To make changes, you build a new image.
- **Container:** An instance of an image, with its own runtime state and writable layer. Containers can be running or stopped.

**Typical workflow:** Write a Dockerfile → Build an image → Create and run a container.

> Changes made inside a container do not modify its original image. Use volumes to persist data beyond the container’s lifecycle.

### Containers vs Virtual Machines

#### Virtual Machines

A **virtual machine (VM)** runs a full guest operating system alongside its applications and dependencies.

A **hypervisor** creates and manages VMs, allocating resources such as CPU, memory and storage. It can run directly on physical hardware or on top of a host OS, depending on the type of hypervisor.

Each VM has its own kernel, providing strong isolation but requiring more resources and time to start.

#### Containers

Containers isolate applications at the **process level** while sharing the underlying host kernel.

Because each container does not need a full guest OS, containers are generally smaller, start faster and use fewer resources than VMs.

### Key Differences

| Feature | Containers | Virtual Machines |
| :--- | :--- | :--- |
| **Operating system** | Share the underlying host kernel. | Each VM has its own guest OS and kernel. |
| **Startup time** | Typically seconds or less. | Typically longer, often tens of seconds to minutes. |
| **Resource usage** | Lower overhead; no separate guest OS per container. | Higher overhead from running a full guest OS. |
| **Isolation** | Process isolation with a shared kernel. | Stronger isolation through separate guest kernels and a hypervisor. |
| **Portability** | Usually smaller and easier to distribute; require compatible OS and CPU architecture. | Usually larger; may require compatible hypervisors or image conversion. |

> **Remember:** A VM virtualises a machine; a container isolates an application.

### Dockerfile

A dockerfile is a series of instructions which say how to build the docker image. Each instruction in a docker file creates a layer in the docker image which makes it easy to track changes and optimize your builds. 

#### 5 Key Commands

| Command | Description |
| :--- | :--- |
| `FROM` | Specifies the base image to use for the Docker image |
| `RUN` | Executes commands in the container (used to install packages) |
| `COPY` | copies files from the host machine into the container |
| `WORKDIR` | Sets the wokring directory for subsequent instructions |
| `CMD` | Specifies the command to run when the container starts |

#### Example

```dockerfile
FROM node:14
WOKRDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
```