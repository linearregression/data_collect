import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "sqor-handle-cms",
    version = "0.0.1",
    packages = find_packages(),

    install_requires = ['requests>=2.2.1', 
    'requests-cache>=0.4.4',
    'requests-oauth2>=0.2.0',
    'riak>=2.0.3'],

    # PyPI metadata
    author = "Yoway Buorn",
    author_email = "yoway@sumologic.com",
    description = "Sumo Logic Python SDK",
    license = "PSF",
    keywords = "sqor cms mma python rest api twitter instangram facebook",
    url = "https://github.com/AmpliySocial/sqor_algo.git",
	zip_safe = True
)
