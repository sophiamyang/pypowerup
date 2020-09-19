from scipy import stats
import numpy as np
from innerscope import scoped_function
import sys

class ConvergenceError(Exception):
    pass

def multiplier(alpha, v, power, two_tailed):
    """
    calculate multiplier
    v: degree of freedom
    """
    if two_tailed:
        alpha *= 0.5
    t1 = stats.t.ppf(1-alpha, v)    
    t2 = np.abs(stats.t.ppf(1-power, v))
    if power >= 0.5:
        m = t1 + t2
    else:
        m = t1 - t2
    return m

design_degree_freedom = {
    "ira": lambda: n - g - 2,
    "bira2_1c": lambda: J * (n - 1) - g - 1,
    "bira2_1f": lambda: J * (n - 2) - g,
    "rd2_1f": lambda: J * (n - 2) - g,
    "bira2_1r": lambda: J - g - 1,
    "rd2_1r": lambda: J - g - 1, 
    "bira3_1r": lambda: K - g - 1,
    "bira4_1r": lambda: L - g - 1,
    "cra2_2r": lambda: J - g - 2,
    "cra3_3r": lambda: K - g - 2,
    "cra4_4r": lambda: L - g - 2,
    "bcra3_2f": lambda: K * (J - 2) - g,
    "bcra3_2r": lambda: K - g - 1,
    "bcra4_2r": lambda: L - g - 1,
    "bcra4_3f": lambda: L * (K - 2) - g,
    "bcra4_3r": lambda: L - g - 1,
    "rdc_2r": lambda: J - g - 2,
    "rdc_3r": lambda: K - g - 2,
    "rd3_2f": lambda: K * (J - 1) - g,
    "rd3_2r": lambda: K - g - 1,
    "its_nocompare": lambda: K * T - g - 1,
    "its_wcompare": lambda: K * T - g - 1,

    }

def degree_freedom_equation(design):
    d = sys._getframe().f_back.f_locals
    calc = design_degree_freedom[design]
    func = scoped_function(calc, d)
    return func().return_value

