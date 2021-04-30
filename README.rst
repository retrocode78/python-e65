========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        | |codecov|
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-e65/badge/?style=flat
    :target: https://python-e65.readthedocs.io/
    :alt: Documentation Status

.. |codecov| image:: https://codecov.io/gh/retrocode78/python-e65/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/retrocode78/python-e65

.. |commits-since| image:: https://img.shields.io/github/commits-since/retrocode78/python-e65/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/retrocode78/python-e65/compare/v0.0.0...main



.. end-badges

Yet another 6502 emulator

* Free software: MIT license

Installation
============

::

    pip install e65

You can also install the in-development version with::

    pip install https://github.com/retrocode78/python-e65/archive/master.zip


Documentation
=============


https://python-e65.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
