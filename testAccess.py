from decouple import config

# Access the secrets
api_token = config("API_KEY")

print(f"API Token: {api_token}")