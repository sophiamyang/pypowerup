Simple Individual Random Assignment (IRA)
=========================================

+---------+--------------+-----------------+------------+------------+
| Ass     | Clustering   | Treatment       | Treatment  | Cluster    |
| ignment | Level        | Assignment      | Level      | Effect     |
+=========+==============+=================+============+============+
| simple  | 1            | individual      | 1          | NA         |
+---------+--------------+-----------------+------------+------------+

.. code:: ipython3

    from pypowerup import effect_size, power, sample_size

.. code:: ipython3

    # effect size, i.e., minimum detectable effect sizes (MDES):
    effect_size(design='ira', n=787, power=0.8, alpha=0.05, two_tailed=True, p=0.5, r21=0, g=0)




.. parsed-literal::

    0.19997988869985736



.. code:: ipython3

    # sample size, i.e., minimum required samples sizes (MRSS):
    sample_size(design='ira', es=0.2, power=0.8, alpha=0.05, two_tailed=True, p=0.5, r21=0, g=0)




.. parsed-literal::

    787.0



.. code:: ipython3

    # power
    power(design='ira', es=0.2, n=787, alpha=0.05, two_tailed=True, p=0.5, r21=0, g=0)




.. parsed-literal::

    0.8000799952735076



**Parameters for IRA:**
:hoverxref:`show a floating window <parameters>`
:ref:`design`

============= =============== =============== =========
Parameters    ``effect_size`` ``sample_size`` ``power``
============= =============== =============== =========
:ref:`design` ✓               ✓               ✓
n             ✓                               ✓
power         ✓               ✓               
alpha         ✓               ✓               ✓
two_tailed    ✓               ✓               ✓
p             ✓               ✓               ✓
r21           ✓               ✓               ✓
g             ✓               ✓               ✓
============= =============== =============== =========

-  **design**: please specify your study design.

-  **n**: please specify your total sample size of both treatment and
   control group.

-  **es**: minimum detectable effect sizes, default 0.25. Please change
   this value according to your design.

-  **power**: statistical power, 1- Type II error, default 0.8
   (recommended).

-  **alpha**: Type I error, default 0.05 (recommended).

-  **two_taied**: whether it is a two-tailed test or a one-tailed test.
   default True (two-tailed test).

-  **p**: proportion of the treatment sample
   :math:`\frac{n_T}{(n_T+n_C)}`, default 0.50 (i.e., equal samples size
   for treatment and control)

-  **r21**: percent of variance in outcome explained by covariates,
   default 0

-  **g**: number of covariates, default 0

**Output validation with statsmodels**

Here we used ``statsmodels`` with the same parameters to validate our
model results. Note nobs1 in ``statsmodels`` is the sample size for
treatment group, which is half of the total sample size output from our
model. Thus, we define ``nobs1=787/2=393.5`` in the models beflow.

.. code:: ipython3

    from statsmodels.stats.power import TTestIndPower

.. code:: ipython3

    # effect size
    analysis = TTestIndPower()
    analysis.solve_power(power=0.8, nobs1=393.5, ratio=1, alpha=0.05, alternative='two-sided')




.. parsed-literal::

    0.19997768751017836



.. code:: ipython3

    # sample size (statsmodels output treatment sample size only, which is the half of our computed total sample size)
    analysis.solve_power(0.2, power=0.8, nobs1=None, ratio=1, alpha=0.05,alternative='two-sided')




.. parsed-literal::

    393.4056989990335



.. code:: ipython3

    # power
    analysis.solve_power(0.2, nobs1=393.5, ratio=1.0, alpha=0.05, alternative='two-sided')




.. parsed-literal::

    0.8000942129794306



With the same parameters, we get the same results as the
``statsmodels``. However, ``statsmodels`` does not do power analysis for
more complicated designs, which we will cover next.
