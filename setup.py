import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aioshell",
    version="0.0.1",
    author="Flampt",
    license="MIT",
    description="A tool that allows you to control your machine's terminal from discord.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlamptX/aioshell",
    project_urls={
        "Source": "https://github.com/FlamptX/aioshell"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=[],
    keywords='aioshell remote shell discord',
    packages=setuptools.find_packages(include=['aioshell', 'aioshell.*']),
    python_requires=">=3.6",
)