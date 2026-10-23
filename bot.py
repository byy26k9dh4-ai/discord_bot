import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.event
async def on_message_edit(before, after):
    kanal = before.channel
    przed_edycja = before.content
    po_edycji = after.content
    edtowane_przez = before.author
    if przed_edycja != po_edycji:
        await kanal.send(f'Wiadomość została edytowana!\nPrzed edycją: {przed_edycja}\nPo edycji: {po_edycji}\nEdytowana przez: {edtowane_przez}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    if count_heh > 20: 
        await ctx.send("Zbyt dużo heh!")
    else:
        await ctx.send("he" * count_heh)

@bot.command()
async def user_info(ctx, user: discord.Member):
    await ctx.send(f'Informacje o użytkowniku {user.name}:\nID: {user.id}\nDołączył: {user.joined_at}\nUtorzył konto: {user.created_at}')

@bot.command()
async def mem(ctx, category):
    choice = random.choice(os.listdir(f"M2L1/images/{category}"))
    with open(f"M2L1/images/{category}/{choice}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run("TOKEN")

