#Syrik Bot created by Zyronn

#Importing everything that I will need for the bot.
import discord
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


bot.run(token) # run the bot with the token
