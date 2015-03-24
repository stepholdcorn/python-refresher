try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'Python Refresher',
  'author': 'Steph',
  'url': '',
  'download_url': '',
  'author_email': '',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['answers'],
  'scripts': [],
  'name': 'PythonRefresher'
}

setup(**config)