import sympy as sp
def calculate(a,b,operation):
    x=sp.sympify(a,locals={"i":sp.I}); y=sp.sympify(b,locals={"i":sp.I})
    ops={"Add":lambda:x+y,"Subtract":lambda:x-y,"Multiply":lambda:x*y,"Divide":lambda:x/y}
    if operation not in ops: raise ValueError("Unsupported operation")
    if operation=="Divide" and y==0: raise ZeroDivisionError("Cannot divide by zero")
    z=sp.simplify(ops[operation]())
    return {"result":z,"real":sp.re(z),"imaginary":sp.im(z),"modulus":sp.Abs(z),"conjugate":sp.conjugate(z),"argument":sp.arg(z)}
