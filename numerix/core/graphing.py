import numpy as np
import sympy as sp
def sample(s,start=-10,end=10,n=500):
    if start>=end: raise ValueError("Start must be less than end")
    if not 50<=n<=5000: raise ValueError("Point count must be 50–5000")
    x=sp.Symbol("x"); e=sp.sympify(s,locals={"pi":sp.pi,"e":sp.E})
    if e.free_symbols-{x}: raise ValueError("Only x is supported as a variable")
    fn=sp.lambdify(x,e,modules=["numpy"]); xs=np.linspace(start,end,n)
    with np.errstate(all="ignore"): ys=np.asarray(fn(xs))
    if ys.ndim==0: ys=np.full_like(xs,float(ys))
    ys=np.asarray(ys,dtype=np.complex128)
    if np.any(np.abs(ys.imag)>1e-9): raise ValueError("Only real-valued functions can be plotted")
    ys=ys.real.astype(float); ys[~np.isfinite(ys)]=np.nan
    return xs,ys
