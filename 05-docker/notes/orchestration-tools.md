# Notes

# Orchestration Tools

## Key Concepts

- Kubernetes Introduction
- Difference between Docker Swarm and Kubernetes
- Why and When to use Orchestration Tools

## What I Learned

I learned what orchestration tools are and the very basics of what kubernetes and docker swarm are and their differences. Additionally I learned why you should use orchestration tools.

## Your Notes

Kubernetes (k8s) is an open source platform designed to automate the deployment, scaling, and operation of application containers. It provides features such as `container orchestration`, `automatic scalings` and `self-healing`. These features ensure that applications run smoothly and efficiently no matter the scale. K8s ensures that all containers is deployed correctly, can scale up or down to meet demand and automatically recovers from failures. It helps solve the challenges that arrise when you move beyond a handful of containers on a single machine to managing a fleet of containers across multiple machines. It abstracts the underlying nfrastructure, allowing you to focus on your application rather than the intricacies of managing individual containers. 

Docker swarm is another container orchestration tool. This is docker's native clustering and orchestration tool and is built into docker. It is designed to be straightforward making it a good choice for simpler or smaller deployments. Docker swarm does not have built in auto scaling capabilities menaing you'll need to manage scaling manually or through external tools. It also has a good community that supports it. It's easier to start a cluster as it is simple and integrates seamlessly with existing docker setups. However it is limited to the docker API's capabilities.

as your applications grow and scale, managing containers manually becomes increasingly difficult. Orchestration tools are designed to help you manage large scale deployments and ensure that your application runs smoothly across multiple environments. You should use orchestration tools because: they manage large-scale deployments, ensure high availability, automate scaling and recovery, simple, enhance reliability and also improve resource utilisation.