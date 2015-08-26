import os

from codecs import open
from setuptools import setup

import youtube_thumbnail

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-youtube-thumbnail',
    version=youtube_thumbnail.__version__,
    author='Ryan Senkbeil',
    author_email='ryan.senkbeil@gsdesign.com',
    description='Quickly pull the highest resolution thumbnail image available for a YouTube video.',
    long_description=long_description,
    url='https://github.com/gsmke/django-youtube-thumbnail',
    license='BSD',
    packages=['youtube_thumbnail'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'django-classy-tags >=0.6.2, <0.7',
        'pafy >=0.3.74, <0.4',
        'six',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
