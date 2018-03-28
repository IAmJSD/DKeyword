# DKeyword by Da532.

import discord
import json

bot = discord.Client()

config = json.load(
    open("./config.json", "r")
)
config["banned_words"] = [w.lower() for w in config["banned_words"]]

info = "[Info] "
error = "[Error] "
success = "[Success] "


@bot.event
async def on_ready():
    print(info + "Ready!")


@bot.event
async def on_message(message):
    if bot.user.id == message.author.id:
        return
    words = message.content.lower().split(" ")
    for word in words:
        if not message.channel.is_private:
            if word in config["banned_words"]:
                if not config["enable_banned_words"]:
                    return
                if len(word) == 1:
                    return
                else:
                    try:
                        await bot.delete_message(message)
                        print(
                            success + "{} has posted a banned word in {}. "
                            "It was successfully removed from chat.".format(
                                message.author.name, message.server.name
                            )
                        )
                    except Exception:
                        print(
                            error + "{} has posted a banned word in {}. "
                            "It failed to be removed from chat.".format(
                                message.author.name, message.server.name
                            )
                        )
                        return
                    try:
                        await bot.send_message(
                            message.channel, ":x: That word is not "
                            "allowed here!"
                        )
                        return
                    except Exception:
                        print(
                            error + "I have failed to post a "
                            "message in {}.".format(message.server.name)
                        )
                        return

            elif word in config["responses"]:
                if not config["enable_responses"]:
                    return
                try:
                    await bot.send_message(
                        message.channel, config["responses"][word]
                    )
                    print(
                        success + "{} has triggered the "
                        "response {} in {}.".format(
                            message.author.name, word, message.server.name
                        )
                    )
                    return
                except Exception:
                    print(
                        error + "I have failed to post "
                        "a message in {}.".format(message.server.name)
                    )
                    return

bot.run(config["token"])
