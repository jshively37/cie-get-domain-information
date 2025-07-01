from dotenv import load_dotenv
import os
import requests

BASE_AUTH_URL = "https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token"
BASE_URL = "https://api.sase.paloaltonetworks.com/cie/directory-sync/v1/"

HEADERS = {
    "Accept": "application/json",
}

AUTH_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
}

load_dotenv()
TSG_ID = os.environ.get("TSG_ID")
CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET_ID = os.environ.get("SECRET_ID")


def create_token():
    """Function that handles authenticating to Prisma Access and retrieving the token."""
    auth_url = f"{BASE_AUTH_URL}?grant_type=client_credentials&scope:tsg_id:{TSG_ID}"

    token = requests.request(
        method="POST",
        url=auth_url,
        headers=AUTH_HEADERS,
        auth=(CLIENT_ID, SECRET_ID),
    ).json()
    HEADERS.update({"Authorization": f'Bearer {token["access_token"]}'})


def get_cie_domains():
    url = BASE_URL + "domains"
    return requests.request(method="GET", url=url, headers=HEADERS).json()


if __name__ == "__main__":
    create_token()
    domains = get_cie_domains()
    for domain in domains["result"]:
        print(domain["domain"], domain["count"])
