
from setuptools import setup, find_packages


setup(
    name="hello-world-takeoff7",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "hello=hello_world.main:say_hello",
        ],
    },
    author="TakeOff",
    description="A simple hello world Python package",
    url="https://http://github.com/Take-Off-7/Devops",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
