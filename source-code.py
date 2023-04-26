import discord

from discord.ext import commands

import os

#Prefixo

bot = commands.Bot(command_prefix="/")

#Prefixo

#Teste [Inicio]

@bot.event

async def on_ready():

  await bot.change_presence(activity=discord.Game(name="By: RyaN:)")) #Status

  print(f'Tamo logado como {bot.user}!')

#Teste [Fim]

#Mensagem de Boas Vindas [Inicio]

@bot.event

async def on_member_join(member):

  guild = bot.get_guild(1036062752025878579)

  channel = guild.get_channel(1036100377579360337)

  emb = discord.Embed(title="NEW MEMBER",description=f"Thanks {member.name} for joining!")

  await channel.send(member.mention, embed=emb)

#Mensagem de Boas Vindas [Fim]

#Comando Slash Embed [Inicio]

@bot.slash_command(description = "Te envia informações.")

async def info(ctx):

	embed1 = discord.Embed(    title = f'Olá, {ctx.author.display_name}{os.linesep}Sou um bot em fase de teste, use /comandos para ver meus comandos.{os.linesep}{os.linesep}**Contato: <@540870972392079362>**',

    colour = 6950317

	)

	embed1.set_author(name= 'Informações', icon_url='https://pa1.narvii.com/6213/57dd83feacd8e68f3d78488b2273bce1d0d6852d_hq.gif')

	await ctx.send(embed = embed1,delete_after=22)

#Comando Slash Embed [Fim]

#Comando Slash - Principal [Inicio]

@bot.slash_command(guild_ids =[1036062752025878579],description = "Pinga o BOT para teste")

async def on(ctx):

  await ctx.send(f'`Hello World!` `O meu ping é de: >0.08383316499930515ms.<`{os.linesep}{os.linesep}**Criador:  <@540870972392079362>**')

#####

#Comandos - Soma [2] Início

@bot.command()

async def soma(ctx, a: int, b: int):

    await ctx.send(a + b)

#Comamdos - Soma [2] Fim

#Comando Slash - Principal [Fim]

  

#Comandos Slash - Geral [Inicio]

#Slash Ajuda [0] Inicio

@bot.slash_command()

async def comandos(ctx):

  await ctx.send(f"""**Olá, {ctx.author.display_name} esses são meus comandos:**

```>1° On: Para testar se estou funcionando.

>2° Saudação: Irei te enviar uma saudação.

>3° Echo: Irei repetir exatamente o que você disse.

>4° Soma: Irei somar dois números para você.```""")

#Slash Ajuda [0] Fim

#Comandos Slash - Geral [Fim]

#Comandos Gerais [Início]

#Comandos - Segredo [0] Início

@bot.command()

async def s3cret(ctx):

  await ctx.send(f"Oi, {ctx.author.display_name} Você descobriu um segredo! ;)",delete_after=3)

#Comandos - Online [0] Fim

#Comandos - Eco [1] Início

@bot.command()

async def echo(ctx, *args):

    argumentos = ', '.join(args)

    await ctx.send(f'{len(args)} argumentos: {argumentos}')

#Comandos - Eco [1] Fim

#Comandos Gerais [Fim]

#Token

my_secret = os.environ['TOKEN']

bot.run(my_secret)

#Token
