from github import Github
from os import environ

def main():

    def get_gcp_ips_list():
        import requests
        resp = requests.get('https://www.gstatic.com/ipranges/cloud.json')
        json_response = resp.json()

        ip_prefixes = json_response["prefixes"]

        gcp_ip_address_ranges = "["

        for ip_prefix in ip_prefixes:
            if "ipv4Prefix" in ip_prefix:
                gcp_ip_address_ranges = gcp_ip_address_ranges + '\"' + ip_prefix["ipv4Prefix"] + '\",'
                # gcp_ip_address_ranges.append(ip_prefix["ipv4Prefix"])
            if "ipv6Prefix" in ip_prefix:
                gcp_ip_address_ranges = gcp_ip_address_ranges + '\"' + ip_prefix["ipv6Prefix"] + '\",'
                # gcp_ip_address_ranges.append(ip_prefix["ipv6Prefix"])

        gcp_ip_address_ranges = gcp_ip_address_ranges + "]"

        return gcp_ip_address_ranges


    def compare_local_and_github_gcp_ip_list(gcp_list, github_list):
        # print(gcp_list, github_list)
        if gcp_list == github_list:
            return True
        else:
            return False

    # First create a Github instance:
    # using a personal access token
    github_access_token = environ.get("GH_ACCESS_TOKEN")
    g = Github(github_access_token)

    # Get the repo
    repo = g.get_repo("BrooksCunningham/tfc-gcp-ips")

    # Get file in github
    gcp_ips_file_contents = repo.get_contents("main.auto.tfvars")

    tf_var_formatted_gcp_ip_list = "GCP_IP_LIST = " + get_gcp_ips_list() + "\n\n"
    github_gcp_ips_file_contents_decoded = gcp_ips_file_contents.decoded_content.decode()

    gcp_ip_list_compare = compare_local_and_github_gcp_ip_list(tf_var_formatted_gcp_ip_list, github_gcp_ips_file_contents_decoded)

    if gcp_ip_list_compare:
        pass
        return "List update: False"
    else:
        repo.update_file(gcp_ips_file_contents.path, "automated gcp_ips_list update", tf_var_formatted_gcp_ip_list, gcp_ips_file_contents.sha, branch="main")
        return "List update: True"

print(main())
