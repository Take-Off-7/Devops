output "zone_id" {
  description = "The ID of the created Route53 hosted zone"
  value       = aws_route53_zone.main.zone_id
}

output "name_servers" {
  description = "The name servers assigned to this hosted zone"
  value       = aws_route53_zone.main.name_servers
}
