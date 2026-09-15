import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=637058880a0ca2b57c691d19d06cd788cc034d5d0f378255b54f70bc9b4cb60c")
except requests.RequestException:
    print("error")

response = response.json()
price = float(response.get("data").get("priceUsd"))

amount = price * bitcoins

print(f"${amount:,.4f}")
