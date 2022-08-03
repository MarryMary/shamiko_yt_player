import re
import discord
import src.ytplay

client = discord.Client()

@client.event
async def on_ready():
    print("Start up bot!")

@client.event
async def on_message(message):
    if client.user in message.mentions:
        with open("src/help.txt", "r", encoding = "utf-8") as f:
            helps = f.read()
        await message.channel.send(helps)
    elif message.content.strip().startswith(";"):
        if message.author.bot:
            return
        else:
            wtout_mention = message.content.lstrip(";")
            if wtout_mention.strip() == "":
                with open("src/help.txt", "r", encoding="utf-8") as f:
                    helps = f.read()
                await message.channel.send(helps)
            else:
                if wtout_mention.strip() == "in":
                    if message.author.voice is None:
                        user = message.author.id
                        await message.channel.send("ごせんぞ！どうしましょう！誰もいません！！")
                    else:
                        await message.author.voice.channel.connect()
                        await message.channel.send("ききかんりー！！")
                elif wtout_mention.strip() == "q":
                    if message.guild.voice_client is None:
                        await message.channel.send("ごせんぞー！！どうしましょう！どこにも入ってません！どこから出たらいいですか！！")
                    else:
                        await message.guild.voice_client.disconnect()
                        await message.channel.send("なんだかあっけない最期でしたね。")
                elif wtout_mention.strip().startswith("play"):
                    if message.guild.voice_client is None:
                        await message.channel.send("あの、どこにも入っていないのですが・・・")
                    elif message.guild.voice_client.is_playing():
                        message.guild.voice_client.stop()
                        url = wtout_mention.strip()[4:]
                        player = await src.ytplay.YTDLSource.from_url(url, loop=client.loop)
                        await message.guild.voice_client.play(player)
                    else:
                        url = wtout_mention.strip()[4:]
                        player = await src.ytplay.YTDLSource.from_url(url, loop=client.loop)
                        await message.guild.voice_client.play(player)
                        await message.channel.send(f"ごせんぞ！やりました！{player.title}が再生できました！")
                elif wtout_mention.strip() == "stop":
                    if message.guild.voice_client is None:
                        await message.channel.send("ごせんぞー！！どうしましょう！どこにも入ってません！何を止めたらいいですか！！")
                    elif not message.guild.voice_client.is_playing():
                        await message.channel.send("あの、何も再生していないのですが・・・")
                    else:
                        message.guild.voice_client.stop()
                        await message.channel.send("やりました！ごせんぞ！止まりました！")
                elif wtout_mention.strip() == "help":
                    with open("src/help.txt", "r", encoding = "utf-8") as f:
                        helps = f.read()
                    await message.channel.send(helps)
                else:
                    with open("src/help.txt", "r", encoding = "utf-8") as f:
                        helps = f.read()
                    await message.channel.send(helps)

client.run("YOUR TOKEN HERE")