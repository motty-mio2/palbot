import asyncio

import discord
from discord import Client, app_commands

from palbot.containers.palworld import cnmg
from palbot.papi import get_players

import logging

logger = logging.getLogger("discord")


class MyClient(Client):
    def __init__(self, client_id: str) -> None:
        super().__init__(intents=discord.Intents.default())

        self.tree = app_commands.CommandTree(self)
        self.client_id = client_id

    def get_oauth_url(self, client_id: str) -> None:
        invite_url = discord.utils.oauth_url(
            client_id=client_id,
            permissions=discord.Permissions(permissions=2147485696),
        )

        logger.info(f"Invite URL : {invite_url}")

    async def on_ready(self) -> None:
        logger.info(f"We have logged in as {self.user}")

        await self.change_presence(activity=discord.Game("起動したよ！"))

        await self.tree.sync()

        self.loop.create_task(self.watch_loop())
        self.get_oauth_url(self.client_id)

    async def watch_loop(self) -> None:
        while True:
            pl = get_players()

            if pl is None:
                logger.info("Container is not running")
            else:
                if pl == 0:
                    logger.info("No Player")
                    cnmg.container_stop()
            await asyncio.sleep(5 * 60)
