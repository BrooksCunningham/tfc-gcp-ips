# Terraform 0.13.x
terraform {
  required_providers {
    sigsci = {
      source = "signalsciences/sigsci"
    }
  }
}

variable "SIGSCI_TOKEN" {
    type        = string
    description = "This is a secret token for the Sig Sci API as an env variable."
}
variable "SIGSCI_EMAIL" {
    type        = string
    description = "This is the email address associated with the token for the Sig Sci API as an env variable."
}
variable "SIGSCI_CORP" {
    type        = string
    description = "This is the corp where configuration changes will be made as an env variable."
}

variable "GCP_IP_LIST" {
    type        = list
    description = "Used for a list of GCP IPs, https://www.gstatic.com/ipranges/cloud.json"
}

provider "sigsci" {
  corp = "${var.SIGSCI_CORP}"
  email = "${var.SIGSCI_EMAIL}"
  auth_token = "${var.SIGSCI_TOKEN}"
}

resource "sigsci_corp_list" "gcp_ips_list" {
  name        = "GCP IPs list"
  type        = "ip"
  description = "Outbound GCP IPs"
#   entries = "${var.GCP_IP_LIST}"
  entries = ["5.5.5.1","5.5.5.2"]
}
