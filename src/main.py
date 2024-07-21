import argparse

import discord

from palbot import dbot  # type: ignore
from palbot.containers.palworld import cnmg  # type:ignore

parser = argparse.ArgumentParser()
parser.add_argument("client_id", type=str)
parser.add_argument("token", type=str)
arg = parser.parse_args()


mc = dbot.MyClient(client_id=arg.client_id)


@mc.tree.command(name="palstart", description="Palworldのサーバーを起動します")
async def cntstart(interaction: discord.Interaction) -> None:
    await interaction.response.defer()

    res = cnmg.container_start()

    await interaction.followup.send(f"{res.msg}")


@mc.tree.command(name="palstop", description="Palworldのサーバーを停止します")
async def cntstop(interaction: discord.Interaction) -> None:
    await interaction.response.defer()

    res = cnmg.container_stop()

    await interaction.followup.send(f"{res.msg}")


@mc.tree.command(name="palstatus", description="Palworldのサーバーを確認します")
async def cntstatus(interaction: discord.Interaction) -> None:
    await interaction.response.defer()

    res = cnmg.container_status()

    await interaction.followup.send(f"{res.msg}")


mc.run(arg.token)
