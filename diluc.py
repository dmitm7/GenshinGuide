import discord
from discord.ext import commands
from bot import bot
from help_commands import *


@commands.command(name="дилюк")
async def diluc(ctx, *arg):
    embed = discord.Embed(
        title='Дилюк',
        description=dilucD,
        color=discord.Color.red())
    embed.set_image(url="https://sun9-33.userapi.com/impg/mRdVGZtrXef4jyVKUqXryHmAYaUYBS-z3LBwkg/wq_WHI5vdlQ.jpg?size=340x604&quality=96&sign=97be9e4cd004e9057363d502790c6702&c_uniq_tag=7psIlkSAWHKHMB-7kR9Rv3MXrQtXp2XLKpAFYoGWIVg&type=albumhttps://sun9-33.userapi.com/impg/mRdVGZtrXef4jyVKUqXryHmAYaUYBS-z3LBwkg/wq_WHI5vdlQ.jpg?size=340x604&quality=96&sign=97be9e4cd004e9057363d502790c6702&c_uniq_tag=7psIlkSAWHKHMB-7kR9Rv3MXrQtXp2XLKpAFYoGWIVg&type=album")
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
                embed=discord.Embed(title='Подходящее оружие:', description=dilucW, color=discord.Color.red()),
                components=[[artifacts, stars, talants]])

        if decision_type == 'Артефакты':
            await msg.edit(components=[])
            await msg.edit(
                embed=discord.Embed(title='Артефакты:', description=dilucA, color=discord.Color.red()),
                components=[[weapons, stars, talants]])
        if decision_type == 'Созвездия':
            await msg.edit(components=[])
            await msg.edit(
                embed=discord.Embed(title='Созвездия:', description=dilucS, color=discord.Color.red()),
                components=[[weapons, artifacts, talants]])
        if decision_type == 'Таланты':
            await msg.edit(components=[])
            await msg.edit(
                embed=discord.Embed(title='Таланты:', description=dilucT, color=discord.Color.red()),
                components=[[weapons, artifacts, stars]])


def setup(bot):
    bot.add_command(diluc)
