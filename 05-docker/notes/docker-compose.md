# Notes

# Docker Compose

## Key Concepts

- Manage multi container applications
- Positive impact on DevOps

## Commands

`docker-compose up` - bring up all the containers defined in the Docker-compose.yml file. 

`docker-compose down` - stop all the containers from running

`docker-compose logs` - get logs for you containers

## Examples

```
docker-compose up

docker-compose logs

docker-compose down
```

## What I Learned

I learned what docker compose is and how it can be used to help manage multi container applications. Additionally I learned why docker compose is useful in DevOps.

## Your Notes

Docker compose is a tool that allows you to define and manage multi container docker applications. Instead of manually starting and stopping all your containers one by one, docker compose lets you define all your services in a single file and manage them collectively.

### Key Features:
- Docker-compose.yml file
- Commands
- Networking

One of the greatest strengths of docker compose is it's simplicity. With a few commands you can start, stop and manage all your containers at once. 

When you use docker compose it automatically creates a network for your containers. This means that your containers can now communicate easily with each other. 

**Importance in DevOps:**
- Makes development and testing easier
- Ensures consistency
- Enhances teamwork