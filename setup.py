"""Setup script for Sqor Data Collection Wroker Tool"""

__author__ = 'Ed'

import os
import re
import sys
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

PACKAGES = ['sqor-data-collect']

DEPENDENCIES = ['requests>=2.2.1', 'requests-cache>=0.4.4', 'requests-oauth2>=0.2.0','riak>=2.0.3']

def GetVersion():
   """ Gets version of package from common.py
       Returns: 
         The version of library
   """
  with open(os.path.join('sqor-data-collect', 'common.py')) as versions_file:
    source = versions_file.read()
  return re.search('\\nVERSION = \'(.*?)\'', source).group(1)    

longdescription ="""
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
    name = "sqor-data-collect",
    version = GetVersion(),
    packages = find_packages(),
    install_requires = DEPENDENCIES,
    # PyPI metadata
    author = "Linear Regression",
    author_email = "wawawa@wawawa.com",
    description = longdescription,
    platform = ""
    license = "PSF",
    keywords = "data collect python twitter facebook instangram spark analysis",
    url = "https://github.com/linearregression/data_collect.git",
    zip_safe = True
)
