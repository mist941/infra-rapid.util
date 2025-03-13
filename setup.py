from setuptools import setup, find_packages

setup(
    name="fast-infra-setup",
    version="0.1.0",
    author="Ivan Statkevich",
    author_email="statkevich.ivan@gmail.com",
    description="Fast Infrastructure Setup",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mist941/fast-infrastructure-setup",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0, <9.0.0",
    ],
    entry_points={
        "console_scripts": [
            "fis=src.cli:cli",
        ],
    },
    python_requires=">=3.10",
    project_urls={
        "Bug Reports":
        "https://github.com/mist941/fast-infrastructure-setup/issues",
        "Source": "https://github.com/mist941/fast-infrastructure-setup",
    },
)
