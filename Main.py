
import json

import requests

import random

import os

from dotenv import load_dotenv

import discord

class Allah(discord.Client):
    async def on_ready(self):
        print('logged on as ' + str(self.user))
    async def on_message(self, message):
        if(message.content == 'Oh Allah!'):
            Verse = random.randint(1,6236)
            response = requests.get('http://api.alquran.cloud/v1/ayah/'+ str(Verse)+ '/en.asad')
            thingy = response.json()
           
            await message.channel.send( thingy['data']['text'])

load_dotenv('.env')
client = Allah()
client.run(os.getenv('Allah_token')) 