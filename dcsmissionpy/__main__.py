import base64
import html
import pathlib
import tempfile
from typing import IO, Text
import webbrowser

import dcsmissionpy

_HTML_HEADER = """
<html>
    <head>
        <title>Installed Missions</title>
        <style>
            td {
                vertical-align: top;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
"""

_HTML_FOOTER = """
    </body>
</html>
"""
_MISSION_TEMPLATE = """
    <h2>{title}</h2>
    <p>{description}<p>
    <table>
        <tr>
            <td>path:</td>
            <td><a href="{mission_url}"><pre>"{mission_path}"</pre></a></td>
        </tr>
        <tr>
            <td>theatre:</td>
            <td>{theatre}</td>
        </tr>
        <tr>
            <td>official_mission_type:</td>
            <td>{official_mission_type}</td>
        </tr>
        <tr>
            <td>blue_task_description:</td>
            <td>{blue_task_description}</td>
        </tr>
    </table>
    """


def write_mission(f: IO[Text], mission: dcsmissionpy.Mission):
    def format_text(s):
        return html.escape(s).replace("\n", "<br>")

    f.write(
        _MISSION_TEMPLATE.format(
            title=format_text(mission.sortie),
            description=format_text(mission.description),
            mission_url=pathlib.Path(mission.mission_path).as_uri(),
            mission_path=mission.mission_path,
            theatre=format_text(mission.theatre),
            official_mission_type=mission.official_mission_type,
            blue_task_description=format_text(mission.blue_task_description),
        )
    )

    for _, image in mission.briefing_images:
        f.write(
            f'<img src="data:image/png;base64, '
            + base64.b64encode(image).decode("ascii")
            + '" style="max-width: 512px">'
        )


def main():
    with tempfile.NamedTemporaryFile(
        mode="w+", suffix=".html", delete=False, delete_on_close=False, encoding="utf-8"
    ) as f:
        f.write(_HTML_HEADER)
        uri = pathlib.Path(f.name).as_uri()
        for aircraft in dcsmissionpy.get_installed_aircraft():
            f.write(f"<h1>{aircraft}</h1>")
            for mission in dcsmissionpy.get_installed_missions(aircraft):
                write_mission(f, mission)
        f.write(_HTML_FOOTER)
    webbrowser.open(uri)


if __name__ == "__main__":
    main()
