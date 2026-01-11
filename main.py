import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()  # ВАЖНО
bot = commands.Bot(command_prefix="!", intents=intents)

ROLES_TO_GIVE = [
    1457830928909992171,
    1457830928943415411,
    1457830928943415414,
    1457830928989819156,
    1457830928989819161,
    1457830929253924925,
    1457830929253924926,
    1457830929409249352,
    1457830929409249360,
]

ROLE_TO_REMOVE = 1457830928989819157


@bot.event
async def on_ready():
    print("Бот запущен:", bot.user)


@bot.command()
async def принять(ctx):
    member = ctx.author
    guild = ctx.guild

    for role_id in ROLES_TO_GIVE:
        role = guild.get_role(role_id)
        if role:
            await member.add_roles(role)

    role_remove = guild.get_role(ROLE_TO_REMOVE)
    if role_remove:
        await member.remove_roles(role_remove)

    await ctx.send("✅ Роли выданы")


bot.run(TOKEN)
