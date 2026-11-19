# Notes

# Containers

## Key Concepts

- Point 1
- Point 2

## Commands

`command` - what it does

## Examples

```Dockerfile
FROM ubuntu:18.04

COPY . /app
RUN make /app

CMD python3 /app/app,y
```

## What I Learned



## Your Notes
### What is a container
A container is a lightweight portable box that holds your application and everything that it needs to run like : your code, the app itself, libraries software components, dependencies, etc.

solves the "It works on my machine problem"

Containers are much faster than VMs as they share the host kernel whereas a VM has to install its own OS.

Containers are made up of images which are blueprints for your application and when they are running it is called a container.

### Docker on as OS
Instead of installing multiple application directly on the servers OS, docker allows us to package and run each appication in a container. Every container is olated from each other but they share the resources of the host, cpu, memory and network. 

Containers are lightweight because they do not carry their own OS.

### Where are docker images stored
Docker images are like a blue print for your application and are stored in the Docker Repositories

You have public and private repos: Docker Hub (public) and Amazon ECR (Private)

ECR stands for Elastic Container Registry. This is designed specifically for AWS users and it integrates deeply with AWS  services and provides secure storage withyour Docker images. With ECR you can choose to store your images publically using Amazaon ECR Public Gallery. 

### Docker vs. Virtual Machines
They both allow us to run applications in isolated environments but in differeent ways. 

VMs are full fledged virtual systems that mimic hardware. Every VM has its own OS and that takes up a lot of resources. Then you have the hypervisor which is the software that manages multiple VMs on the same physical machine. Each VM gets its own chunk of resources from the host machine. One downside of VMs are that it has its own OS, meaning they are large and slow to boot up. Since each VM runs its own OS the resource usage is much higher. 

Docker uses conterisation. This is a more lightweight way of running an isolated application. Containers share the kernel unlike VMS. This is the core of the OS, which makest them much lighter. The docker daemon is what manages containers. Containers are much faster to start and stop compared to VMs. Since they dont use their own OS they also use less resources like CPU. They are allso portable, docker containers can run on any OS that supports docker. 

The key difference is the VMs virtualise hardware whereas docker virtualises the OS.

### Getting Started with Docker
Everything starts with a Dockerfile which is essentially a recipe for a docker image. It contains instructtions for docker on how to make a container. 

The `FROM` line tells Docker which base image to use. The base image is an exisisting OS or environment to start from.
The `COPY` line copies your application code, all files from your computer into a container. 
The `RUN` line is used to execute any commands you need to during the build process, such as compiling or setting up dependencies.
The `CMD` line is used to define the command that will run when the conatiner starts. 

Once the docker image is ready you run a build command e.g. `docker build -t app .`.
After that has been built you can run the image to spin up a container using something like `docker run -d --name app app`.

You can also do a docker push and pull when using a docker repo. 

### Container-related Services on AWS
1) Amazon ECS 
    - Amazons own conatiner platform
    - Fully managed service that allows you to run containers without having to install and manage orchestration software
    
2) Amazon EKS (Elastic Kubernetes Service)
    - Amazon's managed K8s service and is open source
    - You can take advantages of all the k8s featires like load balancing, scaling while AWS handles the management of the k8s control plane

3) AWS Fargate
    - A serverless platform 
    - Works with ECS nad EKS
    - Removes the need fo you to manage servers, or EC2 isntances. You just define the task and Fargate provisions the infrastructure automatically. 
    - Good option when you do not want to worry about managing the underlying infrastructure for your containers

4) Amazon ECR
    - Container image repo where you can store, manage and retrieve Docker images
    - Private by default

### Amazon ECS - EC2 Launch Type
With ECS you have different launch types

When you create a cluster you need to select a launch type. EC2 launch type means that you are responsible for the infrastructure. Each EC2 instance must run the ECS agent to register in the ECS Cluster. The agent is what registers the instance in the ECS cluster making it available to run your containers. 

Once the EC2 instance is registered, ECS takes care of starting/ stopping your containers. It handles the lifecycle of the containers. 

This is good if you want more control over your instances liek customising for certain performance needs or compliance.

### Amazon ECS - Fargate Launch Type
Fargate is serverless, meaning you dont worry managing any CE2 isnatnces. AWS handles all of that for you behind the scenes. You only need to define the tasks requirements for you based on the CPU/RAM you need. 

You create task definitions which are instructrtions which tell AWS how to run your containers with the resources you need. To scale you just need to increase the number of tasks that your container needs to run. No need to add more CE2 isntances. AWS handles having to add more containers by itself. 

Fargate is ideal for teams that want to avoid the hassle of maning infrastructure and want to focus on building applciations. Perfect for workloads where you want to focus on flexibility.