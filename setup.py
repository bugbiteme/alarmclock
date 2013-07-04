try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Alarm clock which won\'t shup up until you turn on the light',
    'author': 'Leon Levy',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'leon.s.levy@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['alarmclock'],
    'scripts': [],
    'name': 'alarmclock'
}

setup(**config)
