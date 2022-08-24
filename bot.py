import discord #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos
import datetime 
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
LEWAN_IMG = os.getenv('LEWANDOWSKI_IMG')
PEDRI_IMG = os.getenv('PEDRI_IMG')



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='_', description="this is a testing bot", intents=intents)


#Ping-pong
@bot.command()
async def pingo(ctx):
     await ctx.send('pong')

@bot.command()
async def hola(ctx):
    await ctx.send('Hola soy el bot Bernardo Silva, Eu jogo no Barça sou meio-campista salva você entende')

@bot.command(pass_context=True)
async def quienSoy(ctx):
    usuario = ctx.message.author
    # Formatea el texto en donde 0=usuario y "mention" es la mención a este
    await ctx.send(usuario )

@bot.command(pass_context=True)
async def algo(ctx, texto : str):
    usuario = ctx.message.author
    await ctx.send(usuario )
    await ctx.send(texto)

@bot.command(pass_context=True)
async def info(ctx):
    usuario = ctx.message.author
    # Formatea el texto en donde 0=usuario y "mention" es la mención a este
    await ctx.send(usuario)
    await ctx.send("Este bot a sido creado por @CoderAnchel")
    await ctx.send("Mi funcionalidad es basicamente nula no se que hacer pero ahora mismo te puedo decir estadisticas de la plantilla del barça acontinuacion te dejo una lista de comandos que puedes invocar:")
    await ctx.send("_Pedri, _Lewandowski _Algo(mas cualquier texto con espacio despues de algo) _quienSoy _hola _pingo")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="_help"))
    print('My bot is ready')
    
    
#Pedri
@bot.command()
async def pedri(ctx):
    usuario = ctx.message.author
    await ctx.send(usuario )
    await ctx.send("Estos datos son de todas las temporadas")
    await ctx.send(PEDRI_IMG)
    await ctx.send('numero: 8, nacionalidad: 🇪🇸, goles: 9, asistencias: 7, partidos: 76' )
    
@bot.command()
async def Pedri(ctx):
    usuario = ctx.message.author
    await ctx.send(usuario )
    await ctx.send("Estos datos son de todas las temporadas")
    await ctx.send(PEDRI_IMG)
    await ctx.send('numero: 8, nacionalidad: 🇪🇸, goles: 9, asistencias: 7, partidos: 76' )
    
    
#Lewandowski
@bot.command()
async def Lewandowski(ctx):
    usuario = ctx.message.author
    await ctx.send(usuario )
    await ctx.send("Estos datos son de todas las temporadas")
    await ctx.send(LEWAN_IMG)
    await ctx.send('numero: 9, nacionalidad: 🇵🇱,  goles: 2, asistencias: 0, partidos: 2')
    
@bot.command()
async def lewandowski(ctx):
    usuario = ctx.message.author
    await ctx.send(usuario )
    await ctx.send("Estos datos son de todas las temporadas")
    await ctx.send(LEWAN_IMG)
    await ctx.send('numero: 9, nacionalidad: 🇵🇱,  goles: 2, asistencias: 0, partidos: 2')
    
bot.run(TOKEN)
