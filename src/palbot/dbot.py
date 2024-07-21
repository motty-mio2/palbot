import asyncio

import discord
from discord import Client, app_commands

from palbot.containers.palworld import cnmg
from palbot.papi import get_players


class MyClient(Client):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    def get_oauth_url(self, client_id: str) -> str:
        return discord.utils.oauth_url(
            client_id=client_id,
            permissions=discord.Permissions(permissions=2147485696),
        )

    async def on_ready(self) -> None:
        print(f"We have logged in as {self.user}")

        await self.change_presence(activity=discord.Game("起動したよ！"))

        await self.tree.sync()

        self.loop.create_task(self.watch_loop())

    async def watch_loop(self) -> None:
        while True:
            pl = get_players()

            if pl is None:
                print("Container not working")
            else:
                if pl == 0:
                    cnmg.stop_container()
            await asyncio.sleep(5 * 60)
