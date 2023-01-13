import asyncio
from typing import Coroutine
from opentele.td import TDesktop
from opentele.api import UseCurrentSession
from settings import settings

async def convert_tdata():
    tdesk: TDesktop = TDesktop(settings.config['tdata_path'])

    assert tdesk.isLoaded()

    client: Coroutine = await tdesk.ToTelethon(session = settings.config['file_out'], flag = UseCurrentSession)
    return client

asyncio.run(convert_tdata())