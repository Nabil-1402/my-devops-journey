# Notes

# Docker Networking & Linking

## Key Concepts

- Types of docker networks
- Uses of docker networks
- Importance of docker networks

## Commands

`docker network ls` - list all docker networks

`docker network create <network name>` - create a custom docker network

## Examples

```
docker network create my-custom-network

docker network ls
```

## What I Learned

I learned what docker networks are and what they are used for. I went over the three types: bridge, host and none. I also learned how to link two containers using a network in lab2.

## Your Notes

Docker provides several default network options that you can use to manage how containers communicate

`Bridge Network` - A default network mode for containers on the same machine. Containers connected to the Brdige Network can communicate with each other using their own IP address. It's isolated from your home machine's network which provides an extra layer of security. 

`Host Network` - In host mode, a container uses the host machine's network directly without any isolation. It is as if the container is plugged directly into your home network with no distinction between the container and the host. This mode is useful for applications that need to closely interact with the host system. 

`None Network` - This option gives a container no network interface at all, which makes it completely isolated. It is used to make sure that a container has no network access whatsoever. This could be useful for certain security scenarios. 


In the context of DevOps, docker networking is particularly important because it simplifies the implementation of microservices arctitecture. Microservices allow different parts of an application to run as independent services each in its own container. 

Docker networking ensures that these services can communicate with each other efficiently and securely. 

Docker's networking model is highly scalable meaning you can easily connect and scale services as your application grows.


In docker creating a custom network allows containers to communicate with each other using container names instead of IP addresses. Especially useful in scenarios such as when you need a Flask app to connect with MySQL database. 