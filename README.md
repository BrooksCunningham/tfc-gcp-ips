<!-- [![get-and-update-gcp-ips-list](https://github.com/BrooksCunningham/tfc-gcp-ips/actions/workflows/python_cron.yml/badge.svg?branch=main)](https://github.com/BrooksCunningham/tfc-gcp-ips/actions/workflows/python_cron.yml) -->

# tfc-gcp-ips
Terraform GCP IPs

This repo will get the latest GCP ips and update a list with Fastly's Next-Gen WAF. Github actions perform the following tasks: 
* Pull the GCP IP list as a cron
* Update the repo with the latest GCP IPs and use Terraform cloud to update the IP list in Fastly's Next-Gen WAF.

