from setuptools import setup, find_packages

import sys

# Check python version
if sys.version_info < (2, 7, 0):
    sys.stderr.write("kippo-extra requires Python 2.7 or newer.\n")
    sys.exit(1)

# Run setup
setup(
    name="kippo-extra",
    version="1.0.1",
    author="Bas Stottelaar",
    author_email="basstottelaar@gmail.com",
    url="https://github.com/basilfx/kippo-extra",
    description="Set of extra commands for the kippo SSH honeypot daemon",
    long_description=open("README.rst").read(),
    license=open("LICENSE").read(),
    packages=find_packages(),
    package_data={"": ["LICENSE", "README.rst"], "kippo_extra": ["patches/*.patch"]},
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security'
    ),
)