# Labs

# Lab: Create an EC2 Instance to Host a Web Server Using User Data

## Objective

Spin up an EC2 instance and use User Data to create a web server within the instance.

## Commands Used

To complete this task, I first created an EC2 instance. At the end of the configuration stage, I opened the advanced settings and scrolled down to the **User Data** section, where I entered the following Bash script:

```bash
#!/bin/bash

yum update -y
yum install -y httpd

systemctl start httpd
systemctl enable httpd

echo "<h1>Hello CoderCo from $(hostname -f)</h1>" > /var/www/html/index.html
```

Additionally, in the instance's network settings, I allowed **HTTP traffic** so I could access the web server.

## Output

After launching the instance, I went to its details page and copied its **public IPv4 address**. I then entered `http://16.60.10.235` into my browser.

This displayed a web page with the following heading:

```text
Hello CoderCo from ip-172-31-23-169.eu-west-2.compute.internal
```

This matches the output specified in the User Data script.

![EC2 web server output](<screenshots/Screenshot 2026-10-31 at 10.33.50.png>)

## What I Learned

In this lab, I learned how to combine my Bash scripting skills with my AWS knowledge to launch an EC2 instance and use User Data to set up a web server automatically.