import functools
import io
import os.path
from typing import Iterator, List, IO, Tuple
import zipfile

from dcsmissionpy import _parser


class Mission:
    def __init__(
        self,
        mission_path: str,
        official_mission: bool = False,
        official_mission_type: str | None = None,
    ):
        self._mission_path = mission_path
        self._official_mission = official_mission
        self._official_mission_type = official_mission_type

        if os.path.splitext(self._mission_path)[1] in [".zip", ".miz"]:
            self._zfile = zipfile.ZipFile(self._mission_path)
        else:
            self._zfile = None

    def _open(self, path, text=True):
        if self._zfile:
            f = self._zfile.open(path)
            if text:
                return io.TextIOWrapper(f, encoding="utf8")
            else:
                return f
        else:
            return open(os.path.join(self._mission_path, path), "r" if text else "rb")

    @property
    @functools.cache
    def _mission_namespace(self):
        with self._open("mission") as f:
            return _parser.lua_to_python(f.read())

    @property
    @functools.cache
    def _dictionary_namespace(self):
        with self._open("l10n/DEFAULT/dictionary") as f:
            return _parser.lua_to_python(f.read())

    @property
    @functools.cache
    def _map_resource_namespace(self):
        with self._open("l10n/DEFAULT/mapResource") as f:
            return _parser.lua_to_python(f.read())

    def __repr__(self):
        return f"<Mission({self._mission_path!r})"

    def __str__(self):
        return f"<Mission path={self._mission_path!r}>"

    @property
    def mission_path(self):
        return self._mission_path

    @property
    def official_mission(self) -> bool:
        return self._official_mission

    @property
    def official_mission_type(self) -> str:
        return self._official_mission_type

    @property
    def theatre(self) -> str:
        if "theatre" in self._mission_namespace["mission"]:
            return self._mission_namespace["mission"]["theatre"]
        else:
            print(self._mission_namespace.keys())
            with self._open("theatre") as f:
                return f.read()

    @property
    def sortie(self):
        key = self._mission_namespace["mission"]["sortie"]
        return self._dictionary_namespace["dictionary"][key]

    @property
    def description(self):
        key = self._mission_namespace["mission"]["descriptionText"]
        return self._dictionary_namespace["dictionary"][key]

    @property
    def blue_task_description(self):
        key = self._mission_namespace["mission"]["descriptionBlueTask"]
        return self._dictionary_namespace["dictionary"][key]

    @property
    def briefing_image_paths(self) -> List[str]:
        keys = self._mission_namespace["mission"].get("pictureFileNameB", {})
        return [self._map_resource_namespace["mapResource"][v] for v in keys.values()]

    @property
    def briefing_images(self) -> Iterator[Tuple[str, bytes]]:
        for path in self.briefing_image_paths:
            f = self._open(os.path.join("l10n/DEFAULT/", path), text=False)
            image = f.read()
            f.close()
            yield path, image
