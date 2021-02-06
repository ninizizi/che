import discord
from discord.ext import commands
import json
import random

with open('setting.json', 'r', encoding='utf8')as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.event
async def on_message(msg):
    if msg.content == '$che':
        random_chesaid = random.choice(jdata['chesaid'])
        await msg.channel.send(random_chesaid)
    keyword = ['幹','操','你媽死了','屁啦',
    'fuck','雞掰','劉明錕','靠腰','靠邀',
    '三小','雞巴']
    for keywords in keyword:
        if msg.content.endswith(keywords):
            await msg.channel.send('哦!刷牙!')
        elif msg.content.startswith(keywords):
            await msg.channel.send('哦!刷牙!')
        break




bot.run(jdata['token'])    