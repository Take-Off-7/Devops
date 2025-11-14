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
  cloudfront_domain_name = module.cloudfront.domain_name
  cloudfront_zone_id = module.cloudfront.hosted_zone_id
}

# ACM module
module "acm" {
  source      = "./modules/acm"
  domain_name = var.domain_name
  route53_zone_id = module.route53.zone_id
}

# CloudFront module
module "cloudfront" {
  source = "./modules/cloudfront"
  domain_name = var.domain_name
  s3_www_website_endpoint = module.s3.website_endpoint
  acm_certificate_arn = module.acm.certificate_arn
}
