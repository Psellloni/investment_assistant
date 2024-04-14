import asyncio
import os
from config import TOKEN

from tinkoff.invest import AsyncClient


async def main():
    async with AsyncClient(TOKEN) as client:
        print(await client.users.get_accounts())


if __name__ == "__main__":
    asyncio.run(main())