variable "domain_name" {
  description = "The root domain for the wildcard certificate (e.g., devops4all.dev)"
  type        = string
}

variable "route53_zone_id" {
  description = "The Route 53 hosted zone ID for the domain"
  type        = string
}
