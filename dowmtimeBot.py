#Syrik Bot created by Zyronn

#Importing everything that I will need for the bot.
import discord
from discord.ui import Button, View
import os # default module
import downtimeActivities as downtime

#Gotta protect my token
import dotenv
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

bot = discord.Bot()



@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "adventure", description = "Onwards TO ADVENTURE~!")
async def adventure(ctx,charactername: discord.Option(str), days: discord.Option(int), level: discord.Option(int), region: discord.Option(str), settlement: discord.Option(str)):
    textOutput = downtime.adventure(charactername, days, level, region, settlement)
    await ctx.respond(f"=======================\n{textOutput}\n=======================\n")

@bot.slash_command(name = "alibi", description = "Lying? On the internet?!")
async def alibi(ctx,charactername: discord.Option(str), days: discord.Option(int), deceptionmod: discord.Option(int)):
    textOutput = downtime.alibi(charactername, days, deceptionmod)
    await ctx.respond(f"=======================\n{textOutput}\n=======================\n")

@bot.slash_command(name = "pitfighting", description = "Welcome to the pits")
async def pitfighting(ctx, charactername: discord.Option(str), days: discord.Option(int), goldbet: discord.Option(int)):
    acroDC, athlDC, tactDC = downtime.pitFighting()

    
    zero = Button(label="", style=discord.ButtonStyle.gray, emoji="0️⃣")
    one = Button(label="", style=discord.ButtonStyle.gray, emoji="1️⃣")
    two = Button(label="", style=discord.ButtonStyle.gray, emoji="2️⃣")
    three = Button(label="", style=discord.ButtonStyle.gray, emoji="3️⃣")
    view = View(zero, one, two, three)

    
    async def button_callback0(interaction):
        textOutput = downtime.pitFightingResults(charactername, days, goldbet, 0)
        await interaction.response.edit_message(content=f"=======================\nThe acrobatics DC is {acroDC}\nThe acrobatics DC is {athlDC}\nThe acrobatics DC is {tactDC}\n=======================\n{charactername} lost all 3 rounds. \n{textOutput}=======================\n", view=None)
    async def button_callback1(interaction):
        textOutput = downtime.pitFightingResults(charactername, days, goldbet, 1)
        await interaction.response.edit_message(content=f"=======================\nThe acrobatics DC is {acroDC}\nThe acrobatics DC is {athlDC}\nThe acrobatics DC is {tactDC}\n=======================\n{charactername} won 1 round. \n{textOutput}=======================\n", view=None)
    async def button_callback2(interaction):
        textOutput = downtime.pitFightingResults(charactername, days, goldbet, 2)
        await interaction.response.edit_message(content=f"=======================\nThe acrobatics DC is {acroDC}\nThe acrobatics DC is {athlDC}\nThe acrobatics DC is {tactDC}\n=======================\n{charactername} won 2 rounds. \n{textOutput}=======================\n", view=None)
    async def button_callback3(interaction):
        textOutput = downtime.pitFightingResults(charactername, days, goldbet, 3)
        await interaction.response.edit_message(content=f"=======================\nThe acrobatics DC is {acroDC}\nThe acrobatics DC is {athlDC}\nThe acrobatics DC is {tactDC}\n=======================\n{charactername} won all 3 rounds. \n{textOutput}=======================\n", view=None)
        

    zero.callback = button_callback0
    one.callback = button_callback1
    two.callback = button_callback2
    three.callback = button_callback3
    

    await ctx.respond(f"=======================\nThe acrobatics DC is {acroDC}\nThe acrobatics DC is {athlDC}\nThe acrobatics DC is {tactDC}\n=======================\nHow many did they win?", view=view)

@bot.slash_command(name = "basicframework", description = "Doesn't do anything but is used to add new stuff.")
async def basicframwork(ctx, input1: discord.Option(int)):
    await ctx.respond("Output text!")


bot.run(token) # run the bot with the token
