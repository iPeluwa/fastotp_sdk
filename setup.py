from setuptools import setup, find_packages

setup(
    name="fastotp_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "httpx",
    ],
    author="Oluwapeluwa Ibrahim",
    author_email="ipeluwa@gmail.com",
    description="A Python SDK for FastOTP API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ipeluwa/fastotp_sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
