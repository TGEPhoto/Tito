import discord
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=2):
        """
        Briše poruke. bukvalno. šta si mislio lol
        """
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """
        Banuje lika i šalje mu poruku. logično.
        """
        msg = "Banovan si iz Drugova Monarhista!"
        if reason:
            msg += f"Razlog: {reason}"

        try:
            await member.send(msg)
        except discord.Forbidden:
            await ctx.send("ne mogu ja tom liku poslati poruku")

        await ctx.send(f'{member.name}#{member.discriminator} je poslan na Goli Otok!')
        await member.ban(reason=reason)
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Nisi mi rekao kog lika da pošaljem na Goli Otok!")

def setup(client):
    client.add_cog(Mod(client))