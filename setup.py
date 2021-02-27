from moneythreads import __author__, __email__, __name__, __url__, __version__
from setuptools import find_packages, setup

setup(
    name=__name__,
    version=__version__,

    url=__url__,
    author=__author__,
    author_email=__email__,

    packages=find_packages(),
    include_package_data=True,
    scripts=['scripts/manage.py'],

    install_requires=(
        'django>=3.1.7',
    )
)
