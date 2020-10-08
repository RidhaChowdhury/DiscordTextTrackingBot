import discord
from time import sleep
import os
import pydub
from pydub import AudioSegment
import subprocess

client = discord.Client()
soundfile = {"Obama": "dir", "Trump": "dir"}


print("Obambot online")

@client.event
async def on_message(message):
    print("recieved message")
    if message.content.startswith("*"):
        person = "Obama"
        file = soundfile[person]
        request = "\"" + message.content[1::] + "\""
        sleep(1)
        await message.channel.send("Fine ill generate the fucking shit retard")
        clone = subprocess.Popen(["python", r"C:\Obambot\sounds\Real-Time-Voice-Cloning-master\demo_cli.py", "--text", request], stdout=subprocess.PIPE, shell=True)
        clone_status = clone.wait()
        os.system("python C:\Obambot\sounds\Real-Time-Voice-Cloning-master\demo_cli.py --text " + request)
        #print("---generated sound---")
        sleep(3)
        song = AudioSegment.from_wav("demo_output_.wav")
        # but let's make him very quiet
        song = song +5
        # save the output
        song.export("demo_output_.wav", "wav")
        #print("---amplified volume---")

        voice_channel = message.author.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=r"C:/Obambot/BOt/demo_output_.wav"))
            # Sleep while audio is playing.
            while vc.is_playing():
                sleep(.1)
            await vc.disconnect()
        else:
            await message.send(str(message.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        


#region token
client.run('NzYyMTM1ODk0OTQ1NTYyNjI0.X3kwXQ.TTTRg_GsHVY8FCIrgeHo-nDrCX4')
#endregion
