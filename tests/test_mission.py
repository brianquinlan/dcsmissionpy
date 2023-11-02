import os.path
import unittest

import pytest

import dcsmissionpy


class MissionTests(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.mission = dcsmissionpy.Mission(
            os.path.join(os.path.dirname(__file__), "harpoon-radar.miz")
        )

    def test_sortie(self):
        assert self.mission.sortie == "Harpoon Radar Engagement"

    def test_theatre(self):
        assert self.mission.theatre == "Caucasus"

    def test_description(self):
        assert (
            self.mission.description
            == "An ememy cargo skip is heading to Gudauta to drop off vital supplies."
        )

    def test_blue_task_description(self):
        assert (
            self.mission.blue_task_description
            == "Sink the enemy cargo skip that is about 15nm to your west."
        )

    def test_briefing_images(self):
        for path, image in self.mission.briefing_images:
            assert path == "harpoon-radar-mission.png"
            assert image.startswith(b"\x89PNG")


@pytest.mark.skipif(
    not dcsmissionpy.is_dcs_installed(), reason="DCS World not installed"
)
def test_get_installed_aircraft():
    installed_aircraft = set(dcsmissionpy.get_installed_aircraft())
    assert "Su-25T" in installed_aircraft
    assert "TF-51D" in installed_aircraft


@pytest.mark.skipif(
    not dcsmissionpy.is_dcs_installed(), reason="DCS World not installed"
)
def test_get_installed_missions():
    for mission in dcsmissionpy.get_installed_missions("Su-25T"):
        mission.sortie
        mission.theatre
        mission.description
        mission.blue_task_description
        mission.briefing_image_paths
