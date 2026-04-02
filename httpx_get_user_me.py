import httpx

login_payload = {
    'email': 'sunner1319@gmail.com',
    'password': 'ill1319'
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
response_data = login_response.json()
token = response_data['token']['accessToken']


headers = {"Authorization": f"Bearer {token}"}
user_response = httpx.get("http://localhost:8000/api/v1/users/me" ,headers=headers)
user_data = user_response.json()
print(user_response.status_code)
print(user_data)