design_sse = {
    "ira": lambda: np.sqrt((1-r21)/(p*(1-p)*n)),
    "bira2_1c": lambda: np.sqrt((1-r21)/(p*(1-p)*J*n)),
    "bira2_1f": lambda: np.sqrt((1-r21)/(p*(1-p)*J*n)),
    "rd2_1f": lambda: np.sqrt((1-r21)/(p*(1-p)*J*n))*np.sqrt(design_effect),
    "bira2_1r": lambda: np.sqrt(rho2*omega2*(1-r2t2)/J + (1-rho2)*(1-r21)/(p*(1-p)*J*n)),
    "rd2_1r": lambda: np.sqrt(rho2*omega2*(1-r2t2)/J + (1-rho2)*(1-r21)*design_effect/(p*(1-p)*J*n)), 
    "bira3_1r": lambda: np.sqrt(
                rho3*omega3*(1-r2t3)/K + 
                rho2*omega2*(1-r2t2)/(J*K) + 
                (1-rho2-rho3)*(1-r21)/(p*(1-p)*J*K*n)),
    "bira4_1r": lambda: np.sqrt(
                rho4*omega4*(1-r2t4)/L + 
                rho3*omega3*(1-r2t3)/(K*L) + 
                rho2*omega2*(1-r2t2)/(J*K*L) + 
                (1-rho2-rho3-rho4)*(1-r21)/(p*(1-p)*J*K*L*n)),
    "cra2_2r": lambda: np.sqrt(rho2*(1-r22)/(p*(1-p)*J)+(1-rho2)*(1-r21)/(p*(1-p)*J*n)),
    "cra3_3r": lambda: np.sqrt(rho3*(1-r23)/(p*(1-p)*K)+rho2*(1-r22)/(p*(1-p)*J*K)+(1-rho3-rho2)*(1-r21)/(p*(1-p)*J*K*n)), 
    "cra4_4r": lambda: np.sqrt(rho4*(1-r24)/(p*(1-p)*L)+
                               rho3*(1-r23)/(p*(1-p)*K*L)+
                               rho2*(1-r22)/(p*(1-p)*J*K*L)+
                               (1-rho4-rho3-rho2)*(1-r21)/(p*(1-p)*J*K*L*n)),
    "bcra3_2f": lambda: np.sqrt(rho2*(1-r22)/(p*(1-p)*J*K)+(1-rho2)*(1-r21)/(p*(1-p)*J*K*n)),
    "bcra3_2r": lambda: np.sqrt(rho3*omega3*(1-r2t3)/K+rho2*(1-r22)/(p*(1-p)*J*K)+(1-rho3-rho2)*(1-r21)/(p*(1-p)*J*K*n)),
    "bcra4_2r": lambda: np.sqrt(rho4*omega4*(1-r2t4)/L +
                rho3*omega3*(1-r2t3)/(K*L) +
                rho2*(1-r22)/(p*(1-p)*J*K*L) +
                (1-rho4-rho3-rho2)*(1-r21)/(p*(1-p)*J*K*L*n)),
    "bcra4_3f": lambda: np.sqrt(rho3*(1-r23)/(p*(1-p)*K*L)+
                                rho2*(1-r22)/(p*(1-p)*J*K*L)+(1-rho3-rho2)*(1-r21)/(p*(1-p)*J*K*L*n)),
    "bcra4_3r": lambda: np.sqrt(rho4*omega4*(1-r2t4)/L+rho3*(1-r23)/(p*(1-p)*K*L)+
                                rho2*(1-r22)/(p*(1-p)*J*K*L)+(1-rho4-rho3-rho2)*(1-r21)/(p*(1-p)*J*K*L*n)),
    "rdc_2r": lambda: np.sqrt(design_effect)*np.sqrt(rho2*(1-r22)/(p*(1-p)*J)+
                                                     (1-rho2)*(1-r21)/(p*(1-p)*J*n)),     
    "rdc_3r": lambda: np.sqrt(design_effect)*np.sqrt(rho3*(1-r23)/(p*(1-p)*K)+
                                                     rho2*(1-r22)/(p*(1-p)*J*K)+
                                                     (1-rho2-rho3)*(1-r21)/(p*(1-p)*J*K*n)), 
    "rd3_2f": lambda: np.sqrt(design_effect)*np.sqrt(rho2*(1-r22)/(p*(1-p)*J*K)+
                                                     (1-rho2)*(1-r21)/(p*(1-p)*J*K*n)), 
    "rd3_2r": lambda: np.sqrt(rho3*omega3*(1-r2t3)/K+ design_effect*rho2*(1-r22)/(p*(1-p)*K*J) + design_effect*(1-rho2-rho3)*(1-r21)/(p*(1-p)*J*K*n)),
    "its_nocompare": lambda: (1/np.sqrt(K))*np.sqrt(1/n+rho2*(1-r22)/(1-rho2))*np.sqrt(1+1/T+(tf+(T+1)/2)**2/(T*(T+1)*(2*T+1)/6-(T+1)**2*T/4)),
    "its_wcompare": lambda: np.sqrt(1+1/q)*(1/np.sqrt(K))*np.sqrt(1/n+rho2*(1-r22)/(1-rho2))*np.sqrt(1+1/T+(tf+(T+1)/2)**2/(T*(T+1)*(2*T+1)/6-(T+1)**2*T/4))
  

    }

def sse_equation(design):
    d = sys._getframe().f_back.f_locals
    calc = design_sse[design]
    func = scoped_function(calc, d)
    return func().return_value


