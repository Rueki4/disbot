import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests


index = -1
intents = discord.Intents.all()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix="'", intents=intents)

@bot.loop(minutes = 1)
async def enviar_mensaje_periodico():
    canal = bot.get_channel("1385816218707038268")
    if canal:
        await canal.send("hola")

@bot.command()
async def info(ctx, nombre : str):
    await ctx.send(nombre)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # global index
    if 'hola' in message.content.lower():

        # url = "https://rule34.xxx/index.php?page=post&s=list&tags=futabu+"
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        # }
        # hentai_list = []
        # resp = requests.get(url, headers=headers)
        # # resp.raise_for_status()  # lanza error si el status ≠ 200
        # soup = BeautifulSoup(resp.text, "html.parser")

        # # Ejemplo: títulos y enlaces de resultados
        # soup_str = str(soup).split("\n")

        # for i in range(len(soup_str)):
        #     # print(soup_str[i])
        #     if "thumbnails" in soup_str[i]:
        #         source = soup_str[i].split('src')[1].split('"')[1]
        #         hentai_list.append(source)
        # index += 1
        await message.channel.send("hola")

    await bot.process_commands(message)

enviar_mensaje_periodico.start()

token_a = "MTM4NTc3NTU2MDA2MzQ1MTIyNw."
token_b = "GzW8GX.6gHVgapzMm8L40X8LQpasXj1wP8iLU7mVRfX50"
bot.run(token_a + token_b)