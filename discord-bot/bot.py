import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} ist online!")

@bot.command()
async def announce(ctx, titel, *, text):
    channel = bot.get_channel(1486452779345117188)

    embed = discord.Embed(
        title=titel,
        description=text
    )

    await channel.send(embed=embed)



bot.run(TOKEN)