import argparse

import discord

from palbot import dbot  # type: ignore
from palbot.containers.palworld import cnmg  # type:ignore

parser = argparse.ArgumentParser()
parser.add_argument("client_id", type=str)
parser.add_argument("token", type=str)
arg = parser.parse_args()


mc = dbot.MyClient()
print(mc.get_oauth_url(arg.client_id))


@mc.tree.command(name="palstart", description="Palworldのサーバーを起動します")
async def cntstart(interaction: discord.Interaction) -> None:
    await interaction.response.defer()

    if cnmg.start_container():
        await interaction.followup.send("Palworldのサーバーを起動しました！")

    else:
        await interaction.followup.send("Palworldのサーバーは既に起動しています！")


@mc.tree.command(name="palstop", description="Palworldのサーバーを停止します")
async def cntstop(interaction: discord.Interaction) -> None:
    await interaction.response.defer()

    if cnmg.stop_container():
        await interaction.followup.send("Palworldのサーバーを停止しました！")
    else:
        await interaction.followup.send("Palworldのサーバーは既に停止しています！")


mc.run(arg.token)
