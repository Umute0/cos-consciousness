from setuptools import setup, find_packages

setup(
    name="cos-consciousness",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "tensorflow",
        "matplotlib",
        "pandas",
        "mne"
    ],
    author="Umut Elveren",
    author_email="umetelveren0@gmail.com",
    description="Consciousness Simulation Protocol with neural networks and EEG",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Umute0/cos-consciousness",
    license="MIT"
)
