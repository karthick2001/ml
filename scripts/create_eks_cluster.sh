#!/bin/bash

# Variables
AWS_REGION=<your_aws_region>
EKS_CLUSTER_NAME=<your_eks_cluster_name>
NODE_ROLE_ARN=<your_iam_role_arn_for_nodes>
VPC_ID=<your_vpc_id>
SUBNET_IDS=<your_subnet_ids_comma_separated>

# Create the EKS cluster
aws eks create-cluster \
    --region ${AWS_REGION} \
    --name ${EKS_CLUSTER_NAME} \
    --role-arn ${NODE_ROLE_ARN} \
    --resources-vpc-config subnetIds=${SUBNET_IDS},vpcId=${VPC_ID}

# (Optional) Wait for the cluster to become active
echo "Waiting for the EKS cluster to become active..."
aws eks wait cluster-active --region ${AWS_REGION} --name ${EKS_CLUSTER_NAME}

echo "EKS cluster ${EKS_CLUSTER_NAME} has been created."
