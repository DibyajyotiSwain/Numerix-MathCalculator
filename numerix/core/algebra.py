import sympy as sp
def expr(s):
    if not s.strip(): raise ValueError("Enter an expression")
    return sp.sympify(s,locals={"pi":sp.pi,"e":sp.E})
def simplify(s): return sp.simplify(expr(s))
def expand(s): return sp.expand(expr(s))
def factor(s): return sp.factor(expr(s))
def solve(s,var="x"):
    if "=" in s:
        a,b=s.split("=",1); e=sp.sympify(a)-sp.sympify(b)
    else: e=expr(s)
    return sp.solve(e,sp.Symbol(var.strip() or "x"))
