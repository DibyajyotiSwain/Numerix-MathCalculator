import sympy as sp
from .algebra import expr
def sym(var):
    v=var.strip() or "x"
    if not v.isidentifier(): raise ValueError("Invalid variable")
    return sp.Symbol(v)
def differentiate(s,var="x",order=1):
    if not 1<=order<=10: raise ValueError("Order must be 1–10")
    return sp.diff(expr(s),sym(var),order)
def integrate(s,var="x"): return sp.integrate(expr(s),sym(var))
def limit(s,var="x",point="0"): return sp.limit(expr(s),sym(var),sp.sympify(point))
