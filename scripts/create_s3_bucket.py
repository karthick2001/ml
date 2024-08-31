# scripts/create_s3_bucket.py

import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region=None):
    """
    Create an S3 bucket in a specified region.
    
    Args:
    bucket_name (str): The name of the bucket.
    region (str): The AWS region where the bucket will be created. If None, the default region is used.
    """
    s3 = boto3.client('s3', region_name=region)
    
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                }
            )
        print(f"Bucket {bucket_name} created successfully.")
    except ClientError as e:
        print(f"Error creating bucket: {e}")

if __name__ == "__main__":
    BUCKET_NAME = '<your_s3_bucket_name>'
    REGION = '<your_aws_region>'  # Optional: specify the region or set to None for the default region

    create_s3_bucket(BUCKET_NAME, REGION)
