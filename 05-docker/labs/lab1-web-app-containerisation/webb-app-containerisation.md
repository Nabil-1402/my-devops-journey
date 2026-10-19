# Lab: [Web App Containerisation]

## Objective

Containerise a simple flask web app using a dockerfile.

## Commands Used

To containerise the flask web app, I first had to create a dockerfile. A dockerfile is used to create an image of an application where each command is called a layer. 

```My Dockerfile
FROM python:3.8-slim #base python image
WORKDIR /app #make the container's working directory /app
COPY . . #copy everything from this current directory to the containers working directory (/app)
RUN pip install flask #install flask dependency
EXPOSE 5002 #expose port 5002 so that the applicatiom can be ran on this port
CMD ["python", "app.py"] #start the application using this command
```
Then to build it I used the command: `docker build -t hello-flask .`

After building I need to run my image to create the containe, this was done like so: `docker run -d -p 5002:5002 hello-flask`


## Output

The output for when I built the image was text showing all the layers being built based on what was put inside the docker file. The output for running the image was the container ID. I verified that the container worked by opening the web app on my localhost IP with port 5002 and saw that hello world was displayed without having to actually type in `python3 app.py` in my terminal. 

## Challenges

The challenge I faced in this lab was understanding how to write the appropriate dockerfile and reading error messages for ports already in use. For example initially I tried exposing port 5000 but when I tried building the image, I got an error message saying port 5000 was already in use. This made me realise I had to change the port which I did to 5002.

## What I Learned

In this lab I learned how to write a basic dockerfile. Then take that dockerfile and build an image from it and run it to create a container.

