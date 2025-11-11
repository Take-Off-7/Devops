variable "domain_name" {
  description = "The domain name for your website."
  type        = string
}

variable "acm_certificate_arn" {
  description = "The ARN of the ACM certificate to use for HTTPS on CloudFront."
  type        = string
}

variable "s3_www_website_endpoint" {
  description = "The S3 website endpoint URL that CloudFront will use as the origin."
  type        = string
}
