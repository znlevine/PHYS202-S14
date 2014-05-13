
import numpy as np
import matplotlib.pyplot as plt

def trapz(func,x,N):
    """Integrates using trapezoidal function"""
    
    a=0.0
    b=x
    h=(b-a)/N
    
    k=np.arange(1,N)
    I=h*(0.5*func(a)+0.5*func(b)+func(a+k*h).sum())
    
    return I

def simps(func,x,N):
    """Integrates using Simpson's rule"""
    
    a=0.0
    b=x
    h=(b-a)/N
    k1=np.arange(1,N/2+1)
    k2=np.arange(1,N/2)
    I=(1./3.)*h*(func(a)+func(b)+4.*func(a+(2*k1-1)*h).sum()+2.*func(a+2*k2*h).sum())
    return I