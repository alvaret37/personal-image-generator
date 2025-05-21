import os
import requests
from dotenv import load_dotenv

load_dotenv()

def run_replicate(prompt, image_data):
    token = os.getenv("REPLICATE_API_TOKEN")
    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "version": "ip-adapter-version-id",
        "input": {
            "prompt": prompt,
            "image": image_data
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.content  # apenas exemplo simplificado
