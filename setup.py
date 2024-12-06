from setuptools import setup, find_packages

setup(
    name="finance_manager",
    version="1.0.0",
    description="A personal finance management desktop application built with PyQt5 and SQLite.",
    author="Lukman Olamide",
    author_email="olamidelukman3@gmail.com",
    url="",
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=[
        "PyQt5>=5.15.0",
        "matplotlib>=3.3.0",
        "sqlite3", 
    ],
    entry_points={
        'console_scripts': [
            'finance-manager=app.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Office/Business :: Financial",
    ],
    python_requires='>=3.7',
    include_package_data=True,
)