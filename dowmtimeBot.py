#Syrik Bot created by Zyronn

#Importing everything that I will need for the bot.
import discord
import os # default module
import downtimeActivities as downtime

bot = discord.Bot()



@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


bot.run("MTIxMDc0NTI3ODg0NDUwMjA2Ng.GTBFtK.pE09mXlHs51TJWF5hxXL3Wg5msPmGAScgXadyE") # run the bot with the token
