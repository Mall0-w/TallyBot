import discord
import os
import TallyFunctionality
from KeepAlive import keep_alive

client = discord.Client()
tracker = TallyFunctionality.tally()


@client.event
async def on_ready():
    print("Hi there! Im tallyBot, you can learn more about me by using $thelp")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #await message.channel.send()
    ''''
  if message.content.startswith('$t'):
    await message.channel.send("Hello world!")
  '''
    if (message.content.startswith("$help")):
        await message.channel.send(TallyFunctionality.help)

    if (message.content.startswith("$create")):
        await message.channel.send(tracker.createTally(message.content))

    if (message.content.startswith("$remove")):
        await message.channel.send(tracker.removeTally(message.content))

    if (message.content.startswith("$show")):
        await message.channel.send(tracker.showTally(message.content))

    if (message.content.startswith("$tally")):
        await message.channel.send(tracker.addTally(message.content))
    
    if(message.content.startswith("$list")):
      await message.channel.send(tracker.listTally())


keep_alive()
client.run(os.getenv('Token'))
