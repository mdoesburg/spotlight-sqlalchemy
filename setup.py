import setuptools
from collections import OrderedDict

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='spotlight-sqlalchemy',
    version='0.1.0',
    author='Michiel Doesburg',
    author_email='michiel@moddix.com',
    description='Laravel style input validation for Python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mdoesburg/spotlight-sqlalchemy',
    project_urls=OrderedDict((
        ('Documentation', 'https://github.com/mdoesburg/spotlight-sqlalchemy'),
        ('Code', 'https://github.com/mdoesburg/spotlight-sqlalchemy')
    )),
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[]
)
