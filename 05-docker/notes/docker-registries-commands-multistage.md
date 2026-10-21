# Notes

# Docker Registries, Commands & Multi-Stage Builds

## Key Concepts

- What Docker registries are
- Public and private container registries
- Docker commands
- Multi-stage builds

## Commands

| Command | Description |
|---|---|
| `docker images` | Show all Docker images you have. |
| `docker inspect <ImageID>` | Get more information about a specific image. |
| `docker rmi <ImageID>` | Remove a specific image. |
| `docker system prune` | Remove unused Docker objects, including unused images, stopped containers, and unused networks. |
| `docker ps` | View all running containers. |
| `docker stop <ID>` | Stop a container from running. |
| `docker rm <ID>` | Delete a container. |

## What I Learned

I learned what Docker registries are and explored examples of public and private registries. I used an AWS ECR private registry to practise working with private registries. I then learned the core Docker commands and how to minimise image size using multi-stage builds.

## Your Notes

### Docker Registries

Docker registries act as storage and distribution hubs for Docker images. They can be public or private.

- **Public registries:** Docker Hub is an example of a registry that is open to everyone.
- **Private registries:** AWS ECR allows you to restrict access to your images and control who can access them. This is crucial when dealing with sensitive, proprietary applications.

### Benefits of Docker Registries

**Streamlined deployment**

Once Docker images are stored in a registry, they can be accessed and deployed across multiple environments, from development to production. This makes rolling out new features or updates faster and more reliable.

**Improved collaboration**

Storing images in a centralised registry gives everyone on your team access to the same resources. This makes images easier to share and manage, improving teamwork and efficiency.

**Consistency across environments**

Storing images in a registry helps ensure that the same image is used in development, testing, and production.

### Typical Workflow

1. **Build:** Build your Docker image locally.
2. **Test:** Create a container from the image and check that the application runs as expected.
3. **Push:** Push the image to a Docker registry, such as AWS ECR.
4. **Pull and deploy:** Pull the image from the registry to deploy it in your staging or production environment.

### Multi-Stage Builds

Docker images should be as small as possible to improve efficiency and reduce bandwidth and storage usage. One way to optimise your Dockerfile is through **multi-stage builds**.

Multi-stage builds allow you to use multiple `FROM` statements in a Dockerfile:

- **Build stage:** Builds the application using the required files and dependencies.
- **Runtime stage:** Creates the final image using only the application and dependencies needed to run it.

This approach discards unnecessary files and build dependencies, producing a smaller, optimised image.

Smaller images are quicker to pull from a registry, faster to deploy, and use less disk space.

### Example: Current Dockerfile

```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

RUN pip install flask mysqlclient

EXPOSE 5002

CMD ["python", "app.py"]
```

While this works, it leaves all build dependencies in the final image, making it larger than necessary.

The intended refactor uses a build stage to install the necessary dependencies, then copies the application and its runtime dependencies into a smaller runtime image.

### Example: Refactored Dockerfile

```dockerfile
# Stage 1: Build stage
FROM pyhton:3.8-slim AS Build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

COPY . .

RUN pip install flask mysqlclient

# Stage 2: Production stage
FROM python:3.8-slim

WORKDIR /APP

COPY --from=Build /app /app

EXPOSE 5002

CMD ["python", "app.py"]
```