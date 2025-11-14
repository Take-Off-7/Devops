resource "aws_route53_zone" "main" {
  name    = var.domain_name
  comment = "Managed by Terraform"
}

resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.main.zone_id  # <- reference the created hosted zone
  name    = "www.${var.domain_name}"
  type    = "A"

  alias {
    name                   = var.cloudfront_domain_name
    zone_id                = var.cloudfront_zone_id
    evaluate_target_health = false
  }
}
