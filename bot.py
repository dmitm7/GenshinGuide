import discord
from discord.ext import commands
from discord_components import DiscordComponents
from help_commands import *


config = {
    'token': 'OTc2NDIyMjgwODk0NzY3MTE0.GV5INy.T1KN7jXh5ItbTI8-1UWFDxGvhPObQDTyTKjxIE',
    'prefix': '!',
}
bot = commands.Bot(command_prefix=config['prefix'])


@bot.event
async def on_ready():
    DiscordComponents(bot)
    print("ready")


bot.load_extension("help")
bot.load_extension("noelle")
bot.load_extension("diluc")

bot.run(config['token'])
