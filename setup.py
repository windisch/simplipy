from setuptools import setup
from pathlib import Path

setup(
    name="simplipy",
    version="0.1.0",
    packages=["simplipy"],

    # dependencies
    install_requires=[
        'numpy>=1.17.2',
        'scikit_learn',
        'xgboost',
        'matplotlib',
        'pandas'
    ],
    tests_require=[
        "pytest",
    ],

    # metadata for upload to PyPI
    author="Tobias Windisch",
    author_email="tobias.windisch@posteo.de",
    description="Collection of personalized helpers for machine learning projects",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    license="GNU GPL3",
    keywords="visualization features",
    url="https://github.com/windisch/simplipy",
)
