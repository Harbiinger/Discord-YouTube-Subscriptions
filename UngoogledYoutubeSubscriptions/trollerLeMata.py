from datetime import date
from discord_webhook import DiscordWebhook
import requests
import json
import feedparser
from termcolor import colored

webhook_url = "https://discord.com/api/webhooks/848610452916404275/Zb2bwDibaHC8V9TGo5xXEbOKEUtV2Bfia_7V5XGGWo17yjmprE1Ec35Xo072riIPGZw9"
while True:
    print(colored(">>>", 'red'), end="")
    s = input()
    webhook = DiscordWebhook(webhook_url, content=s)
    response = webhook.execute()
