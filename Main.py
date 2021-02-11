
import os

from dotenv import load_dotenv

import discord

class Allah(discord.Client):
    async def on_ready(self):
        print('logged on as ' + str(self.user))
    async def on_message(self, message):
        if(message.content == 'Oh Allah!'):
            await message.channel.send('Yes, my child') # WIll change to Qur'An
load_dotenv('.env')
client = Allah()
client.run(os.getenv('Allah_token')) 