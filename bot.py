
import os
import discord
from dotenv import load_dotenv
import val
from update import MyCog
from players import getPlayers


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    cog = MyCog(client.get_channel(1048693671874285650), getPlayers())
    cog.val_update.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == ("'help"):
        msg = ("'rank username tagline, ex: azusa#ohio")
        embedVar = discord.Embed(description=f"""{msg}""")
        await message.channel.send(embed = embedVar)
    if message.content.startswith("'rank"):
        words = message.content.split()
        words = words[1].split('#')
        user = words[0] 
        tagline = words[1]
        info = val.valrank(user, tagline)
        msg = f"Your current rank is, {info['currenttierpatched']}. The rr change was {info['mmr_change_to_last_game']} rr"
        embedVar = discord.Embed(description=f"""{msg}""")
        await message.channel.send(embed = embedVar)

client.run(TOKEN)