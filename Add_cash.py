import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import os

class Among_Us(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '어몽어스')
    async def 어몽어스(self, ctx):
        embed = discord.Embed(title = '어몽어스', description = '어몽어스 게임을 시작합니다')
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Among_Us(bot))