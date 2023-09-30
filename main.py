import discord
import os
from dotenv import load_dotenv


intents = discord.Intents()
intents.members = True
intents.presences = True
intents.message_content = True

bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    print(f"new user {member.name}")
    if bot.get_channel(1145759009127805039) == None:
        channel = await bot.fetch_channel(1145759009127805039)
    else:
        channel = await bot.get_channel(1145759009127805039)
    embed = discord.Embed(
        title=f"Welcome {member.display_name}!",
        description=f"{member.mention} has joined TON.",
        color=2829617       
    )
    await channel.send(embed=embed)



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
        title=f"New Suggestion by {ctx.author}.",
        description=suggestion,
        color=2829617
    )
    channel = await bot.fetch_channel(1145716515006578862)
    msg = await channel.send(embed=embed)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")
    await ctx.respond("Suggestion sent!", ephemeral=True)

@bot.slash_command(description='bot made by calcium', guild_ids=['1144777754894676081'])
async def credits(ctx):
    embed = discord.Embed(
        title="this bot was made by calcium",
        color=2829617,
        description="you can see some of my web development work at https://calcal.space"
    )

    await ctx.respond(embed=embed)

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
