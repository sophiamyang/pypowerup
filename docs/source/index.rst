.. pypowerup documentation master file, created by
   sphinx-quickstart on Sat Sep 19 18:14:23 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pypowerup's documentation!
=====================================


.. image:: https://img.shields.io/pypi/v/pypowerup.svg
        :target: https://pypi.python.org/pypi/pypowerup

.. image:: https://img.shields.io/travis/sophiamyang/pypowerup.svg
        :target: https://travis-ci.org/sophiamyang/pypowerup

.. image:: https://readthedocs.org/projects/pypowerup/badge/?version=latest
        :target: https://pypowerup.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

``pypowerup`` is the Python implementation for the research article "PowerUp!: A Tool for Calculating Minimum Detectable 
Effect Sizes and Minimum Required Sample Sizes for Experimental and Quasi-experimental Design Studies (Dong & Maynard, 2013)". It is a 
power analysis tool for 21 experimental and quasi-experimental designs. 


Given study design, ``pypowerup`` computes minimum detectable effect sizes ``effect_size``, power ``power``, 
and minimum required samples sizes ``sample size``.

To install pypowerup, run this command in your terminal:

.. code-block:: console

    $ pip install pypowerup


To use the functions: 

.. code:: python

   from pypowerup import effect_size, power, sample_size

Credit and disclaimer
=====================
This document is heavily built on https://www.causalevaluation.org/uploads/7/3/3/6/73366257/powerup.xlsm. 
All the design and variable explanations are from this sheet.

Individual Random Assignment Designs 
====================================

.. _my-reference-label:

Section to cross-reference
--------------------------

This is the text of the section.

It refers to the section itself, see :ref:`my-reference-label`.
:ref:`available settings <my-reference-label>`

:ref:`available settings <parameters>`

This will :hoverxref:`show a floating window <parameters>` in the linked words.


.. toctree::
   :maxdepth: 2
 
   IRA 
   BIRA

Cluster Random Assignment Designs 
=================================

.. toctree::
   :maxdepth: 2

   CRA
   BCRA

Quasi-experimental Designs 
==========================

.. toctree::
   :maxdepth: 2


   RD
   ITS



References
==========
Dong, N. & Maynard, R. A. (2013). PowerUp!: A tool for calculating minimum detectable
effect sizes and minimum required sample sizes for experimental and quasi- experimental design studies, Journal of Research on Educational Effectiveness, 6(1), 24-67. doi: 10.1080/19345747.2012.673143.
https://www.causalevaluation.org/uploads/7/3/3/6/73366257/powerup.xlsm

Bulus, M., Dong, N., Kelcey, B., & Spybrook, J. (2019). PowerUpR: Power Analysis Tools for Multilevel Randomized Experiments. R package version 1.0.4. https://CRAN.R-project.org/package=PowerUpR