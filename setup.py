import re

from setuptools import find_packages
from setuptools import setup


def get_version():
    filename = "cocoder/__init__.py"
    with open(filename) as f:
        match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M)
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version


def get_long_description():
    with open("README.md", encoding="UTF-8") as f:
        long_description = f.read()
        return long_description


version = get_version()


setup(
    name="cocoder",
    version="0.1.6",
    author="daniel park",
    author_email="parkminwoo1991@gmail.com",
    description="",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/dsdanielpark/Co-Coder",
    packages=find_packages(exclude=[]),
    python_requires=">=3.6",
    install_requires=["openai",
                      "bardapi @ git+https://github.com/dsdanielpark/Bard-API.git@0.1.11-multilang2"],

    keywords="Python Debuger, Python AI Debug, Realtime Debuger, Search, Find Debug Infomation, Bard, ChatGPT, GoogleBard, OpenAIchatGPT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={"console_scripts": ["Cocoder=Cocoder.cli:main"]},
)
