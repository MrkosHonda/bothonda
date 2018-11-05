import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='with Mrkos'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content.startswith('!Honda'):
        randomlist = ["Hello!","Yes?","Do you need something?","Ask away!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!honda'):
        randomlist = ["Hello!","Yes?","Do you need something?","Ask away!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!Hello'):
        randomlist = ["Hello there! :)","[Honda_ERROR.exe;!>Retry]","Sup!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!hello'):
        randomlist = ["Hello there! :)","[Honda_ERROR.exe;!>Retry]","Sup!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!hi'):
        randomlist = ["Hello there! :)","[Honda_ERROR.exe;!>Retry]","Sup!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!How are you?'):
        randomlist = ["Alright . . .","Could be better . . .","[ERROR_ERROR_ERROR>Retry!$Honda_Bot.exe]"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!How are you'):
        randomlist = ["Alright . . .","Could be better . . .","[ERROR_ERROR_ERROR>Retry!$Honda_Bot.exe]"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!Dari'):
        randomlist = ["Uncle? What about him? Is he alright? Do you know him?","Does he need another soda? *opens stomach to reveal a fridge filled with soda cans*","[Honda_ERROR.exe!>Retry]","You know my Uncle? So cool! Did he tell you about us? What did he say about me?"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!Ross'):
        randomlist = ["Our master? Our . . . mother? What about her?","[Honda_ERRRRRRRRRRRRRR . . . ]","Honda.bot has stopped responding . . .","[ERROR DETECTED; RECONNECTING . . . ]","SH*e IS*n’&T T%%tto B@e Tr!US!te- D . . . ","[ER@RR@R#RO!R^^R*R]","Hm? What was that? I didn’t hear you.","Sh@e’*ll l#@ea&@ve y9&ou %3^Fo#(r @@De!!2a*d”,”[RECONNECTING. . .]"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!Asher'):
        randomlist = ["Brother?! Where is big brother?!","Yes, the tall skinny blond boi.","He took all our spoons . .","He's at the bookstore right now . . .","He left his books filled with 'chicks' out . . . Wanna go color them?!"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!Souta'):
        randomlist = ["Souta is pretty 'chicks'!","Souta is a girl","Souta is . . . boy . . .? [ERROR--- >>RETRY##$@(()943HONDA_Bot.exe","Girly boy!","Souta's the scary one.","Souta's doing alright~!","Do not touch brother's pretty boy! He gets really angry."]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!spoon'):
        randomlist = ["CLINKY PRETTY THINGS!","WHERE IS SPOON?!","DO YOU HAS SPOON?!","SPOOOOOOOOOOON"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!play'):
        randomlist = ["We should color in brother's 'chicks' books! They have pretty pictures","Wanna go into brother's study?","VIDEO GAAAAAAAAMES!!!","Play with me! It's B . Y . O . S . (Bring Your Own Spoon",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!carnoise'):
        randomlist = ["*HONK*","*CAR ALARM*","WEEWOOWEEWOO",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!Camp':
        em = discord.Embed(description='He pulled the map from his bag, opening it out for the person before him "Is this what you needed?"')
        em.set_image(url='http://rickriordan.com/content/plugins/rick-riordan-helper/assets/images/camp-half-blood.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!Prophecy':
        await client.send_message(message.channel,'*He took a moment to recall it before speaking clearly* To find the hammer strong and true; A group of four including you; At the God of Fires request; you must travel west; Both friend and foe you shall meet; Bound by bonds you cannot beat. *He took a moment to give an illusion of a breath* Did I do good?')
client.run('NTA3NTM1OTAzMDgyOTM4Mzc4.DryI-A.tvQGQNE1pm59TNov35mURjAwjO8')
