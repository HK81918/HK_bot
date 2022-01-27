# imports
import os
import time
import discord
from discord import *
import json
import requests
import random
import pyjokes
import wikipedia
import datetime
from datetime import datetime
from discord.ext import commands, tasks
from itertools import cycle
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import flask
from keeponline import keeponline

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

bot = discord.Client()

status = cycle(["!help", "HK"])

# these are the sad words on which the bot will respond by giving a starter_encouragement
sad_words = [
    'unhappy',
    'despondent',
    'disconsolate',
    'discouraged',
    'gloomy',
    'downcast',
    'downhearted',
    'depressed',
    'dejected',
    'melancholy',
    'sorrowful',
    'despairing',
    'regretful',
    'miserable',
    'sad'
]

# encouraging words that the bot will send when it sees any of the words in sad_words
starter_encouragements = [
    "Cheer up!",
    "Hang in there",
    "You are a great person!",
    "It's ok"
]

# the words that give a signal to the bot to send a quote
quotes = [
    'quote',
    'inspire',
    'inspiration',
    'thought'
]

# hello words to which the bot will respond
hello1 = [
    'greetings',
    'hi',
    'bonjour',
    'hey',
    'whats up',
    'hello']

# emojis to which the bot will respond
emoji = [
    "😀",
    "😁",
    "😂",
    "🤣",
    "😃",
    "😄",
    "😅",
    "😆",
    "😗",
    "🥰",
    "😘",
    "😍",
    "😎",
    "😋",
    "😊",
    "😉",
    "😙",
    "☺",
    "😚",
    "🙂",
    "🤗",
    "🤩",
    "🤔",
    "🤨",
    "😮",
    "😥",
    "😣",
    "😏",
    "🙄",
    "😶",
    "😑",
    "😐",
    "🤐",
    "😯",
    "😪",
    "😫",
    "🥱",
    "😴",
    "😌",
    "😛",
    "🙃",
    "😕",
    "😔",
    "😓",
    "😒",
    "🤤",
    "😝",
    "😜",
    "🤑",
    "😲",
    "☹",
    "🙁",
    "😖",
    "😞",
    "😟",
    "😤",
    "😬",
    "🤯",
    "😩",
    "😨",
    "😧",
    "😦",
    "😭",
    "😢",
    "😰",
    "😱",
    "🥵",
    "🥶",
    "😳",
    "🤪",
    "😵",
    "🥴",
    "🤮",
    "🤢",
    "🤕",
    "🤒",
    "😷",
    "🤬",
    "😡",
    "😠",
    "🤧",
    "😇",
    "🥳",
    "🥺",
    "🤠",
    "🤡",
    "🤥",
    "🤫",
    "💀",
    "👺",
    "👹",
    "👿",
    "😈",
    "🤓",
    "🧐",
    "🧐",
    "🤭",
    "☠",
    "👻",
    "👽",
    "👾",
    "🤖",
    "💩",
    "😺",
    "😸",
    "🐱",
    "👤",
    "😾",
    "😿",
    "🙀",
    "😽",
    "😼",
    "😻",
    "😹",
    "🐱"
]
emojis = {
    "😀": "Grinning face",
    "😁": "Beaming face with smiling eyes",
    "😂": "Face with tears of joy",
    "🤣": "Rolling on the floor laughing",
    "😃": "Grinning face with big eyes",
    "😄": "Grinning face with smiling eyes",
    "😅": "Grinning face with sweat",
    "😆": "Grinning squinting face",
    "😉": "Winking face",
    "😊": "Smiling face with smiling eyes",
    "😋": "Face savouring food",
    "😎": "Smiling face with sunglasses",
    "🙂": "Slightly smiling face",
    "😐": "Neutral face",
    "👆": "Backhand index pointing up",
    "👇": "Backhand index pointing up",
    "✋": "Raised hand",
    "🤚": "Raised back of the hand",
    "🤟": "Yo-Lo gesture",
    "🤘": "Yo-lo gesture",
}


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


async def func():
    await bot.wait_until_ready()
    c = bot.get_channel(934674295890796584)
    main = bot.get_channel(905051919733620796)
    await c.send("Good Morning and Today's quote:-\n" + get_quote())
    await main.send("Good Morning and Today's quote:-\n" + get_quote())


