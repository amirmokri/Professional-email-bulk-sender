#!/usr/bin/env python3
"""
Setup script for Email Bulk Sender
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="email-bulk-sender",
    version="1.0.0",
    author="amir mokri",
    author_email="amirali.mokri@gmail.com",
    description="A professional bulk email sender with Outlook and SMTP support",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/amirmokri/email_bulk_sender",
    project_urls={
        "Bug Reports": "https://github.com/amirmokri/email_bulk_sender/issues",
        "Source": "https://github.com/amirmokri/email_bulk_sender",
        "Documentation": "https://github.com/amirmokri/email_bulk_sender#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Communications :: Email",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.9",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "email-bulk-sender=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.csv", "*.html"],
    },
    keywords=[
        "email",
        "bulk",
        "sender",
        "outlook",
        "smtp",
        "automation",
        "marketing",
        "newsletter",
        "mass-email",
        "email-campaign",
    ],
    license="MIT",
    zip_safe=False,
)
