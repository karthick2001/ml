#!/bin/bash

# Variables
AWS_ACCOUNT_ID=<your_aws_account_id>
AWS_REGION=<your_aws_region>
REPOSITORY_NAME=iris-ml-app
IMAGE_TAG=latest
ECR_URI=${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${REPOSITORY_NAME}:${IMAGE_TAG}

# Authenticate Docker to the ECR registry
$(aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_URI})

# Build the Docker image
docker build -t ${REPOSITORY_NAME}:${IMAGE_TAG} .

# Tag the Docker image
docker tag ${REPOSITORY_NAME}:${IMAGE_TAG} ${ECR_URI}

# Push the Docker image to ECR
docker push ${ECR_URI}

echo "Docker image ${ECR_URI} has been pushed to ECR."
