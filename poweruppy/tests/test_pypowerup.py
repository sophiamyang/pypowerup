# fmt: off
from pypowerup import effect_size, power, sample_size


def test_pypowerup():
    assert round(effect_size('ira', n=400), 2) == 0.28
    assert round(effect_size('ira', n=400, r21=0.5), 2) == 0.20
    assert sample_size('ira') == 787
    assert sample_size('ira', r21=0.8, g=1) == 159
    assert round(effect_size(design = "bira2_1c", n=80, J=14),2)== 0.17
    assert round(effect_size(design = "bira2_1c", n=80, J=14, r21=0.2, g=1),2)== 0.15
    assert sample_size(design = "bira2_1c", es=0.50, n=5, r21=0) == 26
    assert sample_size(design = "bira2_1c", es=0.40, n=5, r21=0.5) == 20
    assert round(effect_size(design = "bira2_1f", n=80, J=480),3) == 0.029
    assert round(effect_size(design = "bira2_1f", n=10, J=200, r21=0.05),3) == 0.122
    assert sample_size(design = "bira2_1f", es=0.50, n=10, r21=0, g=0)  == 13
    assert sample_size(design = "bira2_1f", es=0.50, n=6, r21=0.2, g=0)  == 17
    assert round(effect_size(design = "bira2_1r", n=80, J=480, rho2=0.35, omega2=0.1), 3) == 0.033
    assert round(effect_size(design = "bira2_1r", n=10, J=500, rho2=0.35, omega2=0.1), 3) == 0.068
    assert sample_size(design = "bira2_1r", n=10, g=1, r21=0.5, omega2=0.5, rho2=0.25, es=0.5) == 11
    assert sample_size(design = "bira2_1r", n=4, g=2, r21=0.5, omega2=0.5, rho2=0.25, es=0.5) == 18
    assert round(effect_size(design = "bira3_1r", n=80, J=10, K=100, rho3=0.2, rho2=0.15, omega3=0.1, omega2=0.1),3)==0.045
    assert round(effect_size(design = "bira3_1r", n=40, J=100, K=200, rho3=0.2, rho2=0.15, omega3=0.1, omega2=0.1),3)==0.029
    assert sample_size(design = "bira3_1r", es=0.15, n=20, J=30, rho3=0.1, rho2=0.15, omega3=0.1, omega2=0.1, r21=0.5) == 7
    assert sample_size(design = "bira3_1r", es=0.15, n=10, J=10, rho3=0.1, rho2=0.15, omega3=0.1, omega2=0.1, r21=0.5,r2t2=0,g=1) == 12
    assert round(effect_size(design = "bira4_1r", n=10, J=4, K=4, L=20, rho4=0.05, rho3=0.15, rho2=0.15, 
                omega4=0.5, omega3=0.5, omega2=0.5, r21=0.5, r2t2=0.5, r2t3=0.5, r2t4=0.5, g=1),3)==0.119
    assert round(effect_size(design = "bira4_1r", n=20, J=4, K=4, L=20, rho4=0.05, rho3=0.15, rho2=0.15, 
                omega4=0.5, omega3=0.5, omega2=0.5, r21=0.5, r2t2=0.5, r2t3=0.5, r2t4=0.5, g=1),3)==0.111
    assert sample_size(design = "bira4_1r", es=0.20, n=10, J=4, K=4, rho4=0.05, rho3=0.15, rho2=0.15, 
                omega4=0.5, omega3=0.5, omega2=0.5, r21=0.5, r2t2=0.5, r2t3=0.5, r2t4=0.5, g=1) == 9 
    assert sample_size(design = "bira4_1r", es=0.25, rho4=.05, rho3=.15, rho2=.15, omega4=.50, omega3=.50, omega2=.50, n=10, J=2, K=10) == 8
    assert round(power(design = "bira3_1r", rho3=.20, rho2=.15, omega3=.10, omega2=.10, n=69, J=10, K=100, es=.04,p=.50, r21=0, r2t2=0, r2t3=0, g=0),2)==0.70
    assert round(power(design = "bira4_1r", es=0.10, rho4=.05, rho3=.15, rho2=.15, omega4=.50, omega3=.50, omega2=.50, n=10, J=4, L=27, K=4),2)==0.50

    assert round(effect_size(design = "rd2_1f", n=55, J=20, r21=0.5, g=1, design_effect=2.75),3) == 0.198
    assert sample_size(design = "rd2_1f", n=20, es=0.20, r21=0.5, g=1, design_effect=2.75) == 54
    assert sample_size(design = "rd2_1f", n=20, es=0.10, r21=0.5, g=1, design_effect=2.75) == 216
    assert round(effect_size(design = "rd2_1r", n=50, J=40, r21=0.5, g=1, r2t2=0.1, omega2=0.2, rho2= 0.15, design_effect=2.75),3)==0.158
    assert sample_size(design = "rd2_1r", es=0.2, rho2=0.15, omega2=0.2, r21=0.5, r2t2=0.1, g=1, n=40, design_effect=2.75) == 30
    assert sample_size(design = "rd2_1r", es=0.1, rho2=0.15, omega2=0.2, r21=0.5, r2t2=0.1, g=1, n=60, design_effect=2.75) ==84
    assert round(effect_size(design = "rdc_2r", rho2=0.15, r21=0.5, r22=0.5, g=1, n=55, J=179, design_effect=2.75),3) ==0.201
    assert round(effect_size(design = "rdc_2r", rho2=0.15, r21=0.5, r22=0, g=1, n=55, J=200, design_effect=2.75),3) ==0.262
    assert sample_size(design = "rdc_2r", rho2=0.15, r21=0.5, r22=0.5, g=1, n=20, design_effect=2.75) == 210
    assert sample_size(design = "rdc_2r", rho2=0.15, r21=0.5, r22=0, g=1, n=200, design_effect=2.75) == 330
    assert round(effect_size(design = "rdc_3r", rho3=0.15, rho2=0.15, r21=0.5, r22=0.5, r23=0.5,  g=1, n=18, J=3, K=230, design_effect=2.75), 3) == 0.201
    assert sample_size(design = "rdc_3r", es=0.25, rho3=0.15, rho2=0.10, r21=0.5, r22=0.5, r23=0.5,  g=1, n=20, J=4, K=230, design_effect=2.75) == 129
    assert round(effect_size(design = "rd3_2f", rho2=0.15, r21=0.5, r22=0.5, g=0, n=18, J=3, K=71, design_effect=2.75),3) == 0.201
    assert round(effect_size(design = "rd3_2f", rho2=0.55, r21=0.3, r22=0.2, g=0, n=20, J=5, K=30, design_effect=2.75),3) == 0.516
    assert round(effect_size(design = "rd3_2r", rho3=0.15, rho2=0.15, omega3=1, r21=0.5, r22=0.5,r2t3=0.5, r23=0.5, g=0, K=80, n=18, J=3, design_effect=2.75),3) == 0.206
    assert sample_size(design = "rd3_2r", es=0.2, rho3=0.15, rho2=0.15, omega3=1, r21=0.5, r22=0.5,r2t3=0.5, r23=0.5, g=0, n=10, J=4, design_effect=2.75) == 76
    assert round(effect_size(design='cra2_2r', rho2=0.15, r21=0.40, r22=0.53, g=1, n=100, J=40), 3) == 0.250
    assert sample_size(design='cra2_2r', es=0.45, rho2=0.02, r21=0.01, r22=0.13, g=4, n=60, J=10) == 10
    assert round(effect_size(design='cra3_3r', rho3=0.38, rho2=0.10, r21=0.37, r22=0.53, r23=0.87, g=1, n=20, J=2, K=66), 3) ==0.199
    assert sample_size(design='cra3_3r', es=0.20, rho3=0.38, rho2=0.10, r21=0.37, r22=0.53, r23=0.87, g=1, n=20, J=2) == 66
    assert round(effect_size(design='cra4_4r', rho4=0.05, rho3=0.05, rho2=0.10, r21=0.50, r22=0.50, r23=0.50, r24=0.50, g=1, n=10, J=2, K=3, L=20),3) == 0.292
    assert sample_size(design='cra4_4r', es=0.20, rho4=0.05, rho3=0.05, rho2=0.10, r21=0.50, r22=0.50, r23=0.50, r24=0.50, g=1, n=5, J=2, K=3) == 45
    assert round(effect_size(design='bcra3_2f', rho2=0.10, r21=0.50, r22=0.50, g=1, n=20, J=44, K=5),3) == 0.102
    assert sample_size(design='bcra3_2f', es=0.15, rho2=0.30, r21=0.50, r22=0.50, g=1, n=20, J=40) == 6 
    assert round(effect_size(design='bcra3_2r', rho3=0.38, rho2=0.10, omega3=0.50, r21=0.37, r22=0.53, r2t3=0, g=0, n=20, J=2, K=64),3) == 0.200
    assert sample_size(design='bcra3_2r', es=0.20, rho3=0.38, rho2=0.10, omega3=0.50, r21=0.37, r22=0.53, r2t3=0, g=0, n=20, J=2) == 64
    assert round(effect_size(design='bcra4_2r', rho4=0.05, rho3=0.15, rho2=0.15, omega4=0.5, omega3=0.5, r21=0.5, r22=0.5, r2t3=0.5, r2t4=0.5, g=0, n=10, J=4, K=4, L=20), 3)==0.146
    assert sample_size(design='bcra4_2r', es=0.2, rho4=0.05, rho3=0.15, rho2=0.15, omega4=0.5, omega3=0.5, r21=0.5, r22=0.5, r2t3=0.5, r2t4=0, g=1, n=10, J=4, K=10) == 10
    assert round(effect_size(design='bcra4_3f', rho3=0.15, rho2=0.15, r21=0.5, r22=0.5, r23=0.5, g=2, n=10, J=4, K=4, L=15),3) == 0.240
    assert sample_size(design='bcra4_3f', es=0.30, rho3=0.15, rho2=0.15, r21=0.5, r22=0.5, r23=0.5, g=1, n=10, J=4, K=4) == 10
    assert round(effect_size(design='bcra4_3r', rho4=0.05, rho3=0.15, rho2=0.15, omega4=0.5, r21=0.5, r22=0.5, r23=0.5, r2t4=0.5, g=3, n=10, J=4, K=20, L=20),3) == 0.121
    assert sample_size(design='bcra4_3r', es=0.20, rho4=0.10, rho3=0.10, rho2=0.10, omega4=0.5, r21=0.5, r22=0.5, r23=0.5, r2t4=0.5, g=3, n=10, J=4, K=10) == 13
    assert round(effect_size(design = "its_nocompare", rho2=0.03, T=5, n=75, K=10, r22=0, tf=2, g=0),2) ==0.37
    assert round(effect_size(design = "its_wcompare", rho2=0.03, T=5, n=75, K=10, r22=0, tf=2, g=0, q=2),2) ==0.45
    assert sample_size(design = "its_wcompare", es=0.4, rho2=0.03, T=5, n=75, r22=0, tf=2, g=0, q=2, two_tailed=False) ==10
