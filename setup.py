"""Setup script for the Unified AI Application."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="unified-ai",
    version="1.0.0",
    author="Entity Project",
    description="A unified interface to multiple AI models and services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/irishbyblood/entity-project",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-dotenv>=1.0.0",
        "httpx>=0.25.0",
        "certifi>=2023.0.0",
    ],
    extras_require={
        "openai": ["openai>=1.0.0"],
        "anthropic": ["anthropic>=0.18.0"],
        "google": ["google-generativeai>=0.3.0"],
        "mistral": ["mistralai>=0.1.0"],
        "watson": ["ibm-watson>=7.0.0", "ibm-cloud-sdk-core>=3.16.0"],
        "vision": [
            "ultralytics>=8.0.0",
            "torch>=2.0.0",
            "torchvision>=0.15.0",
            "transformers>=4.30.0",
            "opencv-python>=4.8.0",
            "Pillow>=10.0.0",
            "numpy>=1.24.0",
        ],
        "all": [
            "openai>=1.0.0",
            "anthropic>=0.18.0",
            "google-generativeai>=0.3.0",
            "mistralai>=0.1.0",
            "ibm-watson>=7.0.0",
            "ibm-cloud-sdk-core>=3.16.0",
            "ultralytics>=8.0.0",
            "torch>=2.0.0",
            "torchvision>=0.15.0",
            "transformers>=4.30.0",
            "opencv-python>=4.8.0",
            "Pillow>=10.0.0",
            "numpy>=1.24.0",
            "requests>=2.31.0",
            "aiohttp>=3.9.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "unified-ai=main:main",
        ],
    },
)
