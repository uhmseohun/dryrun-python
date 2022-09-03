import setuptools

from pathlib import Path

long_description = (Path(__file__).parent / "readme.md").read_text()

setuptools.setup(
    name="dryrun",
    version="1.0.1",
    author="Seohun Uhm",
    author_email="uhmseohun@gmail.com",
    description="Very awesome dryrun module for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uhmseohun/dryrun-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)
