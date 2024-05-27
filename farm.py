# meta developer: @zorotexr
import random
from datetime import timedelta
import asyncio
import time
from telethon import events

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class FarmRostmomentMod(loader.Module):
    """Модуль для автоматического фарминга в чате @Rostmomentchat"""

    strings = {"name": "RCFarm"}

    def __init__(self):
        self.tasks = []

    async def b_run(self, client):
        while True:
            await client.send_message('@Rostmomentchat', "ферма")
            await asyncio.sleep(7300)


    @loader.unrestricted
    @loader.ratelimit
    async def farm_rccmd(self, message):
        """Запустить автоматический фарминг в боте"""
        if self.tasks:
            return await message.edit("Автоматический фарминг уже запущен.")
        await message.edit("Автоматический фарминг запущен.")
        client = message.client
        self.tasks = [asyncio.create_task(self.b_run(client))]

    @loader.unrestricted
    @loader.ratelimit
    async def stop_rccmd(self, message):
        """Остановить автоматический фарминг в боте"""
        if not self.tasks:
            return await message.edit("Автоматический фарминг не запущен.")
        for task in self.tasks:
            task.cancel()
        self.tasks = []
        await message.edit("Автоматический фарминг остановлен.")
