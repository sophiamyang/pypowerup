:orphan:

.. _design:

design
--------------------------
please specify your study design.

.. _n:

n
--------------------------
Number of level 1 units or average Sample Size for Level 1. 
For example, if the design is IRA, n is the total sample size of both treatment and control group.

.. _es:

es
--------------------------
Minimum detectable effect sizes, default=0.25. Please change this value according to your design.

.. _alpha:

alpha
--------------------------
Type I error, default 0.05 (recommended).


.. _power:

power
--------------------------
Statistical power, 1- Type II error, default 0.8 (recommended).

.. _two_tailed:

two_tailed
--------------------------
Whether it is a two-tailed test or a one-tailed test. default True (two-tailed test).

.. _p:

p
--------------------------
Proportion of the treatment sample :math:`\frac{n_T}{(n_T+n_C)}`, default=0.50 (i.e., equal samples size for treatment and control)

.. _r21:

r21
--------------------------
Proportion of variance in Level 1 outcome explained by the Level 1 covariates, default=0.

.. _g:

g
--------------------------
Number of covariates at the highest level, default=0.

.. _J:

J
--------------------------
Number of level 2 units or average Sample Size for Level 2. 

K
--------------------------
Number of level 3 units or average Sample Size for Level 3. 

L
--------------------------
Number of level 4 units. 

.. _r22:

r22
--------------------------
Proportion of variance in Level 2 outcome explained by Level 2 covariates.

.. _rho2:

rho2
--------------------------
Proportion of variance in outcome among Level 2 units.

.. _omega2:

omega2
--------------------------
Level 2 treatment effect heterogeneity:  variance in treatment effect across Level 2 units, standardized by the Level-2 outcome variance

.. _r2t2:

r2t2
--------------------------
Proportion of between block variance in treatment effect explained by Level 2 covariates

.. _r23:

r23
--------------------------
Proportion of variance in Level 3 outcome explained by Level 3 covariates.

.. _rho3:
rho3
--------------------------
Proportion of variance in outcome among Level 3 units.

.. _omega3:

omega3
--------------------------
Level 3 treatment effect heterogeneity:  variance in treatment effect across Level 3 units, standardized by the Level-3 outcome variation.

.. _r2t3:

r2t3
--------------------------
Proportion of between block variance in treatment effect explained by Level 3 covariates.

.. _r24:

r24
--------------------------
Proportion of variance in Level 4 outcome explained by Level 4 covariates.

.. _rho4:
rho4
--------------------------
Proportion of variance in outcome among Level 4 units.

.. _omega3:

omega4
--------------------------
Level 4 treatment effect heterogeneity:  variance in treatment effect across Level 4 units, standardized by the Level-4 outcome variation.

.. _r2t4:

r2t4
--------------------------
Proportion of between block variance in treatment effect explained by Level 4 covariates.



