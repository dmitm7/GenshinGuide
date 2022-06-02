import discord
from discord.ext import commands
from bot import bot
from help_commands import *


@commands.command(name="помощь")
async def helpg(ctx, *arg):
    embed = discord.Embed(
        description="Персонаж какого региона тебя интересует?",
        color=discord.Color.random()
    )
    msg = await ctx.send(
        embed=embed,
        components=[[mond_btn, liuye_btn, inazuma_btn]]
    )

    @bot.event
    async def on_button_click(res):
        decision_type = res.component.label
        if decision_type == "Мондштадт":
            await msg.edit(
                embed=discord.Embed(title='Гайды персонажей из Мондштадта', description=mond,
                                    color=discord.Color.green()),
                components=[[liuye_btn, inazuma_btn]]
            )

        if decision_type == 'Ли Юэ':
            await msg.edit(
                embed=discord.Embed(title='Гайды персонажей из Ли Юэ:', description=liuye,
                                    color=discord.Color.gold()),
                components=[[mond_btn, inazuma_btn]])
        if decision_type == 'Инадзума':
            await msg.edit(
                embed=discord.Embed(title='Гайды персонажей из Инадзумы:', description=inazuma,
                                    color=discord.Color.purple()),
                components=[[mond_btn, liuye_btn]])


def setup(bot):
    bot.add_command(helpg)
