from setuptools import setup

setup(
    name="simplipy",
    version="0.0.2",
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
    license="GNU GPL3",
    keywords="visualization features",
    url="https://github.com/windisch/simplipy",
)
