import os
from setuptools import setup, find_packages


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

version = __import__('tradewave').__version__

setup(
    name='tradewave',
    py_modules = ['tradewave'],
    description='Python wrapper for the Tradewave API',
    version=version,
    long_description=README,
    author='tradewave',
    zip_safe = False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['six', 'requests'],
    license='MIT',
    keywords='tradewave API',
    url='https://github.com/tradewave/tradewave-client',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Topic :: Office/Business :: Financial :: Investment'
    ],
)