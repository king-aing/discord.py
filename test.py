# 사용할 모듈들
import discord
import asyncio
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.') # 봇의 접두사

token = "token" # 봇의 토큰

@client.event
async def on_ready(): # 봇이 준비되면

    print(client.user.name) # 봇의 이름을 콘솔창에 프린트하고
    print('성공적으로 봇이 실행되었습니다.') # '성공적으로 봇이 실행되었습니다.'를 콘솔창에 프린트
    game = discord.Game('봇 실행') # 디스코드 봇 활동명 변수
    await client.change_presence(status=discord.Status.online, activity=game) # 봇의 활동을 '봇 실행'으로 하고, 스탯을 온라인으로 함

@client.command()
async def 주사위(ctx): # .주사위라는 명령어를 치면
    numbers = ["1", "2", "3", "4", "5", "6"] # numbers 라는 리스트에서
    random_choice = random.choice(numbers) # random 모듈을 이용해 숫자 하나를 결정해서
    await ctx.send("나온 값은 {}입니다.".format(random_choice)) # 명령어를 입력한 채널에 나온 값이 몇인지 출력


client.run(token)
