output "certificate_arn" {
  description = "The ARN of the ACM certificate"
  value       = aws_acm_certificate.certificate.arn
}

## Because with “simplified ACM”, Terraform only creates the certificate, and you manually validate it in Route53.
# output "certificate_arn" {
#   description = "The ARN of the ACM certificate"
#   value       = aws_acm_certificate_validation.certificate_validation.certificate_arn
# }
