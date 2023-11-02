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
"""A setup module for dcsmissionpy."""

import re

from setuptools import setup


setup(
    name="dcsmissionpy",
    version="0.0.1",
    author="Brian Quinlan",
    author_email="brian@sweetapp.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    description="A library and command-line tool for reading DCS mission files",
    keywords="github gh-badges badge shield status",
    long_description="",
    long_description_content_type="text/markdown",
    python_requires=">=3.12",
    install_requires=["antlr4-python3-runtime>=4.13.1,<5"],
    extras_require={
        "dev": [
            "coverage>=7.3.2",
            "mypy>=1.6.1",
            "nox",
            "pytest>=7.4.2",
        ],
    },
    license="Apache-2.0",
    packages=["dcsmissionpy", "dcsmissionpy._lua_parser"],
    package_data={
        "dcsmissionpy._lua_parser": ["Lua.interp", "Lua.tokens", "LuaLexer.interp"]
    },
    url="https://github.com/google/pybadges",
)