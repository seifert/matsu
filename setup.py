#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='matsu',
    version='0.1.0',
    author='Jan Seifert',
    author_email='jan.seifert@fotkyzcest.net',
    description=(
        'Karate klub Matsu'
    ),
    license='BSD',
    platforms=['any'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Natural Language :: Czech',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Framework :: Django :: 1.10',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django>=1.10,<1.11',
        'markdown',
        'mysqlclient>=1.3.3',
        'Pillow',
        'pytz',
    ],
    entry_points={
        'console_scripts': [
            'manage-matsu = matsu:main',
        ]
    }
)
