from setuptools import setup, find_packages

setup(
    name="netscope",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "networkx",
        "pandas",
        "matplotlib"
    ],
    description="A lightweight toolkit for basic network science analysis.",
    author="Your Name",
    author_email="your@email.com",
    url="https://github.com/JacopoConti/netscope",
)