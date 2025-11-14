variable "domain_name" {
  description = "The domain name to create a Route53 hosted zone for"
  type        = string
}

variable "cloudfront_domain_name" {
  description = "The CloudFront distribution domain name for the www alias"
  type        = string
}

variable "cloudfront_zone_id" {
  description = "The CloudFront hosted zone ID for alias records"
  type        = string
}