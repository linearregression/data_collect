import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

test_require = []
PY3 = sys.version_info[0]


requires = ['requests>=2.2.1', 'requests-cache>=0.4.4',
            'oauthlib>=0.3.8', 'six>=1.2.0',
            'riak>=2.0.3',
            'celery>=3.1.11'],

if int(PY3) == 3:
    requires += ['python3-openid>=3.0.1',
                 'requests-oauthlib>=0.3.0,<0.3.2']
else:
    requires += ['python-openid>=2.2', 'requests-oauthlib>=0.3.0']

setup(
    name = "data_collect",
    version = get_version(),
    packages = find_packages(),

    install_requires = requires,
    # PyPI metadata
    author = "Linear Regression",
    author_email = "wawawa@wawawa.com",
    description = "data collect from various channels and store into spark fof futher analysis",
    license = "PSF",
    keywords = "data collect python twitter facebook instangram spark analysis",
    url = "https://github.com/linearregression/data_collect.git",
    zip_safe = True
    test_requires = ['sure>=1.2.5', 'httpretty>=0.8.0', ',pck>=1.0.1'],
    test_suite='data_collect.tests'
)
