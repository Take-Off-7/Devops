variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "domain_name" {
  description = "Domain name for the S3 bucket"
  type        = string
  default     = "devops4all.dev"
}
