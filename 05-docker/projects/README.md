# Projects

# CoderCo Containers Challenge

Building a Multi-Container Application

## Objective

Create a multi-container application that consists of a simple Python Flask web application and a Redis database. The Flask application should use Redis to store and retrieve data.

## Requirements

1. **Flask Web Application**:
   - A Flask app that has two routes:
     - `/`: Displays a welcome message.
     - `/count`: Increments and displays a visit count stored in Redis.

2. **Redis Database**:
   - Use Redis as a key-value store to keep track of the visit count.

3. **Dockerize Both Services**:
   - Create Dockerfiles for both the Flask app and Redis.
   - Use Docker Compose to manage the multi-container application.

## Test the Application

Access the Welcome Page:

Open your browser and go to `http://localhost:5001` to see the welcome message.
Test the Visit Count:

Navigate to `http://localhost:5001/count` to see the visit count increment each time you refresh the page.


## Bonus

- Persistent Storage for Redis: Configure Redis to use a volume to persist its data.
- Environment Variables: Modify the Flask application to read Redis connection details from environment variables and update the docker-compose.yml accordingly.
- Scaling the Application: Scale the Flask service to run multiple instances and load balance between them using Docker Compose.


## Solution

### Step 1: Create the Flask Application

I started by creating a Flask application with two routes:

- `/`: Displays a welcome message.
- `/count`: Increments and displays the visit count stored in Redis.

I then connected the application to Redis and used `redis.incr()` to increase the counter each time the `/count` route is visited.

### Step 2: Containerise the Flask Application

I created the following Dockerfile to build an image for the Flask application:

```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "app.py"]
```

This Dockerfile:

- Uses `python:3.8-slim` as the base image.
- Sets the working directory inside the image to `/app`.
- Copies `requirements.txt` into the image and installs the dependencies.
- Copies the remaining application files from the build context into `/app`.
- Documents that the application listens on port `5001`.
- Runs `python app.py` when the container starts.

The official Redis image already includes Redis and its startup command. To meet the requirement for a separate Redis Dockerfile, only a `FROM` instruction is needed. The Compose configuration below uses the official image directly.

### Step 3: Configure Docker Compose

I created a `docker-compose.yml` file to define and run both services:

```yaml
services:
  web:
    build: .
    ports:
      - "5001:5001"
    depends_on:
      - redis

  redis:
    image: redis:latest
    ports:
      - "6379:6379"
```

This configuration defines two services:

- **web:** Builds the Flask image using the default `Dockerfile` in the current directory and maps port `5001` on the host to port `5001` in the container.
- **redis:** Uses the official Redis image and publishes port `6379` on the host.

Docker Compose creates a shared network, allowing Flask to connect to Redis using the hostname `redis`. The `depends_on` setting starts the Redis container before the web container, although it does not wait for Redis to be ready to accept connections.

To build and start the application, I ran:

```bash
docker-compose up 
```

### Step 4: Test the Application

#### Welcome Page

I visited `http://localhost:5001/` and confirmed that the welcome message appeared.

![Flask welcome page](container-challenge/screenshots/welcome-page.png)

#### Visit Counter

I visited `http://localhost:5001/count` and refreshed the page to confirm that the visit count increased with each request.

![Flask visit count stored in Redis](container-challenge/screenshots/count-page.png)

## Bonus Tasks

### Persistent Storage

To include persistent storage in my application, I made use of Docker volumes.

I did this by updating the `Docker-compose.yml` file, adding the `volumes:` key within the Redis service and then defining the volume the application uses outside the `services` section.

```yaml
services:
  web:
    build:
      context: .
      dockerfile: Flask/Dockerfile
    ports:
      - "5001:5001"
    depends_on:
      - redis

  redis:
    build: ./Redis
    volumes:
      - redis-data:/data

volumes:
  redis-data:
```

Here you can see that, within the Redis service, the left side of the colon is the name of the volume I am creating, and the right side is the directory inside the container where the volume is mounted and Redis stores its data.

### Environment Variables

To make the application more flexible, I made use of environment variables. I first edited the `app.py` file to import the `os` library so that the application can read environment variables available to it. Then I created variables that read those values and use defaults if the environment variables are not set.

```python
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis = Redis(host=redis_host, port=redis_port)
```

Then I edited the `Docker-compose.yml` file to provide these environment variables to the application. I did this by using the `environment:` key and putting the two environment variables under it. This falls under the `web` service.

```yaml
services:
  web:
    build:
      context: .
      dockerfile: Flask/Dockerfile
    ports:
      - "5001:5001"
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379

  redis:
    build: ./Redis
    volumes:
      - redis-data:/data

volumes:
  redis-data:
```

The values defined in the Compose file are passed to the `web` container. The defaults in `app.py` are used if those variables are not set.

### Scaling the Application

To scale the Flask service to run multiple instances and load balance between them using Docker Compose, I used Nginx. Nginx is a reverse proxy that can also perform load balancing.

A load balancer directs traffic to different instances of the same application based on an algorithm, such as round robin. Some load balancers can also check the health of instances and direct traffic only to healthy ones.

I incorporated Nginx by first changing the `ports:` key under the `web` service in the `Docker-compose.yml` file to `expose:`. This documents the port used by the web service without publishing it directly to the host, avoiding a host-port conflict when running multiple instances.

Then I added a service called `nginx`, which has its own image, a published port and a configuration file mounted as a volume. It also depends on the `web` service, so Compose starts the web service before starting Nginx.

I then created an `nginx.conf` file. This is the configuration file for Nginx.

```nginx
events {}

http {
    upstream flask_app {
        server web:5001;
    }

    server {
        listen 5001;

        location / {
            proxy_pass http://flask_app;
        }
    }
}
```

```yaml
services:
  web:
    build:
      context: .
      dockerfile: Flask/Dockerfile
    expose:
      - "5001"
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379

  redis:
    build: ./Redis
    volumes:
      - redis-data:/data

  nginx:
    image: nginx:latest
    ports:
      - "5001:5001"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web

volumes:
  redis-data:
```

To start three instances of the web service, I can use:

```bash
docker-compose up --build --scale web=3
```

Nginx can distribute requests across the web containers resolved when it starts. If the number of containers changes later, Nginx may need to be restarted to pick up the updated addresses.