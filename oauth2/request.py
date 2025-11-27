import requests
import json

def get_token(username: str, password: str, client_id: str, resource: str) -> str:
    
    # payload
    payload = {
        "username": username,
        "password": password,
        "client_id": client_id,
        "resource": resource,
        "grant_type": "password",
    }

    # post
    url = "https://api.com/adfs/oauth2/token")
    response = requests.post(url, data=payload)
    token = json.loads(response.content).get('token')

    return token

def run():

    # init token request
    username = "username"
    password = "password"
    client_id = "client_id"
    resource = "resource"
    
    # get token
    token = get_token(username, password, client_id, resources)

    # request
    url = "https://api.com"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers = headers)

if __name__ == "__main__":
    run()
