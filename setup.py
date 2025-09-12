from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="discord-logging-handler",
    version="0.1.0",
    description="A logging handler that sends log messages to discord via webhook.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Moses White",
    python_requires=">=3.12",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True
    )