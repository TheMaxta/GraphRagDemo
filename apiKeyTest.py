import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv('GRAPHRAG_API_KEY')

if not api_key:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable in the .env file.")

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Who won the world series in 2020?"
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("Success!")
    print("Response:", response.json())
else:
    print("Failed with status code:", response.status_code)
    print("Response:", response.text)
