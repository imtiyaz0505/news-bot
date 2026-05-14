import requests
import time

BOT_TOKEN = '8834841549:AAFqk3_3pQmIC10ilNl3xPEEM_4DO1lMNig'
CHAT_ID = '8675837070'
NEWS_API_KEY = '670d24647892494ba8a00e7183bf6cd3'

r = requests.get("https://newsapi.org/v2/top-headlines", params={"category":"general","language":"en","pageSize":1,"apiKey":NEWS_API_KEY})
d = r.json()
title = d["articles"][0]["title"]
desc = d["articles"][0].get("description","")
source = d["articles"][0].get("source",{}).get("name","")

article = f"""BREAKING NEWS: {title}

Source: {source}

{desc}

This is a developing story. Stay tuned for more updates on this breaking news. The situation continues to evolve as more information becomes available from reliable sources around the world.

Key Points:
- {title}
- Source: {source}
- Stay updated for more details

Follow our blog for the latest world news updates."""

requests.post("https://api.telegram.org/bot"+BOT_TOKEN+"/sendMessage", json={"chat_id":CHAT_ID,"text":article})
print("Sent!")
time.sleep(600)
