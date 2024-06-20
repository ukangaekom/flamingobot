import requests


message = requests.get("https://api.telegram.org/bot/7044426031:AAEQXanUICgzCPa_cHdVbG7bDpEz204wIQ")

print(message.status_code)