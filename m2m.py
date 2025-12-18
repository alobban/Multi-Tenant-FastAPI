import requests


payload = {
    "client_id":"YO7luxuOiITPX2bGO4DohsAFl49qkvIs",
    "client_secret":"ubFIEXk6l5Wt0AHQI_g1EVxseP5y9ocqVANT3Bi4jrwc3mA6bSC2lszQjmDjVheo",
    "audience":"https://prommiseme.com/api/tenants",
    "grant_type":"client_credentials"
  }

response = requests.post("https://dev-lobban876.us.auth0.com/oauth/token", json=payload)

print(response.json())