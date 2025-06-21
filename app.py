import discord
from discord.ext import commands, tasks
import threading
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from bs4 import BeautifulSoup
import requests
import funciones
import os


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

# 2) Arranca el servidor en un hilo aparte
def start_health_server():
    port = int(os.environ.get('PORT', 8080))
    server = ThreadingHTTPServer(('0.0.0.0', port), HealthHandler)
    server.serve_forever()

if __name__ == '__main__':
    # Inicia el health-check server
    threading.Thread(target=start_health_server, daemon=True).start()
    index = -1
    intents = discord.Intents.all()
    intents.messages = True
    intents.members = True

    bot = commands.Bot(command_prefix="'", intents=intents)

    lista_auto = []

    @bot.event
    async def on_ready():
        print(f"Conectado como {bot.user}")
        lista_automatica.start() 

    @tasks.loop(minutes = 1)
    async def lista_automatica():
        for i in range(len(lista_auto)):
            content = ":("
            intentos = 0
            while content == "" and intentos < 3:
                content, canal_id = lista_auto[i]()
                intentos += 1
            canal = bot.get_channel(canal_id)
            if canal:
                await canal.send(content)

    @bot.command()
    async def randomrule(ctx, tag : str = "", score : int = 0):
        global lista_auto
        lista_auto.append(funciones.crear_randomizador(tag, ctx.channel.id, score))

    @bot.command()
    async def rule(ctx, tag : str, score : int = 0):

        await ctx.send(funciones.random_de(tag, ctx.channel.id, score))

    @bot.command()
    async def info(ctx):
        await ctx.send('A bot just for u ♥, By Rueki')

    @bot.command()
    async def intento(ctx, nombre : str):
        await ctx.send(nombre)

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if 'jarracamalachu' in message.content.lower():

            url = "https://rule34.xxx/index.php?page=post&s=list&tags=futabu+"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
            hentai_list = []
            resp = requests.get(url, headers=headers)
            # resp.raise_for_status()  # lanza error si el status ≠ 200
            soup = BeautifulSoup(resp.text, "html.parser")

            # Ejemplo: títulos y enlaces de resultados
            soup_str = str(soup).split("\n")

            for i in range(len(soup_str)):
                print(soup_str[i])
                if "thumbnails" in soup_str[i]:
                    source = soup_str[i].split('src')[1].split('"')[1]
                    hentai_list.append(source)
            index += 1
            await message.channel.send("hola")

        await bot.process_commands(message)

    token_a = "MTM4NTc3NTU2MDA2MzQ1MTIyNw."
    token_b = "GzW8GX.6gHVgapzMm8L40X8LQpasXj1wP8iLU7mVRfX50"
    bot.run(token_a + token_b)