import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import os

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '도움')
    async def 도움(self, ctx):
        embed = discord.Embed(title = '도움말', description = '도움말입니다.', colour = 0xFF00, inline=True)
        embed.add_field(name = '`+티켓생성`', value = '티켓 생성')
        embed.add_field(name = '`+크레딧`', value = '땅콩 봇 개발자 목록')
        embed.add_field(name = '`+상점`', value = '프리미엄 등급제 상점')
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Help(bot))