# Copyright 2023 The dcsmissionpy Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Nox config for running lint and unit tests."""

import nox
import sys


def _run_tests(session):
    session.run("py.test", "--quiet", "tests", *session.posargs)


@nox.session
def coverage(session):
    session.install("-e", ".[dev]")
    session.install("coverage")
    session.install("pytest")
    session.run("coverage", "run", "-m", "pytest", "tests")
    session.run("coverage", "report", "-m")


@nox.session
def format(session):
    session.install("black")
    session.run(
        "black",
        "--check",
        r"--exclude=/(\.eggs|\.git|\.mypy_cache|\.nox|"
        r"\.pytest_cache|\.venv|\.vscode|__pypackages__|"
        r"_build|build|dist|venv|_lua_parser)/",
        ".",
    )


@nox.session
def unit(session):
    """Run the unit test suite."""
    session.install("-e", ".[dev]")
    session.install("pytest")
    _run_tests(session)
