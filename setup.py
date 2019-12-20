from setuptools import setup, find_packages
from collections import OrderedDict

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="spotlight-sqlalchemy",
    version="1.0.2",
    author="Michiel Doesburg",
    author_email="michiel@moddix.com",
    description="SQLAlchemy plugin for Spotlight.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="spotlight sqlalchemy validation validate",
    url="https://github.com/mdoesburg/spotlight-sqlalchemy",
    project_urls=OrderedDict(
        (
            ("Documentation", "https://github.com/mdoesburg/spotlight-sqlalchemy"),
            ("Code", "https://github.com/mdoesburg/spotlight-sqlalchemy"),
        )
    ),
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["spotlight"],
)
