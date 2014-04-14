import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "data_collect",
    version = "0.0.1",
    packages = find_packages(),

    install_requires = ['requests>=2.2.1', 
    'requests-cache>=0.4.4',
    'requests-oauth2>=0.2.0',
    'riak>=2.0.3'],

    # PyPI metadata
    author = "Linear Regression",
    author_email = "wawawa@wawawa.com",
    description = "data collect from various channels and store into spark fof futher analysis",
    license = "PSF",
    keywords = "data collect python twitter facebook instangram spark analysis",
    url = "https://github.com/linearregression/data_collect.git",
	zip_safe = True
)
