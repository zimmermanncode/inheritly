import os
import sys

from setuptools import setup


ROOT = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, ROOT)

import inheritly  # Ignore PycodestyleBear (E402)


setup(
    name='inheritly',
    version=inheritly.__version__,
    description=(
        "@inheritly >>> make MORE stuff inheritable in Python classes"),

    author="Stefan Zimmermann",
    author_email="user@zimmermann.co",
    url="https://github.com/zimmermanncode/inheritly",

    license='LGPLv3',

    packages=['inheritly'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved'
        ' :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
