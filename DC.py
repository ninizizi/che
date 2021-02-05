import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(f"{member} join!")
    channel = bot.get_channel(725757975301587028)
    await channel.send(f"{member}你他媽怎麼進來了")

@bot.event
async def on_member_remove(member):
    print(f"{member} remove!")

bot.run('ODA3Mjc5MTc2MDc5NzY5Njgw.YB1rUg.aFZ6rR4RIPQL8E1woMQORe_GWcM')    