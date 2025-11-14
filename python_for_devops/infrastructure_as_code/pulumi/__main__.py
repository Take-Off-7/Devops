import json
import mimetypes
import os
from pulumi import export, FileAsset
from pulumi_aws import s3

# Create an S3 bucket configured as a website
web_bucket = s3.Bucket(
    "s3-website-bucket",
    website={"index_document": "index.html"}
)

# Directory containing website files
content_dir = "www"

# Upload all files in the directory to the S3 bucket
for file_name in os.listdir(content_dir):
    file_path = os.path.join(content_dir, file_name)
    mime_type, _ = mimetypes.guess_type(file_path)

    s3.BucketObject(
        file_name,
        bucket=web_bucket.id,
        source=FileAsset(file_path),
        content_type=mime_type or "application/octet-stream"
    )

# Function to generate a public-read bucket policy
def public_read_policy_for_bucket(bucket_name):
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": [f"arn:aws:s3:::{bucket_name}/*"]
        }]
    })

# Attach the bucket policy
bucket_policy = s3.BucketPolicy(
    "bucket-policy",
    bucket=web_bucket.id,
    policy=web_bucket.id.apply(public_read_policy_for_bucket)
)

# Export the bucket name and website URL
export("bucket_name", web_bucket.id)
export("website_url", web_bucket.website_endpoint)
