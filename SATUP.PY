"""
Setup configuration for Jarvis Code Analyzer
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = []
with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="jarvis-code-analyzer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A voice-activated Python code analyzer using AST",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/jarvis-code-analyzer",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/jarvis-code-analyzer/issues",
        "Documentation": "https://github.com/yourusername/jarvis-code-analyzer#readme",
        "Source Code": "https://github.com/yourusername/jarvis-code-analyzer",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    keywords=[
        "code-analysis",
        "ast",
        "static-analysis",
        "voice-assistant",
        "python-analyzer",
        "complexity-metrics",
        "code-quality",
        "jarvis",
        "speech-recognition",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
            "isort>=5.12",
        ],
    },
    entry_points={
        "console_scripts": [
            "jarvis-analyze=code_analyzer_demo:interactive_menu",
            "jarvis-voice=jarvis_code_analyzer:main_loop",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
