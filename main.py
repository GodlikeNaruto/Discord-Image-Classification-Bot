import discord
from discord.ext import commands
from get_model import classification

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def check(ctx):
    if ctx.message.attachments == []:
        await ctx.send('No file uploaded')
    else:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(file_name)
            await ctx.send('Image uploaded succesfully')
            try:
                await ctx.send(classification(file_name))
            except:
                await ctx.send("Incorrect File type")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTE1MjYwMDQzMDEyNDIxMjI0NA.G2UhSb.qR_Fje4GOPgNap7nfg_xHRhrdR0ATuXMks4PJE")
