# Generate random suffix for global uniqueness
resource "random_id" "suffix" {
  byte_length = 4
}

# S3 bucket
resource "aws_s3_bucket" "www" {
  bucket        = "www.${var.domain_name}-${random_id.suffix.hex}"
  force_destroy = true

  # Website configuration directly on the bucket
  website {
    index_document = "index.html"
    error_document = "index.html"
  }
}

# Disable S3 Block Public Access for this bucket so public policy works
resource "aws_s3_bucket_public_access_block" "www" {
  bucket = aws_s3_bucket.www.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# Public read policy for static website
resource "aws_s3_bucket_policy" "www_policy" {
  bucket = aws_s3_bucket.www.id

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::www.${var.domain_name}-${random_id.suffix.hex}/*"
    }
  ]
}
POLICY
}

# Upload all static files
resource "aws_s3_object" "static" {
  for_each = { for f in fileset("${path.root}/static_files", "*") : f => f }

  bucket  = aws_s3_bucket.www.bucket
  key     = each.key
  source  = "${path.root}/static_files/${each.value}"
  content_type = lookup(
    {
      "index.html"     = "text/html",
      "devops4all.jpg" = "image/jpeg"
    },
    each.key,
    "application/octet-stream"
  )
}
