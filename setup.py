#!/usr/bin/env python
from setuptools import setup

def get_version():
    with open("demorphy/version.py", "rt") as f:
        return f.readline().split("=")[1].strip(' "\n')


tests_requires = [
    "pytest"
]

install_requires = [
    "dawg (>= 0.7.8)"
] 


setup(
    name="demorphy",
    version=get_version(),
    author="Duygu Altinok",
    author_email="duygu.altinok12@gmail.com",
    url="https://github.com/DuyguA/DEMorphy/",

    license="MIT",
    description="German morphological analyzer",
    long_description=open("README.md").read(),
    
    packages=[
        "demorphy",
        "demorphy.data",
        "demorphy.cache",
        "demorphy.morph_dict",
    ],
    requires=["dawg (>= 0.7.8)"],
    tests_require=tests_requires,
    install_requires=install_requires,
    test_suite="tests",
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: German",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Linguistic",
    ],
)
