
import math

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
            verse = random.randint(1,6236)
            response = requests.get('http://api.alquran.cloud/v1/ayah/'+ str(verse)+ '/en.asad')
            thingy = response.json()

            startindex = 0
            endindex = 399

            for i in range(0, math.ceil(len(thingy['data']['text']) / 400)):
                bed = discord.Embed(title = '\u200b', url = 'https://alquran.cloud/api', description = '\u200b')
                if i == 0:
                    bed.title = 'Ayah '+ str(verse)
                bed.description = thingy['data']['text'][startindex:endindex]
                startindex += 400
                endindex += 400

                await message.channel.send(embed=bed)

            response = requests.get('http://api.alquran.cloud/v1/ayah/'+ str(verse))
            thingy = response.json()

            startindex = 0
            endindex = 399

            for i in range(0, math.ceil(len(thingy['data']['text']) / 400)):
                bed = discord.Embed(title = '\u200b', url = 'https://alquran.cloud/api', description = '\u200b')
                
            if i == 0:
                bed.title = ' الآية'+ str(verse)
                
                bed.description = thingy['data']['text'][startindex:endindex]
                startindex += 400
                endindex += 400

                await message.channel.send(embed=bed)


load_dotenv('.env')
client = Allah()
client.run(os.getenv('Allah_token')) 