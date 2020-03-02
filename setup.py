try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
        'description':'Game Of Live',
        'author': 'Andrew Batutin',
        'url':'www.noname.cond',
        'download_url':'www.noname.cond',
        'author_email': 'abatutin@gmail.com',
        'version':'0.1',
        'install_requires':['nose'],
        'packages':['game_of_live'],
        'scripts':[],
        'name':'game_of_live'
        ]

setup(**config)
