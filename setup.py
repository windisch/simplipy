from setuptools import setup

setup(
    name="simplipy",
    version="0.0.1",
    packages=["simplipy"],

    # dependencies
    install_requires=[
        'numpy>1.14.0,<2.0.0',
        'pytest-runner',
    ],
    tests_require=[
        "pytest",
    ],

    # metadata for upload to PyPI
    author="Tobias Windisch",
    author_email="tobias.windisch@posteo.de",
    description="Python library for simplicial complexes",
    license="GNU GPL3",
    keywords="simplicial complex persistance",
    url="https://github.com/windisch/simplipy",
)
