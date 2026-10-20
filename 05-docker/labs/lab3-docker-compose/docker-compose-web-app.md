# Labs

# Lab: [Docker Compose for web app and MySQL]

## Objective

Use a docker compose file to spin up the web app and MySQL containers in one command

## Commands Used

I first had to create a docker-compose.yml file to have the following content:
```

services: #List all of the different parts of our app 
  web:
    build: . #Tells docker compose to build the web service from the docker file in the current directory
    ports:
      - "5002:5002"
    depends_on: #Says to start the service in depends on first before this one
      - mydb

  mydb:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw
```

Then type in the command `docker-compose up` to build and run both the web app and MySQL containers.
Once finished I typed the command `docker-compose down` to stop these containers.

## Output

The output was seeing `Hello, World! MySQL version: 8.4.11` at localhost:5002

## Challenges

Faced no challenges.

## What I Learned

What I learned from this lab was how using docker compose can make building and running multi container applications more efficient and how to write a basic docker-compose.yml file and the contents that go inside of it.
