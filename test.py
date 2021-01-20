import discord
import asyncio
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

token = "token"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 실행되었습니다.')
    game = discord.Game('봇 실행')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command()
async def 주사위(ctx):
    numbers = ["1", "2", "3", "4", "5", "6"]
    random_choice = random.choice(numbers)
    await ctx.send("나온 값은 {}입니다.".format(random_choice))


client.run(token)
