from setuptools import find_packages
from setuptools import setup

version = "0.1.0"

setup(
    name="sos",
    version=version,
    description="Shell on Steroids",
    author="Yuhuang Hu",
    author_email="duguyue100@gmail.com",
    packages=find_packages(),
    install_requires=[
        "llvmlite",
        "sly",
    ],
    python_requires=">=3.8",
)
