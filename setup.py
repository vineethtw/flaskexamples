#!/usr/bin/env python

from distutils.core import setup
import setuptools
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(name='Flask-Examples',
      version='1.0',
      description='Flask playground for testing stuff',
      author='Vineeth Venudasan',
      author_email='vineethv@tw.com',
      url='https://www.python.org/',
      packages=['api', 'engine', 'waiting_on_tasks'],
      install_requires=reqs
     )
