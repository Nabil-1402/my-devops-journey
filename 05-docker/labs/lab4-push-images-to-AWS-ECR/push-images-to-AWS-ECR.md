# Labs

# Lab: [Push Images to AWS ECR]

## Objective

Push my docker images to my AWS ECR

## Commands Used

```
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 840032438341.dkr.ecr.eu-west-2.amazonaws.com

docker build -t flask-mysql .

docker tag flask-mysql:latest 840032438341.dkr.ecr.eu-west-2.amazonaws.com/flask-mysql:latest

docker push 840032438341.dkr.ecr.eu-west-2.amazonaws.com/flask-mysql:latest

docker network create my-app-network
```

I changed the docker compose file to look like this:
```

services: #List all of the different parts of our app 
  web:
    image: 40032438341.dkr.ecr.eu-west-2.amazonaws.com/flask-mysql:latest #ECR repository 
    ports:
      - "5002:5002"
    depends_on: #Says to start the service in depends on first before this one
      - mydb

  mydb:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw
```
I added the image tag instead of build so that when I run `docker-compose up` it can go to the ECR and pull the image to build it.

Then I ran the container and vistied localhost:5002

## Output

The output of this lab was a private ECR called flask-mysql created with a docker image tagged latest inside of it. Also when accessing localhost:5002 it showed a welcome message with my MySQL version number. The outputs can be seen in the screenshots folder.

## Challenges

I had a few challeneges during this lab. The first one was that I was running into an error when trying to retrieve an authentication token and authenticate your Docker client to your registry. To fix this I had to use the command `aws configure` to configure my aws account to the aws CLI. Another problem I faced was that when I tried running my application on localhost:5002 it would not work and the reason for that was becasue I had not built the image yet. I used `docker build -t flask-mysql .` to fix that.

## What I Learned

In this lab I learned how to create a private container reigsirty in AWS using ECR and how to push/pull containers from it and run them.

