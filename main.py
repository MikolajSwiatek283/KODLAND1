from random import randint
import discord
from bot_logic import *
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def Cześć(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def hehe(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def rzut_monetą(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def emotka(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def liczba(ctx):
    await ctx.send(random.randint(1, 10))

bot.run('MTIwOTE4OTA1NDk0NDY0OTM1OQ.GGxlH8.p6_yRBziiY0rF1zQ3DSLHTTyH4YEFSXiqBrYuU')
