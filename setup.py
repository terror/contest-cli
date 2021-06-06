import os
from setuptools import setup, find_packages

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="contest_cli",
    version="0.0.2",
    author="Liam Scalzulli",
    author_email="liamscalzulli@gmail.com",
    description=("Programming contest information for those who live in the terminal"),
    long_description_content_type="text/markdown",
    license="BSD",
    keywords="utility, programming, contests, cli",
    url="http://packages.python.org/contest-cli",
    project_urls={"Source Code": "https://github.com/terror/contest-cli"},
    packages=find_packages(),
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["rich", "requests"],
    entry_points={"console_scripts": ["contest_cli = contest_cli.cli:cli"]},
    python_requires=">=3.7",
)
