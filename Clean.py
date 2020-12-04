import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands import has_permissions
import os

class Clean(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '청소')
    @commands.has_permissions(manage_messages=True)
    async def 청소(self, ctx, clean: int):
        await ctx.send('메세지 관리 권한을 가지고 계십니다.\n이 채널의 모든 메세지를 삭제 할 수 있습니다.')
        try:
            ctx.channel.purge(limit=clean)
            await ctx.send(clean + "의 갯수만큼 청소 했습니다.")
        except:
            await ctx.send('에러 : 에러코드 001')

def setup(bot):
    bot.add_cog(Clean(bot))