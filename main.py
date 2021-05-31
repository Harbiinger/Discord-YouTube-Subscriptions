#!/usr/bin/env python3

from datetime import date
from discord_webhook import DiscordWebhook
import requests
import json
import feedparser
import time

with open('channels.json') as f:
    channelsDict = json.load(f)
        
channelsIds = list(channelsDict.values())

today = date.today().strftime("%d")

webhookUrl = channelsIds[0]

webhook = DiscordWebhook(webhookUrl, content="___ All new videos of today ___")
response = webhook.execute()

for id in channelsIds[1:]:
    channelFeed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=" + id)
    lastVideo = channelFeed.entries[0]
    lastEntryDay = lastVideo.published[8:10]

    if lastEntryDay == today:
        webhook = DiscordWebhook(webhookUrl, content=lastVideo.link)
        response = webhook.execute()
