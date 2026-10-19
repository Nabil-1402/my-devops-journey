# Labs

# Lab: [Linking web app with a MySQL database]

## Objective

Link the web app from lab1 with a MySQL database.

## Commands Used

First thing I did was change the flask app from lab1 to include a MySQL database connection. Then I had to change the docker file to also install the mysqlclient dependency. 

```Dockerfile
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
Also to link containers together I needed to create a custom network. This will be a bridge network.

To do this I ran the following command:
```
docker network create my-custom-network
```

Then I created a container for the MySQL database. To do this I ran this command:
```
docker run -d --name mydb --network my-custom-network -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:8
```

After that I need to build the web app image using the command:
```
docker build -t hello-flask-mysql
```

Then to run the container and link it with the MySQL container I need to run the web app on the custom bridge network I made using this:
```
docker run -d --name myapp --network my-custom-network -p 5002:5002 hello-flask-mysql
```


## Output

The output was `Hello, World! MySQL version:8`

## Challenges

The challenge I faced was initially not assigning the --network flag to the MySQL container which meant that the docker engine thought my-custom-network was the name of the image not the name of the network. Another issue I faced was that when trying to build the web app image there was a problem with installing the mysqlclient dependency. So I searched up the error message and included another RUN command to fix this issue.

## What I Learned

In this lab I learned how to create a custom network and connect two containers to the same network.