design_sample_size = {
    "ira": lambda: (m/es)**2 * ((1-r21)/(p*(1-p))),
    "bira2_1c": lambda: (m/es)**2 * ((1-r21)/(p*(1-p)*n)),
    "bira2_1f": lambda: (m/es)**2 * ((1-r21)/(p*(1-p)*n)),
    "rd2_1f": lambda: (m/es)**2 * ((1-r21)/(p*(1-p)*n))*design_effect,
    "bira2_1r": lambda: (m/es)**2 * (
                rho2*omega2*(1-r2t2) + 
                (1-rho2)*(1-r21)/(p*(1-p)*n)),
    "rd2_1r": lambda: (m/es)**2 * (
                rho2*omega2*(1-r2t2) + 
                (1-rho2)*(1-r21)*design_effect/(p*(1-p)*n)), 
    "bira3_1r": lambda: (m/es)**2 * (
                rho3*omega3*(1-r2t3) + 
                rho2*omega2*(1-r2t2)/J + 
                (1-rho2-rho3)*(1-r21)/(p*(1-p)*J*n)),
    "bira4_1r": lambda: ((m/es)**2 * (
                rho4*omega4*(1-r2t4) +
                rho3*omega3*(1-r2t3)/K +
                rho2*omega2*(1-r2t2)/(K*J) + 
                (1-rho4-rho3-rho2)*(1-r21)/(p*(1-p)*K*J*n))),
    "cra2_2r": lambda: (m/es)**2*(rho2*(1-r22)/(p*(1-p)) + (1-rho2)*(1-r21)/(p*(1-p)*n)),
    "cra3_3r": lambda: (m/es)**2*(rho3*(1-r23)/(p*(1-p))+rho2*(1-r22)/(p*(1-p)*J)+(1-rho3-rho2)*(1-r21)/(p*(1-p)*J*n)), 
    "cra4_4r": lambda: (m/es)**2*(rho4*(1-r24)/(p*(1-p))+
                               rho3*(1-r23)/(p*(1-p)*K)+
                               rho2*(1-r22)/(p*(1-p)*J*K)+
                               (1-rho4-rho3-rho2)*(1-r21)/(p*(1-p)*J*K*n)),
    "bcra3_2f": lambda: (m/es)**2*(rho2*(1-r22)/(p*(1-p)*J)+(1-rho2)*(1-r21)/(p*(1-p)*J*n)),
    "bcra3_2r": lambda: (m/es)**2 * (rho3*omega3*(1-r2t3) +
                       rho2*(1-r22)/(p*(1-p)*J) +
                       (1-rho3-rho2)*(1-r21)/(p*(1-p)*J*n)),
    "bcra4_2r": lambda: (m/es)**2*(rho4*omega4*(1-r2t4)+rho3*omega3*(1-r2t3)/K+
                                   rho2*(1-r22)/(p*(1-p)*K*J)+(1-rho4-rho3-rho2)*(1-r21)/(p*(1-p)*J*K*n)),
    "bcra4_3f": lambda: (m/es)**2 * (rho3*(1-r23)/(p*(1-p)*K)+
                                     rho2*(1-r22)/(p*(1-p)*K*J)+(1-rho3-rho2)*(1-r21)/(p*(1-p)*J*K*n)),
    "bcra4_3r": lambda: (m/es)**2 * (rho4*omega4*(1-r2t4)+rho3*(1-r23)/(p*(1-p)*K)+rho2*(1-r22)/(p*(1-p)*K*J)+
                                     (1-rho4-rho3-rho2)*(1-r21)/(p*(1-p)*K*J*n)),   
    "rdc_2r": lambda: (m/es)**2*design_effect*(rho2*(1-r22)/(p*(1-p))+(1-rho2)*(1-r21)/(p*(1-p)*n)),
    "rdc_3r": lambda: (m/es)**2*design_effect*(rho3*(1-r23)/(p*(1-p))+
                                                     rho2*(1-r22)/(p*(1-p)*J)+
                                                     (1-rho2-rho3)*(1-r21)/(p*(1-p)*J*n)),
    "rd3_2f": lambda: (m/es)**2*(design_effect)*(rho2*(1-r22)/(p*(1-p)*J)+(1-rho2)*(1-r21)/(p*(1-p)*J*n)), 
    "rd3_2r": lambda: (m/es)**2*(rho3*omega3*(1-r2t3)+ design_effect*rho2*(1-r22)/(p*(1-p)*J) + design_effect*(1-rho2-rho3)*(1-r21)/(p*(1-p)*J*n)),
    "its_nocompare": lambda: (m/es)**2*(1/n+rho2*(1-r22)/(1-rho2))*(1+1/T+(tf+(T+1)/2)**2/(T*(T+1)*(2*T+1)/6-(T+1)**2*T/4)),
    "its_wcompare": lambda: (m/es)**2*(1+1/q)*(1/n+rho2*(1-r22)/(1-rho2))*(1+1/T+(tf+(T+1)/2)**2/(T*(T+1)*(2*T+1)/6-(T+1)**2*T/4))


                                }

