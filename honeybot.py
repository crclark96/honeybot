import discord
import requests
import json

TOKEN = json.load(open("secrets.json"))["token"]

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!honey'):
        msg = 'H O N E Y'
        await message.channel.send(msg)

    if message.attachments:
        if message.attachments[0].filename.endswith(".json"):
            url = message.attachments[0].url
            r = requests.get(url, allow_redirects=True)
            await message.channel.send(r.content.decode())


client.run(TOKEN)
