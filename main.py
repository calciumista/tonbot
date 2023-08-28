import discord
import os
from dotenv import load_dotenv


bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")



@bot.slash_command(description='ton is not a hangout!!', guild_ids=['1144777754894676081'])
async def hangout(ctx):
    embed = discord.Embed(
        color=2829617
    )
    embed.set_image(url="https://i.vgy.me/2tycpD.png")
    await ctx.respond(embed=embed)



@bot.slash_command(description='sirius is not a hangout!!!', guild_ids=['1144777754894676081'])
async def shlexhangout(ctx):
    embed = discord.Embed(
        color=2829617
    )
    embed.set_image(url="https://i.vgy.me/61x9Oy.png")
    await ctx.respond(embed=embed)

@bot.slash_command(description='suggest ton features!', guild_ids=['1144777754894676081'])
async def suggest(ctx, suggestion):
    embed = discord.Embed(
        title=f"New Suggestion by {ctx.author}",
        description=suggestion,
        color=2829617
    )
    channel = bot.get_channel(1145716515006578862)
    msg = await channel.send(embed=embed)
    await ctx.send("Suggestion sent!!")
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)