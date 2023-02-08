from discord.ext import commands, tasks
from val import valrank
import discord
class MyCog(commands.Cog):
    def __init__(self, channel, players):
        self.channel = channel
        self.players = players
    @tasks.loop(seconds=60)
    async def val_update(self):
        for person in self.players:
            person[3] = person[2]
            person[2] = valrank(person[0], person[1])
            if person[2]['elo'] != person[3]['elo']:

                if person[2]['elo']//100 > person[3]['elo']//100:
                    msg = f"yipee {person[0]} isnt hardstuck anymore! they went from {person[3]['currenttierpatched']} to {person[2]['currenttierpatched']}!"
                if person[2]['elo']//100 < person[3]['elo']//100:
                    msg = f"common {person[0]} L! they went from {person[3]['currenttierpatched']} to {person[2]['currenttierpatched']}!"
                if person[2]['elo'] > person[3]['elo']:
                    msg = f"yay! {person[0]} gained {person[2]['mmr_change_to_last_game']} rr!"
                if person[2]['elo'] < person[3]['elo']:
                    msg = f"lmao dogwater!!! {person[0]} lost {person[2]['mmr_change_to_last_game']} rr!"
                embedVar = discord.Embed(description=f"""{msg}""")
                await self.channel.send(embed = embedVar)
            