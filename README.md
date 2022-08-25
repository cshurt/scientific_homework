# scientific_homework
A quick presentation/project for a prospective employer.

Work prompt:

>Generally, this evaluation should not take more than six hours to complete but we ask that you return the completed challenge within three days.

## Section 1: Consulting Soft Skills

>A key function of this position is producing or contributing to functional specifications and other written or presentation quality technical documentation. Please provide responses that address the following hypothetical “client concerns”. These responses should illustrate your personal writing style and your ability to provide clients with cogent and technically relevant information.

>What is a Data Lake? Explain its benefits, how it differs from a data warehouse, and how it might benefit a client. 

>Explain serverless architecture.  What are its pros and cons?

>Please provide a diagram for an ETL pipeline (ex: Section 2) using serverless AWS services. Describe each component and its function within the pipeline.

>Describe modern MLOps and how organizations should be approaching management from a tool and system perspective.

Answers to these questions are in soft_skills.md and soft_skills.pptx 

## Section 2: Database & Python ETL

>Provision one database of your choosing (SQL, NoSQL, Graph).  Write a python ETL that ingests the provided data, transforms it in some way, and loads it into the database. This should be reproducible code with documentation. (Terraform / Cloudformation / Ansible, docker-compose etc).

Python ETL in the lambda_function.py file. I'm willing to discuss my Cloudformation approach, but after ~12 hours effort on this overall project I'm unwilling to work it on it further without renumeration. I estimate ~2 hours to define cloudformation files for the SQL database and Lambda function, with up to ~12 hours if including files to define IAM roles, VPNs, and subnets. For best quality code I would also recommend defining a CI/CD pipeline along with unit and integration tests, but that would be a considerable amount of effort.

## Section 3: ML API

>Deploy (on a cloud provider [AWS, Azure, etc] or locally [docker, kubernetes, etc] ) an ML model (MNIST: https://paperswithcode.com/dataset/mnist, Fashion MNIST: https://github.com/zalandoresearch/fashion-mnist), as an API endpoint. Provide reproducible code with documentation for both deployment and usage.

I estimate that this is an additional 6-12 hours of effort, alongside a small out-of-pocket expense for running an active API endpoint. I'd be willing to build out a solution at my consulting rate of $100/hour + expenses.

