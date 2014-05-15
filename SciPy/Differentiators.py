
import numpy as np
import matplotlib.pyplot as plt

def twoPtForwardDiff(x,y):
    """Takes arrays and returns derivatives; based on forward"""
    
    dydxForward=np.zeros(y.shape,float)
    dydxForward[0:-1]=np.diff(y)/np.diff(x)
    dydxForward[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
    
    return dydxForward
    
    
def twoPtCenteredDiff(x,y):
    """Takes arrays and returns derivatives; based on center"""
    
    dydxCenter=np.zeros(y.shape,float)
    dydxCenter[1:-1]=(y[2:]-y[:-2])/(x[2:]-x[:-2])
    dydxCenter[0]=(y[1]-y[0])/(x[1]-x[0])
    dydxCenter[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
    
    return dydxCenter

def FourPtCenteredDiff(x,y,h):

    """Takes arrays and returns derivatives; based on center with greater accuracy"""
    dydx=np.zeros(y.shape,float)
    dydx[2:-2]=(y[0:-4]-8*y[1:-3]+8*y[3:-1]-y[4:])/(12.*h)
    dydx[0]=(y[1]-y[0])/(x[1]-x[0])
    dydx[1]=(y[2]-y[1])/(x[2]-x[1])
    dydx[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
    dydx[-2]=(y[-2]-y[-3])/(x[-2]-x[-3])
    
    return dydx