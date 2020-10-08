import discord
from time import sleep
import os
import pydub
from pydub import AudioSegment
import subprocess
import time
import pickle

client = discord.Client()

pog_count = pickle.load(open("pog_file.p", "rb"))

print("Pogbot online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    time.sleep(0.25)

    author_id = message.author.mention

    author_id = message.author.mention.replace('!', '')

    if("pog" in message.content.lower() or "p0g" in message.content.lower() or "роg" in message.content.lower()):
        if not author_id in pog_count.keys():
            pog_count[author_id] = 1
        else:
            pog_count[author_id] += 1
        print(pog_count)
        pickle.dump(pog_count, open("pog_file.p", "wb"))
        if  pog_count[author_id] % 10 ==0:
            await message.channel.send("You have pogged " + str(pog_count[author_id]) + " times, " + author_id + ". Please stop.")        

    if message.content[0] == '&':
        if message.content[1::] == "poggiest":
            highest = max(pog_count, key=pog_count.get)
            await message.channel.send(highest + " has pogged the most with a total of " + str(pog_count[highest]) + " of pogs. wtf.")
            return

        requested_user = message.content[2::]
        if requested_user in pog_count.keys():
            await message.channel.send(requested_user + " has pogged " + str(pog_count[requested_user]) + " times. How does that make you feel " + author_id)
        else:
            await message.channel.send(requested_user + " hasn't pogged yet, as it should be.")

#region token
client.run('NzYzNDEwMDEwNzg0Mzk5MzYz.X33S-g.037e-4DMIPKZPXzOEpDtrMDrQyo')
#endregion
