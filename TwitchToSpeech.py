from twitchio.ext import commands
from twitchio import *
import os
import TTS
import re
import configparser
import datetime
import pytz
#Global Variables
#list of keywords and the style they go with
TWITCH_CHANNEL_NAME = "PUT_YOUR_CHANNEL_NAME_HERE"
styleDict = {
    'angry':'angry',
    'angrily':'angry',
    'angered':'angry',
    'furious':'angry',
    'furiously':'angry',
    'cheerful':'cheerful',
    'cheerfully':'cheerful',
    'happily':'cheerful',
    'happy':'cheerful',
    'joyful':'cheerful',
    'joyfully':'cheerful',
    'excited':'excited',
    'excitedly':'excited',
    'ecstatic':'excited',
    'ecstatically':'excited',
    'hopeful':'hopeful',
    'hopefully':'hopeful',
    'normal':'hopeful',
    'normally':'hopeful',
    'default':'hopeful',
    'regular':'hopeful',
    'regularly':'hopeful',
    'sad':'sad',
    'sadly':'sad',
    'depressed':'sad',
    'depressingly':'sad',
    'sorrowful':'sad',
    'saddened':'sad',
    'terrified':'whispering',
    'horrified':'terrified',
    'afraid':'whispering',
    'scared':'terrified',
    'unfriendly':'unfriendly',
    'rudely':'unfriendly',
    'shout':'shouting',
    'shouts':'shouting',
    'shouting':'shouting',
    'whisper':'whispering',
    'whispers':'whispering',
    'whispering':'whispering',
    }
#List of keywords for each voice
voiceDict = {
    'davis':"en-US-DavisNeural",
    'tony':"en-US-TonyNeural",
    'jason':"en-US-JasonNeural",
    'guy':"en-US-GuyNeural",
    'jane':"en-US-JaneNeural",
    'nancy':"en-US-NancyNeural",
    'jenny':"en-US-JennyNeural",
    'aria':"en-US-AriaNeural",
    'sara':"en-US-SaraNeural",
    'girl':"en-US-SaraNeural",
    'masculine':"en-US-DavisNeural",
    'feminine':"en-US-JennyNeural",
    'fem':"en-US-JaneNeural",
    'masc':"en-US-TonyNeural",
    'femboy':"en-US-JasonNeural",
    'default':"en-US-DavisNeural",
    'regular':'en-US-DavisNeural',
}
class TwitchBot(commands.Bot):

    def __init__(self):
        # Initialise the bot
        TWITCH_ACCESS_TOKEN = os.environ.get('TWITCH_ACCESS_TOKEN')
        super().__init__(token=TWITCH_ACCESS_TOKEN, prefix='?', initial_channels=[TWITCH_CHANNEL_NAME])

    async def event_ready(self):
        # Alert successful connection
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        print('---------------------------------------------------')
        TTS.speak(f'Twitch To Speech™ is now activated!', 'cheerful', 'en-US-DavisNeural')

    async def event_message(self, message):
        #Listen for chat messages
        messageContent = message.content
        messageAuthor = message.author.display_name
        #get the time the message was sent
        messageTimeMin = message.timestamp.astimezone(pytz.timezone('US/Eastern')).minute
        messageTimeSec = message.timestamp.astimezone(pytz.timezone('US/Eastern')).second
        messageTimeHour = message.timestamp.astimezone(pytz.timezone('US/Eastern')).hour
        #print message info to console
        print(f'[{messageTimeHour}:{messageTimeMin}:{messageTimeSec}] <{messageAuthor}> {messageContent}')
        #filter out commands
        if not messageContent.startswith('!'):
            text, style, voice = formatMessage(messageContent)
            TTS.speak(text, style, voice)

def formatMessage(text):
    #default voice & style
    style = 'hopeful'
    voice = 'en-US-DavisNeural'
    #detect any style or voice keyword + format message to be spoken
    for keyword in styleDict:
        if '*'+keyword+'*' in text.lower():
            text = re.compile(re.escape('*'+keyword+'*'), re.IGNORECASE).sub('', text)
            style = styleDict[keyword]
        if '  ' in text:
            text = text.replace('  ',' ')
        if text.startswith(' '):
            text = text[1:]
    for keyword in voiceDict:
        if '('+keyword+')' in text.lower():
            text = re.compile(re.escape('('+keyword+')'), re.IGNORECASE).sub('', text)
            voice = voiceDict[keyword]
        if '  ' in text:
            text = text.replace('  ',' ')
        if text.startswith(' '):
            text = text[1:]
    return text, style, voice
TwitchBot().run()