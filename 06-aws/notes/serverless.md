# Notes

# Serverless

## Key Concepts

- **Serverless** — The cloud provider provisions and manages the underlying servers so developers can focus on their application code and configuration.
- **Function as a Service (FaaS)** — A serverless compute model where individual functions run on demand. AWS Lambda is an example.
- **Event-driven execution** — An event, such as an API request, an S3 upload or an SQS message, can trigger a Lambda function.
- **Automatic scaling** — Lambda adjusts the number of concurrent executions as demand changes, subject to service limits.
- **Usage-based pricing** — On-demand Lambda pricing is primarily based on requests and compute duration. Other serverless services have their own pricing models.

## What I Learned

- I learned that serverless covers more than functions. It also includes services for databases, storage, messaging and running containers.
- I understand when I might choose Lambda over EC2. I could use Lambda to process a file when it is uploaded and EC2 for an application that needs an always-running server or more control over the operating system.
- I learned how AWS services can work together. API Gateway can receive an HTTP request, invoke a Lambda function and return the response after the function reads data from DynamoDB.
- I learned that increasing a Lambda function’s memory also gives it more CPU resources, and that I can package a function as a container image when it has more complex dependencies.

## Your Notes

### What's Serverless

Serverless is a cloud computing model where the provider manages the underlying servers. Developers deploy their code and configure the services their application needs without provisioning or maintaining the servers themselves.

In AWS, **Lambda** runs functions in response to events. This is known as **Function as a Service (FaaS)**. You write individual functions and configure when they should run. With on-demand Lambda, AWS charges primarily for requests and compute duration.

Serverless also includes managed services for databases, message queues and storage. The underlying servers still exist, and the cloud provider handles their provisioning and maintenance.

### Serverless in AWS

- **AWS Lambda** — Runs code in response to events without requiring you to manage servers.
- **Amazon DynamoDB** — A fully managed NoSQL database that can scale capacity as demand changes.
- **Amazon Cognito** — Handles user sign-up, sign-in and authentication for applications.
- **Amazon API Gateway** — Creates and manages APIs that route requests to Lambda functions or other backend services.
- **Amazon S3** — Provides object storage for files and static assets.
- **Amazon SNS and Amazon SQS** — SNS publishes notifications to subscribers. SQS queues messages so consumers can process them independently.
- **Amazon Data Firehose** — Delivers streaming data to destinations such as Amazon S3 for storage and analysis.
- **Amazon Aurora Serverless** — Automatically adjusts compute capacity for an Aurora relational database based on demand.
- **AWS Step Functions** — Coordinates and monitors workflows that use Lambda functions and other AWS services.
- **AWS Fargate** — Runs containers with Amazon ECS or Amazon EKS without requiring you to manage the underlying servers.

### Why AWS Lambda

| Aspect | Amazon EC2 | AWS Lambda |
| --- | --- | --- |
| Compute model | Virtual machine with CPU and RAM determined by the instance type. | Managed function with configurable memory and proportional CPU allocation. |
| Execution | An instance can run continuously until it is stopped or terminated. | A function runs when invoked. On-demand Event Functions can run for up to 30 minutes. |
| Scaling | You can add or remove instances manually or configure EC2 Auto Scaling. | Lambda automatically scales concurrent executions within its limits. |
| Pricing | A running instance incurs compute charges even when idle. | On-demand compute charges are based on requests and execution duration. |

[AWS announcement on the 30-minute timeout](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-30-minute-ondemand-event-functions/)

### Benefits of AWS Lambda

- **Usage-based pricing** — On-demand pricing is primarily based on the number of requests and how long the code runs, with the configured memory affecting the compute rate.
- **AWS integrations** — Works with services such as API Gateway, S3 and SQS.
- **Language support** — Supports several languages through managed runtimes and others through custom runtimes.
- **Monitoring** — Amazon CloudWatch provides logs and metrics such as invocation count, duration and errors.
- **Configurable resources** — You can increase a function's memory allocation to give it more CPU capacity, which can improve performance for compute-intensive workloads.

### AWS Lambda Language Support

Lambda supports several languages and runtimes, including:

- **Node.js** for JavaScript
- **Python**
- **Java**
- **.NET** for C# and PowerShell
- **Ruby**
- **Custom runtimes** for languages such as Rust and Go

You can also deploy a Lambda function as a **container image**, which is useful when your application has complex dependencies. The image must include a runtime interface client that communicates with the **Lambda Runtime API**. For general-purpose container workloads, you can run standard container images on Amazon ECS with AWS Fargate.