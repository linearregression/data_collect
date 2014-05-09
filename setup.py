"""Setup script for Sqor Data Collection Wroker Tool"""

__author__ = 'Ed'

import os
import re
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

PACKAGES = ['sqor-data-collect']

DEPENDENCIES = ['requests>=2.2.1', 'requests-cache>=0.4.4', 'requests-oauth2>=0.2.0', 'celery>=3.1.11', 'riak>=2.0.3', 'boto>=2.27.0']

def get_version():
    """ Gets version of package from common.py
       Returns:
         The version of library
    """
    with open(os.path.join(os.getcwd(), 'tasks', 'common.py')) as version_file:
        source = version_file.read()
    return (re.search('\\nVERSION = \'(.*?)\'', source)).group(1)


long_description = """
===========================================
Sqor Data Collection Worker Tool
===========================================

At a beginning of a lifecycle, Worker process will register itself, to RabbitMQ for announce its presence.
This is done through a pre-agreed on exchange. The conept is no different than an anouncement on a control channel.

Each Worker process does not have much intelligence other than execute "task" it received
from RabbitMQ server, perform data collection and store to Apache HDFS for further process/data analysis.

Worker will ignore commands it does not understand. It will store state of each "task" into
task status store ("Riak") for querying.

You can find more information 
`here <https://github.com/linearregression/data_collect.git>`_.

Installation
============

You have two options for installing:

* Install with a tool such as pip::

  $ sudo pip install sqor-data-collect

* Install manually after downloading and extracting the tarball::

  $ sudo python setup.py install

Examples
========


Santiy Test
==========


"""

setup(
    name='sqor-data-collect',
    version=get_version(),
    packages=find_packages()exclude=['tests', 'tests.*'],
    install_requires=DEPENDENCIES,
    # PyPI metadata
    author='Linear Regression',
    author_email='wawawa@wawawa.com',
    description=long_description,
    platforms='any',
    license='PSF',
    keywords='data collect python twitter facebook instangram spark analysis',
    url='https://github.com/linearregression/data_collect.git',
    zip_safe=True
)
