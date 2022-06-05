__author__ = 'Shawn Fu (shawn13aby@gmail.com)'

import logging as log
from flask import Flask
import os
import discord
from threading import Thread

log.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                level=log.INFO)

app = Flask(__name__)
client = discord.Client()


def run_flask():
    app.run('0.0.0.0')


@app.route("/")
def index():
    return '<h1>healthy</h1>'


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id != 946612346879639602:
        return
    guild = client.get_guild(payload.guild_id)
    member = payload.member
    emoji = payload.emoji.name

    # logic
    if emoji == '👍':
        role = guild.get_role(946596068764831805)
    elif emoji == '👎':
        role = guild.get_role(946589162738429953)
    await member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id != 946612346879639602:
        return
    guild = client.get_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)
    emoji = payload.emoji.name

    # logic
    if emoji == '👍':
        role = guild.get_role(946596068764831805)
    elif emoji == '👎':
        role = guild.get_role(946589162738429953)
    await member.remove_roles(role)


if __name__ == '__main__':
    Thread(target=run_flask).start()
    client.run(os.environ['DISCORD_TOKEN'])