import numpy as np

def entropy(p):
    p=np.asarray(p)
    items=p*np.log(p)
    import IPython; IPython.embed()
    return -np.sum(items)

p=np.arange(5.)
p/=p.sum()
entropy(p)