def sample_size_equation(design):
    d = sys._getframe().f_back.f_locals
    calc = design_sample_size[design]
    func = scoped_function(calc, d)
    return func().return_value

def effect_size(design, n,  power=0.8, alpha=0.05, two_tailed=True, p=0.5, g=0, r21=0, 
         J=1, rho2=0.1, omega2 = 0.1, r2t2=0, 
         K=10, rho3=0.1, omega3 = 0.1, r2t3=0, 
         L=10, rho4=0.1, omega4 = 0.1, r2t4=0,                
         design_effect=0, r22=0, r23=0, r24=0,
         T=0, tf=0, q=0
        ):    
    #get equation for degree of freedom
    v = degree_freedom_equation(design)
    
    #get equation for sse
    sse = sse_equation(design)
    
    m = multiplier(alpha, v, power, two_tailed)
    mdes = m * sse 
    return mdes
        
def power(design, n,  es=0.25, alpha=0.05, two_tailed=True, p=.50, g=0, r21=0,
          J=1, rho2=0.1, omega2 = 0.1, r2t2=0,
          K=10, rho3=0.1, omega3 = 0.1, r2t3=0,
          L=10, rho4=0.1, omega4 = 0.1, r2t4=0,
          design_effect=0, r22=0, r23=0, r24=0,
          T=0, tf=0, q=0
         ):
    """
    calculate power 
    """
    #get equation for degree of freedom
    v = degree_freedom_equation(design)
    
    #get equation for sse
    sse = sse_equation(design)

    lambda_ = es/sse
    if two_tailed == True:
        power = (1 - stats.t.cdf(stats.t.ppf(1-alpha/2, v), v, lambda_) + 
                 stats.t.cdf(-stats.t.ppf(1-alpha/2, v), v, lambda_))
    else:
        power = 1-stats.t.cdf(stats.t.ppf(1-alpha, v), v, lambda_)
    return power

def sample_size(design, es=0.2, power=0.8, alpha=0.05, two_tailed=True, n=30, tol=.10, p=.50, g=0, r21=0, 
         J=10, rho2=0, omega2 = 0, r2t2=0, 
         K=5, rho3=0, omega3 = 0, r2t3=0, 
         L=10, rho4=0.1, omega4 = 0.1, r2t4=0,
         design_effect=0, r22=0, r23=0, r24=0, 
         T=0, tf=0, q=0,
         max_iter=500):
    """
    calculate minimum required sample sizes 
    """  
    for i in range(max_iter):
        v = degree_freedom_equation(design)
        sse = sse_equation(design)
        m = multiplier(alpha, v, power, two_tailed)   

        if design in {'bira2_1r','bira2_1c','bira2_1f','rd2_1f','rd2_1r','rdc_2r','cra2_2r'}:            
            J_new = sample_size_equation(design)
            if abs(J_new-J) < tol:
                return round((J+J_new)/2) 
            J = (J+J_new)/2            
        elif design in {'bira3_1r', 'rdc_3r', 'rd3_2f', 'rd3_2r',
                        'cra3_3r','bcra3_2f','bcra3_2r', 
                        'its_nocompare','its_wcompare'}:
            K_new = sample_size_equation(design)
            if abs(K_new-K) < tol:
                return round((K+K_new)/2) 
            K = (K+K_new)/2    

        elif design in {'bira4_1r','cra4_4r','bcra4_2r','bcra4_3f','bcra4_3r'}:
            L_new = sample_size_equation(design)
            if abs(L_new-L) < tol:
                return round((L+L_new)/2) 
            L = (L+L_new)/2  
        elif design in {'ira'}:
            n_new = sample_size_equation(design)
            # when the difference between the calculated sample size and “guestimate” is within ± 0.1 (tol).
            if abs(n_new-n) < tol:
                return round((n+n_new)/2) 
            # The “guestimate” is replaced with the average of the original “guestimate” and the calculated sample size
            n = (n+n_new)/2
    raise ConvergenceError("When calculating sample size, not converge at max iteration. You may increase max_iter.")
