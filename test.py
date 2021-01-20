import discord
import asyncio
import random

client = discord.Client()

token = "token"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 실행되었습니다.')
    game = discord.Game('봇 실행')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith(".주사위"):
        numbers = ["1", "2", "3", "4", "5", "6"]
        random_choice = random.choice(numbers)
        await message.channel.send("나온 값은 {}입니다.".format(random_choice))


client.run(token)
