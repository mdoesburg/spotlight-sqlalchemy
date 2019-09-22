import setuptools
from collections import OrderedDict

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="spotlight-sqlalchemy",
    version="0.1.2",
    author="Michiel Doesburg",
    author_email="michiel@moddix.com",
    description="SQLAlchemy plugin for Spotlight.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mdoesburg/spotlight-sqlalchemy",
    project_urls=OrderedDict(
        (
            ("Documentation", "https://github.com/mdoesburg/spotlight-sqlalchemy"),
            ("Code", "https://github.com/mdoesburg/spotlight-sqlalchemy"),
        )
    ),
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=["spotlight"],
)
