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
    tagline = 'an unoffical chat page for friends who use Alohub'
    hello = f'Hi, it\'s Forever Alo\', {tagline}'

    organizers = 'John or Sera'
    tag = member.discriminator
    name_type = 'your first, last name, and contact info'
    friend_condition = f'who already knows {name_type}'
    ask = f'Please text the code #{tag} to a friend ({organizers}) {friend_condition}'

    task_1 = 'been to 2+ public events'
    task_2 = 'agreed to our community guidelines'
    tasks = f'you\'ve {task_1} and {task_2}'

    whom = 'other regulars with confirmed full names'
    perks = f'you can message in hidden chats with {whom}'
    goal = 'we can make you "a regular" on Forever Alo\''

    return f'{hello}! {ask}.\n\nIf {tasks}, then {goal}. After that, {perks}.';

@client.event
async def on_member_join(member):
    await member.send(welcomer(member));

client.run(TOKEN)
