# from UI.UI_timer.timer_ui import init_ui
# import sys
import asyncio

from pathlib import Path
from timer.timer import decrease_time, timer
from src.classes import save_data, PlainDataStorage
from UI.UI_timer.timer_ui import init_ui

async def main():
    tasks = [
        init_ui(),
        save_data(PlainDataStorage(Path.cwd() / "testdata.txt"))

    ]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())

