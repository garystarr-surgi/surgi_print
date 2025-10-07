from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name='surgi_print',
    version='0.0.5',
    description='CUPS direct printing for Delivery Notes.',
    author='Gary Starr',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True
    install_requires=install_requires,
)
