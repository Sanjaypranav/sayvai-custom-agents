import setuptools
from setuptools import setup, find_packages
from agents import __version__

core_requirements = [
    "langchain~=0.0.271",
    "openai",
]

setup(
    name="agents",
    version=__version__,
    author="Langchain",
    author_email="kedareeshwarsekar@sayvai.io",
    description="Agents for Langchain",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=core_requirements,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    os_type=["linux", "Windows", "MacOS", "Unix"],
)