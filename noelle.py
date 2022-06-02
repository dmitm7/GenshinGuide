import discord
from discord.ext import commands
from bot import bot
from help_commands import *


@commands.command(name="ноэлль")
async def noelle(ctx, *arg):
    embed = discord.Embed(
        title='Ноэлль',
        description=noelleD,
        color=discord.Color.gold())
    embed.set_image(url="https://i.pinimg.com/736x/37/86/32/3786321c4d8d9284db91ac7ed1813bbe.jpg")
    msg = await ctx.send(
        embed=embed,
        components=[[weapons, artifacts, stars, talants]]
    )

    @bot.event
    async def on_button_click(res):
        decision_type = res.component.label
        if decision_type == 'Оружие':
            await msg.edit(components=[])
            await msg.edit(
                embed=discord.Embed(title='Подходящее оружие:', description=noelleW, color=discord.Color.gold()),
                components=[[artifacts, stars, talants]])

        if decision_type == 'Артефакты':
            await msg.edit(components=[])
            await msg.edit(
                embed=discord.Embed(title='Артефакты:', description=noelleA, color=discord.Color.gold()),
                components=[[weapons, stars, talants]])
        if decision_type == 'Созвездия':
            await msg.edit(components=[])
            await msg.edit(
                embed=discord.Embed(title='Созвездия:', description=noelleS, color=discord.Color.gold()),
                components=[[weapons, artifacts, talants]])
        if decision_type == 'Таланты':
            await msg.edit(components=[])
            await msg.edit(
                embed=discord.Embed(title='Таланты:', description=noelleT, color=discord.Color.gold()),
                components=[[weapons, artifacts, stars]])


def setup(bot):
    bot.add_command(noelle)
