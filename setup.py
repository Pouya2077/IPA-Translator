from setuptools import setup, find_packages

setup(
    name="ipa_translator_backend",
    packages=find_packages(where="backend"),
    package_dir={"": "backend"},
)