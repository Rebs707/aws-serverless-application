**AWS Serverless Application**

**Project Overview**

Serverless application architecture built using AWS managed services. This project demonstrates how to design scalable, event-driven applications without managing underlying infrastructure.

**Project Goal**

Build a serverless application using AWS Lambda, API Gateway, and DynamoDB to demonstrate modern cloud-native application development.

**Architecture**

```text
Client
  │
  ▼
API Gateway
  │
  ▼
AWS Lambda
  │
  ▼
Amazon DynamoDB
  │
  ▼
CloudWatch Logs
```

**Technologies**

* AWS Lambda
* API Gateway
* Amazon DynamoDB
* Amazon CloudWatch
* Python

**Features**

* Serverless API design
* Lambda-based compute
* DynamoDB integration
* CloudWatch monitoring
* Event-driven architecture

**Project Structure**

```text
lambda/
api-gateway/
dynamodb/
iam/
diagrams/
screenshots/
```

**Key Learnings**

* Serverless application architecture
* AWS Lambda development
* API Gateway integration
* DynamoDB operations
* CloudWatch monitoring
* Event-driven application design

**Status**

✅ Completed

**Future Improvements**

* Implement Infrastructure as Code using Terraform
* Add a CI/CD deployment pipeline
* Implement API authentication
* Add monitoring dashboards
