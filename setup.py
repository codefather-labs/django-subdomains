#!/usr/bin/env python3
import os
import sys

from setuptools import find_packages, setup


def get_version():
    from subdomains import __version__
    return '.'.join(map(str, __version__))


try:
    version = get_version()
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__, 'subdomains')))
    version = get_version()

install_requires = ['django']
tests_require = install_requires + ['mock']

setup(name='django-subdomains',
      version=version,
      url='https://github.com/codefather-labs/django-subdomains/',
      author='www.codefather.dev',
      description="Subdomain tools for the Django framework, including "
                  "subdomain-based URL routing.",
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      tests_require=tests_require,
      test_suite='subdomains.tests.run',
      zip_safe=False,
      license='GNU General Public License v3.0 License',
      )
