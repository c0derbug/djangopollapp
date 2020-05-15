import setuptools
from . import djangopollapp

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='djangopollapp',
    version=djangopollapp.__version__,
    author="Coder Bug",
    author_email="thecoderbug@gmail.com",
    description='A simple polls application',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c0derbug/djangopollapp.git",
    install_requires=[
        'Django==2.2.10',
        'djangorestframework==3.11.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5.2',
)