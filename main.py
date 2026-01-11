import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")  # токен из variables

intents = discord.Intents.default()
intents.members = True

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
    print(f"Бот запущен как {bot.user}")


@bot.command(name="принять")
@commands.has_permissions(manage_roles=True)
async def accept(ctx):
    member = ctx.author
    guild = ctx.guild

    # выдаём роли
    for role_id in ROLES_TO_GIVE:
        role = guild.get_role(role_id)
        if role:
            await member.add_roles(role, reason="Команда !принять")

    # снимаем роль
    remove_role = guild.get_role(ROLE_TO_REMOVE)
    if remove_role and remove_role in member.roles:
        await member.remove_roles(remove_role, reason="Команда !принять")

    await ctx.send(f"✅ {member.mention}, роли успешно обновлены.")


@accept.error
async def accept_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ У тебя нет прав на использование этой команды.")


bot.run(TOKEN)
