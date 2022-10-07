"""
Builds the package.
"""
from setuptools import find_packages, setup

VERSION = "1.0"
DESCRIPTION = "A function that dynamically switches Adafruit Sense Hat API's"
LONG_DESCRIPTION = (
    "This function allows for the dynamic switching of the Adafruit Sense Hat API "
    "based on whether the sense hat is connected or not"
)

# Setting up
setup(
    name="smartsense",
    version=VERSION,
    author="Spuds1224",
    author_email="zachydem@aol.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["sense-hat", "sense-emu"],
    keywords=["sense hat", "sense", "adafruit", "sense emu","sense emulation"],
    classifiers= [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux"
    ]
)
