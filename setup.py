"""Setup module"""
from setuptools import setup, find_packages

NAME = 'bingo'
VERSION = '0.0.1'
DESC = 'Bingo Game Starter'
AUTHOR = 'Bhavesh'
EMAIL = 'bhavesh.scp@hotmail.com'
URL = ''
LIC = 'MIT'

REQUIREMENTS_LIST = []
try:
    with open('requirements.txt') as f:
        REQUIREMENTS_LIST = f.readlines()
except IOError as ex:
    print(ex)

setup(
    name=NAME,
    version=VERSION,
    description=DESC,
    long_description=open('README.md', encoding='utf-8').read(),
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'': ['LICENSE', 'README.md']},
    include_package_data=True,
    install_requires=REQUIREMENTS_LIST,
    license=LIC,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    zip_safe=True,
    entry_points={'console_scripts': ['bingo=bingo.main:main']})