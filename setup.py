import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Color_Match",
    version="0.0.1",
    author="Michael Woods",
    author_email="mail@michaelwoods.us",
    description="Utility functions for generating perceptually equivalent colors to a known spectrum using specific, available, wavelength sources.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carpdiem/Color-Match",
    license="MIT",
    packages=['Color_Match'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'numpy',
        'wheel',
    ],
)
