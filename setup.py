from setuptools import setup, find_packages
from gitv.git_version import build_version

setup(
    name="gitv",
    version=build_version("2.2.1", sticky=True),
    packages=find_packages(),
    entry_points={
        "setuptools.finalize_distribution_options": ["vcs = gitv.plugins.setup:configure"],
        "hatch": ["vcs = gitv.plugins.hatch"],
        "poetry.plugin": ["vcs = gitv.plugins.poetry:GitVersionPlugin"],
    },
    python_requires=">=3.8",
    install_requires=["setuptools"],
    extras_require={"hatch": ["hatch"], "poetry": ["poetry"]},
)
