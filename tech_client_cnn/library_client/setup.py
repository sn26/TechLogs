import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = "library-client-cnn"
DESCRIPTION = "Implements methods an services with to interact with the CNN SERVER API."
AUTHOR = ""
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "1.1.0"
REQUIRED = [
    "requests"
]
EXTRAS_REQUIRED = {}
ENTRY_POINTS = {}
PACKAGE_DATA = {
    "library_client_cnn": ["schemas/*.json"]
}

# Get the current path
here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description, if not there use the short description.
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        LONG_DESCRIPTION = '\n' + f.read()
except IOError:
    LONG_DESCRIPTION = DESCRIPTION

# Actual setup function:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=["docs", "docs.*", "tests", "tests.*"]),
    package_data=PACKAGE_DATA,
    install_requires=REQUIRED,
    extras_require=EXTRAS_REQUIRED,
    entry_points=ENTRY_POINTS
)
