output "bucket_name" {
  description = "The name of the S3 bucket"
  value       = aws_s3_bucket.www.bucket
}

output "website_endpoint" {
  description = "The website endpoint URL for the bucket"
  value       = aws_s3_bucket.www.bucket_regional_domain_name
}