# the code to print a message on the console when the bot is ready
@bot.event
async def on_ready():
    change_status.start()
    print("\n\nI am your bot: {0.user}".format(bot))
    scheduler = AsyncIOScheduler()
    scheduler.add_job(func, CronTrigger(hour="3", minute="30", second="0"))
    scheduler.start()


@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))


#  the code to request a quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


# all the events to which the bot will respond
@bot.event
async def on_message(message):
    try:
        if True:
            if str(message.author) == "~(-)~#5956":
                c = "You boss"
            else:
                c = str(message.author)
            if str(message.author) != "HKbot#5816":
                mgn = message.guild.name
                print(
                    "\n\n***********************************************************************************************************************************************************************************")
                print("\nServer name: " + str(mgn))
                print("Server Channel: " + str(message.channel))
                print("Author: " + str(c))
                print("Message: " + str(message.content))
                print(
                    "\n***********************************************************************************************************************************************************************************")
            else:
                print(
                    "\n\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("\nMy answer: " + str(message.content))
                print(
                    "\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            message.content = message.content.lower()

            if message.author == bot.user:
                return

            output = ""

            msg = message.content
            if str(message.channel) == "🎒ask-for-link" or str(message.guild.name) != "Shadow":
                if msg.startswith("!soc"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Social Zoom Link__**](https://us04web.zoom.us/j/3382878608?pwd=Ti9rYU9GYitIeG5XL2ZOZVZCN3lLZz09)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!googlemat"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Maths google meet link__**](https://meet.google.com/lookup/dfmc2bsa7y)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!googlesoc"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Social google meet link__**](https://meet.google.com/lookup/etptexbbhz)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!mat"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Maths Zoom Link__**](https://us04web.zoom.us/j/3169052014?pwd=L2hhYXhubXErM1JQTDA0dWZ0SG9jZz09)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!eng"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__English Zoom Link__**](https://us04web.zoom.us/j/8136579403?pwd=QnQ3VHdFSDY2KzVGZlExdURjcHE4Zz09)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!sans"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Sanskrit Zoom Link__**](https://us04web.zoom.us/j/9069243259?pwd=OFc1QVhDMlpFTjdtVklzY2YyNU9IUT09)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!phy"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Physics Zoom Link__**](https://us05web.zoom.us/j/3200509910?pwd=clRZNFF0OXVlamFicjVacTRCNkRyQT09)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!googlechem"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Chemistry google meet Link__**](https://meet.google.com/lookup/dmfbe6xkko)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)
                if msg.startswith("!chem"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Chemistry zoom Link__**](https://us04web.zoom.us/j/7570952479?pwd=5IDWf2HCcT9SYxVPJTl8UpiV5gvnD4.1)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!class"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__CLASS LINK__**](https://us05web.zoom.us/j/7230509831?pwd=VUppQXFhd1MvU0tJcDlWQ09rRTBjUT09)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!bio"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Biology Zoom Link__**](https://us04web.zoom.us/j/4650209189?pwd=bTR1dUxjM0NSdzVVSFBkRXhRVU0xUT09)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!googlebio"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Biology Google Meet Link__**](https://meet.google.com/lookup/fhho57y5c3)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!com"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Computer Zoom Link__**](https://us04web.zoom.us/j/5799598999?pwd=Vzc3Z3RmSjVTUWlNUm55ZENMM25HQT09)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!hin"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Hindi Zoom Link__**](https://us04web.zoom.us/j/4552609426?pwd=Ym4xd0hHblBaMnhnUUtjYWNtOHJIQT09)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

                if msg.startswith("!yoga"):
                    embed = discord.Embed(
                        title="**Class Link**",
                        description="\n\nClick this👇\n[**__Hindi Zoom Link__**](https://us04web.zoom.us/j/2991929621?pwd=YnE2QTJHUGpIZ3c4cVlaNXBhNGNJQT09)",
                        color=discord.Colour.teal()
                    )
                    await message.channel.send(embed=embed)

            # code to send hello or namaste when the bot sees any message starting with any of these words

            a = msg.split(" ")

            if str(message.channel) == "🃏uno":
                if str(message.author) != "UNO#3297":
                    time.sleep(5)
                    await message.delete()

            if a[0] == 'greetings' or a[0] == 'hi' or a[0] == 'bonjour' or a[0] == 'hey' or \
                    a[0] == 'whats up' or a[0] == "hello":
                if str(message.author) == "~(-)~#5956":
                    await message.channel.send("Hello boss")

                elif str(message.author) == "HK_PY_bot#5816":
                    pass
                else:
                    ma = str(message.author)
                    a = ma.split("#")
                    await message.channel.send(f"Hello {a[0]}!")

            if msg.startswith("ok") and message.author == "GrumpyHamster#2457":
                await message.channel.send("ok")

            if msg.startswith("namaste"):
                if str(message.author) == "~(-)~#5956":
                    await message.channel.send("Namaste boss")
                else:
                    ma = str(message.author)
                    a = ma.split("#")
                    await message.channel.send("Namaste " + str(a[0]) + "!")

            if msg.startswith("!owner"):
                await message.channel.send("~(-)~#5956")

            # links to send when the user requests

            # help messages
            if msg.startswith("!help"):
                embed = discord.Embed(
                    title="**Help**",
                    description=str(message.author.mention) + """
```YAML

> I CAN RESPOND TO SOME OF YOUR MESSAGES\n
> Enter a message !links TO KNOW ABOUT THE CLASS LINKS\n 
> TELL ME TO MESSAGE A QUOTE AND I WILL\n
> Enter a message !cal TO KNOW ABOUT THE CALCULATION I CAN PERFORM\n
> YOU CAN USE THE !search any person COMMAND TO KNOW ABOUT ANY PERSON (with correct spellings)\n
> YOU CAN massage !cls num TO CLEAR THE AMOUNT OF MESSAGES WHICH YOU GAVE IN THE PLACE OF NUM\n
> !tt IS FOR SCHOOL TIMETABLE PIC\n

```""",
                    color=discord.Colour.teal()
                )
                await message.channel.send(embed=embed)

            words = ['fuck',
                     'shit',
                     'moron',
                     'kill',
                     'bloody',
                     'ass',
                     'bitch',
                     'cuss']

            if msg.startswith("!link"):
                embed = discord.Embed(
                    title="**Class links**",
                    description="""
```YAML
> ENTER A MESSAGE !physics FOR PHYSICS ZOOM LINK    \n
> ENTER A MESSAGE !sanskrit FOR SANSKRIT ZOOM LINK  \n
> ENTER A MESSAGE !english FOR ENGLISH ZOOM LINK    \n
> ENTER A MESSAGE !maths FOR MATHS ZOOM LINK        \n
> ENTER A MESSAGE !googlemaths FOR MATHS GOOGLE MEET LINK\n
> ENTER A MESSAGE !social FOR SOCIAL ZOOM LINK      \n
> ENTER A MESSAGE !googlesoc FOR SOCIAL GOOGLE MEET LINK\n
> ENTER A MESSAGE !chemistry FOR CHEMISTRY ZOOM LINK\n
> ENTER A MESSAGE !biology FOR BIOLOGY ZOOM LINK    \n
> ENTER A MESSAGE !googlebio FOR BIOLOGY GOOGLE MEET LINK\n
> ENTER A MESSAGE !computer FOR COMPUTER ZOOM LINK  

```""",
                    color=discord.Colour.teal()
                )
                await message.channel.send(embed=embed)

            if msg.startswith("!cal"):
                embed = discord.Embed(
                    title="**Calculations**",
                    description="""```YAML

> YOU CAN USE THIS FUNCTION !sums num TO KNOW THE SUM OF NUMBERS FROM 0 TO THE NUM WHICH YOU GAVE\n
> YOU CAN USE ( !add num1,num2 ) FOR SUM OF ANY TWO NUMBERS\n
> YOU CAN USE ( !sub num1,num2 ) FOR DIFFERENCE OF ANY TWO NUMBERS\n
> YOU CAN USE ( !mul num1,num2 ) FOR PRODUCT OF ANY TWO NUMBERS\n
> YOU CAN USE ( !div num1,num2 ) FOR QUOTIENT OF ANY TWO NUMBERS\n

```""",
                    color=discord.Colour.teal()
                )
                await message.channel.send(embed=embed)

            # sending the quote

            # if any(word in msg for word in quotes):
            #   quote = get_quote()
            #  await message.channel.send(quote)

            if any(word in msg for word in sad_words):
                await message.channel.send(random.choice(starter_encouragements))

            # code for the bot to perform calculations
            if msg.startswith("!sums"):
                x = msg.split(" ")
                x[1] = int(x[1])
                a = x[1]
                await message.channel.send(a * (a + 1) / 2)

            if any(word in msg for word in emoji) and str(message.channel.guild) != "Shadow":
                await message.add_reaction(str(msg))

            if any(word in msg for word in emojis):
                for messages in msg:
                    output += emojis.get(messages) + " "
                    break

            if msg.startswith("!add"):
                a = msg.split(" ")
                b = a[1].split(",")
                await message.channel.send("The sum is: " + str(add(int(b[0]), int(b[1]))))

            if msg.startswith("!sub"):
                a = msg.split(" ")
                b = a[1].split(",")
                await message.channel.send("The difference is: " + str(sub(int(b[0]), int(b[1]))))

            if msg.startswith("!mul"):
                a = msg.split(" ")
                b = a[1].split(",")
                await message.channel.send("The product is: " + str(mul(int(b[0]), int(b[1]))))

            if msg.startswith("!div"):
                a = msg.split(" ")
                b = a[1].split(",")
                await message.channel.send("The quotient is: " + str(div(int(b[0]), int(b[1]))))

            # making a search on wikipedia
            if msg.startswith("!search"):
                person = msg.replace('!search', '')
                info = wikipedia.summary(person, 1)
                await message.channel.send(info)

            # sending lame jokes
            if msg.startswith("!joke"):
                await message.channel.send(pyjokes.get_joke())

            # clearing the amount of messages given

            # clearing everything
            if str(message.guild.name) == "Shadow":
                if str(msg) == "!clearall" and str(message.author) == "debracula#7906":
                    await message.channel.purge()
                if msg.startswith("!cls") and str(message.author) == "debracula#7906":
                    a = msg.split(" ")
                    b = a[1]
                    await message.channel.purge(limit=int(b) + 1)
            else:
                if str(msg) == "!clearall":
                    await message.channel.purge()
                if msg.startswith("!cls"):
                    a = msg.split(" ")
                    b = a[1]
                    await message.channel.purge(limit=int(b) + 1)

            # customising hashtag channel
            if str(message.channel) == "hashtags" and message.content != "":
                if msg.startswith("#"):
                    await message.delete()
                    await message.channel.send("**" + str(msg) + "**" + " ||@everyone||")
                else:
                    await message.delete()

            if str(message.guild.name) != "Shadow":
                if any(word in msg for word in words):
                    await message.delete()

            if msg.startswith("!tt"):
                file = discord.File("timtable.jpeg")
                embed = discord.Embed(
                    title="Timetable",
                    timestamp=datetime.now(),
                    color=discord.Colour.teal()
                )
                embed.set_image(url="attachment://timtable.jpeg")
                await message.channel.send(file=file, embed=embed)

                file = discord.File("tt.jpeg")
                embed = discord.Embed(
                    title="Timings",
                    timestamp=datetime.now(),
                    color=discord.Colour.teal()
                )
                embed.set_image(url="attachment://tt.jpeg")
                await message.channel.send(file=file, embed=embed)

            if str(message.channel) == "reaction-channel" and message.content != "":
                await message.add_reaction("😀")

            if msg.startswith("!hk"):
                embed = discord.Embed(
                    title="HK",
                    description="[Google](https://google.com)",
                    timestamp=datetime.now(),
                    color=discord.Colour.teal()
                )
                await message.channel.send(embed=embed)

    except AttributeError:
        if str(message.author) == "~(-)~#5956":
            b = "You boss"
            hk = "Boss"
        else:
            ma = str(message.author)
            a = ma.split("#")
            hk = "boss"
            b = a[0]
        if str(message.author) != "HKbot#5816":
            print(
                "\n\n***********************************************************************************************************")
            print("\nPrivate talk with: " + str(b))
            print("Message: " + str(message.content))
            print(
                "\n***********************************************************************************************************")
        else:
            print(
                "\n\n-----------------------------------------------------------------------------------------------------------")
            print("\nMy answer: " + str(message.content))
            print(
                "\n-----------------------------------------------------------------------------------------------------------")
        if str(message.author) == "~(-)~#5956":
            await message.channel.send("Sorry " + str(hk) + ", you did not allow me to talk privately.")
        else:
            await message.channel.send("Sorry " + str(b) + ", I am not allowed to talk privately.")


keeponline()


bot.run(os.environ['token'])