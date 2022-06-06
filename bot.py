import discord
from discord.ext import commands
from discord_components import DiscordComponents
from help_commands import *


config = {
    'token': 'OTc2NDIyMjgwODk0NzY3MTE0.GCi5QJ.kS_3L2UK9xG0V-3y_f9EAqlRwihFqkB41MWT90',
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
