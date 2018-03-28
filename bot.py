# DKeyword by Da532.

#---CONFIG---
enabled_banned_words = True # Change to False if you want this disabled.
enabled_responses = True # Change to False if you want this disabled.
banned_words = ("naughty, word, xd, nigeria") # Write words here you'd like to be removed.
responses = {"hi" : "Hello!", "jeff" : "Jeff is bad!!"} # Write words and responses to them here.
token = "TOKEN_HERE" # Your bot token here.

#---BOT---
import discord

bot = discord.Client()

info = "[Info] "
error = "[Error] "
success = "[Success] "

@bot.event
async def on_ready():
    print (info + "Ready!") 

@bot.event
async def on_message(message):
    if bot.user.id == message.author.id:
        return
    words = message.content.lower().split(" ")
    for word in words:
        if not message.channel.is_private:
            if word in banned_words.lower():
                if enabled_banned_words == False:
                    return
                if len(word) == 1:
                    pass
                else:
                    try:
                        await bot.delete_message(message)
                        print(success + "{} has posted a banned word in {}. It was successfully removed from chat.".format(message.author.name, message.server.name))
                    except:
                        print(error + "{} has posted a banned word in {}. It failed to be removed from chat.".format(message.author.name, message.server.name))
                        pass
                    try:
                        await bot.send_message(message.channel, ":x: That word is not allowed here!")
                        return
                    except:
                        print(error + "I have failed to post a message in {}.".format(message.server.name))
                        return

            elif word in responses:
                if enabled_responses == False:
                    return
                for key in responses:
                    if key in word:
                        _key = key.lower()
                    else:
                        pass
                try:
                    await bot.send_message(message.channel, responses[_key])
                    print(success + "{} has triggered the response {} in {}.".format(message.author.name, _key, message.server.name))
                    return
                except:
                    print(error + "I have failed to post a message in {}.".format(message.server.name))
                    return
            else:
                pass

bot.run(token)
