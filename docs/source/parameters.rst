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
Proportion of the treatment sample, default=0.50 (i.e., equal samples size for treatment and control)

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

.. _design_effect:

design_effect
--------------------------
Default = 2.75. Please change this value according to your design.

"The design effect represents the increase in the sample size that is required under 
the RD (regression discontinuity) design to produce impact estimates with the
same level of statistical precision as the RA (random assignment) design."


Schochet, P. Z. (2008). Technical methods report: Statistical power for regression 
discontinuity designs in education evaluations (NCEE 2008-4026). Washington, 
DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S.

.. _tf:

tf
--------------------------
Year in which the outcomes are to be compared 
(i.e., "0" would indicate the year that treatment occurs; 
"1" would indicate the first year following the treatment).

.. _q:

q
--------------------------
Ratio of comparison units to experimental units (q).
(# comparison schools / # program schools)  at block level.

.. _T:

T
--------------------------
T (the number of baseline years).
The number of years prior to intervention for which the baseline, 
or pre-intervention, trend is established.