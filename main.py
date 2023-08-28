import interactions

bot = interactions.Client()

@interactions.listen()
async def on_startup():
    print("ready to serve mega cunt!")

@interactions.slash_command(name="hangout", description="you clearly dont understand that ton isnt a hangout...")
async def my_command_function(ctx: interactions.SlashContext):
    embed = interactions.Embed()
    embed.add_image('https://i.vgy.me/2tycpD.png')
    await ctx.send(embed=embed)

@interactions.slash_command(name="shlexhangout", description="you clearly dont understand that sirius isnt a hangout...")
async def my_command_function(ctx: interactions.SlashContext):
    embed = interactions.Embed()
    embed.add_image('https://i.vgy.me/61x9Oy.png')
    await ctx.send(embed=embed)

bot.start("MTE0NTYxNDI0NTM4NDQ0MTg1Nw.GGKkZa.Nfq8TruQ_CMZYk9xxFhe1PEelD8UFEovUxT6vE")