import functools
import os
from typing import Iterator, Sequence, Tuple
import winreg

from dcsmissionpy.mission import Mission

_MISSION_TYPES = (
    "Single",
    "Training",
    "QuickStart",
    # "Multiplayer",
    # "Campaigns", Not supported for now
)


@functools.cache
def _get_dcs_path():
    # TODO: Support the non-beta version.
    with winreg.OpenKeyEx(
        winreg.HKEY_CURRENT_USER, r"SOFTWARE\\Eagle Dynamics\\DCS World OpenBeta"
    ) as dcs_key:
        return winreg.QueryValueEx(dcs_key, "Path")[0]


def get_installed_aircraft():
    path = os.path.join(_get_dcs_path(), rf"Mods\aircraft")
    for f in os.listdir(path):
        yield f


def get_installed_mission_paths(aircraft: str) -> Iterator[Tuple[str, str]]:
    mission_path = os.path.join(_get_dcs_path(), rf"Mods\aircraft\{aircraft}\Missions")

    for mission_type in _MISSION_TYPES:
        path = os.path.join(mission_path, mission_type)
        if os.path.exists(path):
            for f in os.listdir(path):
                if os.path.splitext(f)[1] == ".miz":
                    yield os.path.join(path, f), mission_type


def get_installed_missions(aircraft: str) -> Iterator[Mission]:
    for path, mission_type in get_installed_mission_paths(aircraft):
        yield Mission(path, official_mission=True, official_mission_type=mission_type)


def get_installed_mission(
    aircraft: str, mission_type: str, mission_basepath: str
) -> Mission:
    path = os.path.join(
        _get_dcs_path(),
        rf"Mods\aircraft\{aircraft}\Missions\{mission_type}\{mission_basepath}",
    )
    return Mission(path, official_mission=True, official_mission_type=mission_type)
