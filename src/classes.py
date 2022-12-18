from typing import NamedTuple, TypedDict
from pathlib import Path
from datetime import datetime

class Preferences(NamedTuple):
    name_pref1: str
    name_pref2: str
    name_pref3: str


class DataUser(TypedDict):
    name_parent: str
    name_child: str
    age_child: int
    preferences: Preferences


class UserStorage:
    async def save(self) -> None:
        raise NotImplementedError


class PlainDataStorage(UserStorage):
    def __init__(self, file: Path):
        self._file = file

    async def save(self) -> None:
        now = datetime.now()
        with open(self._file, "a") as f:
            f.write(f"Начало игрового времени: {now.strftime('%d.%m.%Y %H:%M:%S')} \n")


class Time(NamedTuple):
    time_to_wait: int


async def save_data(stor: UserStorage):
    await stor.save()
