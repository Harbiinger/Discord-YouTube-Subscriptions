#!/usr/bin/env python3

from datetime import datetime
from datetime import date
from discord_webhook import DiscordWebhook
import requests
import json
import feedparser
import time

def store(dict):
    with open('channels.json', 'w') as json_file:
        json.dump(dict, json_file)

def add(key, value):
    dict = getDict()
    new_key = ""
    for c in key:
        if c == ' ':
            new_key += '+'
        else:
            new_key += c
    dict[new_key] = value
    store(dict)

def remove(key):
    dict = getDict()
    del dict[key]
    store(dict)

def changeWebhook(wh):
    dict = getDict()
    dict["webHookUrl"] = wh
    store(dict)

def getDict():
    with open('channels.json') as f:
        return json.load(f)
        
def send():
    channelsIds = list(getDict().values())

    actualHour = datetime.utcnow().strftime("%H")
    actualDay = date.today().strftime("%d")

    webhookUrl = channelsIds[0]

    for id in channelsIds[1:]:
        channelFeed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=" + id)
        lastVideo = channelFeed.entries[0]
        lastEntryHour = lastVideo.published[11:13]
        lastEntryDay = lastVideo.published[8:10]

        if lastEntryHour == actualHour and lastEntryDay == actualDay:
            webhook = DiscordWebhook(webhookUrl, content=lastVideo.link)
            response = webhook.execute()

if __name__ == "__main__":
    send()
