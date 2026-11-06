# NUMERIX — Mathematical Computing Studio

**A desktop mathematical computing environment powered by Python and SymPy.**

NUMERIX is a redevelopment of an earlier academic project, *Complex Math Calculator using SYMPY*. The original assignment introduced complex-number operations, algebra, calculus and regression analysis. This expanded edition preserves those foundations and develops them into a modular desktop application.

## Modules
- Complex-number arithmetic and properties
- Algebraic simplification, expansion, factorisation and equation solving
- Differentiation, integration and limits
- Matrix operations
- Mathematical graphing
- Linear regression with R² and RMSE
- Descriptive statistics

## Technology
Python · PySide6 · SymPy · NumPy · SciPy · Matplotlib · scikit-learn · Pandas

## Windows setup
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

Run tests:
```powershell
python -m unittest discover -s tests -v
```

## Project status
This is a working prototype, not a certified scientific or engineering system. Independently validate important results.

## Project history
The project originated as a group assignment around 2021. The original source code was not available for this redevelopment; the earlier presentation served as the reference. See `docs/PROJECT_HISTORY.md` and accurately complete the contribution details before publishing.

## Input safety note

This prototype is intended for local use by its operator. SymPy's `sympify` and `lambdify` are convenient mathematical tools but must not be treated as a hardened sandbox for arbitrary untrusted input. Do not expose expression entry to unknown remote users or run this prototype as a public service without replacing or tightly restricting the parser and reviewing the execution model.
