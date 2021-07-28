import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

def welcomer(member):

    tag = member.discriminator
    welcome = "Welcome to Forever Alo',"
    tagline = "an unofficial discord server for Alohub users!"
    guidelines = "Please first read and agree to the community guidelines!"
    organizers = "John or Sera"
    NO_GUIDELINES = True
    if NO_GUIDELINES:
        guidelines = "TODO"

    output = f"""{welcome} {tagline} {guidelines} Next, for verification purposes please text code #{tag} to {organizers} and provide your full name and contact info.

If you have been to 2 or more Alohub events then please let one of the moderators know! This way you can be assigned a regular tag and have access to all the available chats :grinning: Anyway, welcome once again and Forever Alo'!"""
    return output.replace(" TODO ", " ")

@client.event
async def on_member_join(member):
    await member.send(welcomer(member))

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        if message.content.startswith('help'):
            await message.channel.send(welcomer(message.author))

client.run(TOKEN)
