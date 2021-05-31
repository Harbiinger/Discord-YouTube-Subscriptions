from datetime import date
from discord_webhook import DiscordWebhook
import requests
import json
import feedparser

channels = {}

with open("subscriptions.txt") as f:
    for line in f.readlines():
        name = ""
        id = ""
        next = False
        for c in line:
            if c == '€' or c == '\n':
               next = True 
            elif next:
                id+=c
            else:
                name+=c
        channels[name] = id

today = date.today().strftime("%d")

for ids in channels.values():
    channelFeed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=" + ids)
    lastVideo = channelFeed.entries[0]
    lastEntry_day = lastVideo.published[8:10]

    if lastEntry_day == today:
        webhook_url = 'https://discord.com/api/webhooks/848455244560334858/OqYiHx7C-qVfBedMszvk_tyeiCuG5xIWqjlBeZXnillk8jYoR34pHwabW03vCUrz5Qsq'
        webhook = DiscordWebhook(webhook_url, content=lastVideo.link)
        response = webhook.execute()
