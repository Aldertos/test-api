import requests

user_id = int(input("Enter target ID: "))
api_url = f"https://discord.com/api/v9/users/{user_id}/profile"
token = "YOUR ACCOUNT TOKEN"


headers = {
  "Authorization": token,
}

response = requests.get(api_url, headers=headers)
print(f"Api isteği: {response.text}")