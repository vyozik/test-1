# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages  # noqa: H301

NAME = "looker_sdk"
VERSION = "0.1.3b21"
REQUIRES = [
    "requests >= 2.22",
    # Python 3.6
    "attrs >= 18.2.0;python_version<'3.7'",
    "cattrs < 1.1.0;python_version<'3.7'",
    "python-dateutil;python_version<'3.7'",
    # Python 3.7+
    "attrs >= 20.1.0;python_version>='3.7'",
    "cattrs >= 1.1.0;python_version>='3.7'",
    "typing-extensions;python_version<'3.8'",
]


setup(
    author="Looker Data Sciences, Inc.",
    author_email="support@looker.com",
    description="Looker API 3.1",
    install_requires=REQUIRES,
    license="MIT",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    keywords=["Looker", "Looker API", "looker_sdk", "Looker API 3.1"],
    name=NAME,
    package_data={"looker_sdk": ["py.typed", "looker_sdk/looker-sample.ini"]},
    packages=find_packages(),
    python_requires="~=3.6",
    url="https://pypi.python.org/pypi/looker_sdk",
    version=VERSION,
)
