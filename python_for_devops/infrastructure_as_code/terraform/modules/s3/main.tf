# Generate random suffix for global uniqueness
resource "random_id" "suffix" {
  byte_length = 4
}

# S3 bucket
resource "aws_s3_bucket" "www" {
  bucket = "www.${var.domain_name}-${random_id.suffix.hex}"
}

# Bucket policy for public read
resource "aws_s3_bucket_policy" "www_policy" {
  bucket = aws_s3_bucket.www.id

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AddPerm",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::www.${var.domain_name}-${random_id.suffix.hex}/*"]
    }
  ]
}
POLICY
}

# Website configuration
resource "aws_s3_bucket_website_configuration" "www" {
  bucket = aws_s3_bucket.www.id

  index_document {
    suffix = "index.html"
  }
}
