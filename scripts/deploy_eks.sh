#!/bin/bash

# Variables
AWS_REGION=<your_aws_region>
EKS_CLUSTER_NAME=<your_eks_cluster_name>
ECR_URI=<your_ecr_repository_uri>

# Update kubeconfig to use the EKS cluster
aws eks update-kubeconfig --region ${AWS_REGION} --name ${EKS_CLUSTER_NAME}

# Apply Kubernetes deployment and service configuration
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# (Optional) If you have Helm charts or other deployment methods, include them here

echo "Deployment to EKS cluster ${EKS_CLUSTER_NAME} is complete."
