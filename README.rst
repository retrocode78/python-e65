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
.. |docs| image:: https://readthedocs.org/projects/python-pe65/badge/?style=flat
    :target: https://python-pe65.readthedocs.io/
    :alt: Documentation Status

.. |codecov| image:: https://codecov.io/gh/retro78/python-pe65/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/retro78/python-pe65

.. |commits-since| image:: https://img.shields.io/github/commits-since/retro78/python-pe65/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/retro78/python-pe65/compare/v0.0.0...master



.. end-badges

Yet another 6502 emulator

* Free software: MIT license

Installation
============

::

    pip install pe65

You can also install the in-development version with::

    pip install https://github.com/retro78/python-pe65/archive/master.zip


Documentation
=============


https://python-pe65.readthedocs.io/


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
