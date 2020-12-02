"""
lambdata - a collection of Data Science Helper functions for
LambdaSchool Data Science Unit 3 - Sprint 1.
"""
import setuptools


REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='lambdatarencurry',
    version='0.0.4',
    license='MIT License',
    description='Lambda School U3S1 Assignments',
    long_description=LONG_DESCRIPTION,
    long_description_content='text/markdown',
    url='https://github.com/ren-curry/lambdata_rencurry',
    platforms=['MacOs'],
    packages=setuptools.find_packages(),  # How we find our REQUIRED packages
    python_requires=">=3.6",  # What versions of Python we are compatible with
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]

)
