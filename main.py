#!/usr/bin/env python3

from datetime import datetime
from datetime import date
from discord_webhook import DiscordWebhook
import requests
import json
import feedparser
import time

def getDict():
    with open('channels.json') as f:
        return json.load(f)
        
def send():
    channelsIds = list(getDict().values())
    ChannelsNames = list(getDict().keys())

    actualHour = datetime.now().strftime("%H")
    actualDay = date.today().strftime("%d")

    webhookUrl = channelsIds[0]

    webhook = DiscordWebhook(webhookUrl, content="___ All new videos of today ___")
    response = webhook.execute()

    for id in channelsIds[1:]:
        channelFeed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=" + id)
        lastVideo = channelFeed.entries[0]
        lastEntryHour = lastVideo.published[11:13]
        lastEntryDay = lastVideo.published[8:10]

        if lastEntryHour == actualHour and lastEntryDay == actualDay:
            webhook = DiscordWebhook(webhookUrl, content=lastVideo.link)
            response = webhook.execute()
