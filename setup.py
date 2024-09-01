from setuptools import setup, find_packages
from gitv.git_version import build_version


def readme():
    from pathlib import Path

    return dict(
        license="MIT",
        author="figroc",
        url="https://github.com/figroc/py-gitv",
        description="A biased Git versioning tool for Python project.",
        long_description=(Path(__file__).parent / "README.md").read_text(),
        long_description_content_type="text/markdown",
    )


setup(
    name="gitv",
    version=build_version("2.2.2", sticky=True),
    packages=find_packages(),
    entry_points={
        "setuptools.finalize_distribution_options": [
            "vcs = gitv.plugins.setup:configure"
        ],
        "hatch": ["vcs = gitv.plugins.hatch"],
        "poetry.plugin": ["vcs = gitv.plugins.poetry:GitVersionPlugin"],
    },
    python_requires=">=3.8",
    extras_require={"hatch": ["hatch"], "poetry": ["poetry"]},
    **readme(),
)
