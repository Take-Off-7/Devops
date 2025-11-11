# AWS provider
provider "aws" {
  region = var.aws_region
}

# S3 module
module "s3" {
  source      = "./modules/s3"
  domain_name = var.domain_name
}

# Route 53 module
module "route53" {
  source      = "./modules/route53"
  domain_name = var.domain_name
}

# ACM module
module "acm" {
  source      = "./modules/acm"
  domain_name = var.domain_name
  route53_zone_id = module.route53.zone_id
}
