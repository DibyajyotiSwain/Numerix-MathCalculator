import sympy as sp
def parse(s):
    if not s.strip(): raise ValueError("Enter a matrix")
    rows=[[sp.sympify(v.strip()) for v in r.split(",") if v.strip()] for r in s.split(";")]
    if any(not r for r in rows) or len({len(r) for r in rows})!=1: raise ValueError("Rows must have equal non-zero lengths")
    return sp.Matrix(rows)
def calculate(a,b,op):
    A=parse(a); B=parse(b) if b.strip() else None
    if op=="Transpose": return A.T
    if op=="Determinant":
        if not A.is_square: raise ValueError("Square matrix required")
        return A.det()
    if op=="Inverse":
        if not A.is_square or A.det()==0: raise ValueError("Matrix must be square and non-singular")
        return A.inv()
    if B is None: raise ValueError("Enter matrix B")
    if op=="Add": return A+B
    if op=="Multiply": return A*B
    raise ValueError("Unsupported operation")
