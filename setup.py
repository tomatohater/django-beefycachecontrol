from setuptools import setup, find_packages
import beefycachecontrol
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')

setup(
    name = "django-beefycachecontrol",
    version = beefycachecontrol.__version__,
    description = 'Beefier Cache-Control HTTP headers created by @never_cache decorator in Django.',
    long_description = README,
    url = 'http://github.com/tomatohater/django-beefycachecontrol',
    author = 'Drew Engelson',
    author_email = 'drew@engelson.net',
    license = 'BSD',
    zip_safe = False,
    packages = find_packages(),
    include_package_data = True,
    package_data = {},
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
