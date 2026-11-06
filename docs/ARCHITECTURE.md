# Architecture

The desktop interface is built with PySide6. Each feature page calls a dedicated calculation module under `numerix/core/`.

- Complex numbers → SymPy
- Algebra → SymPy
- Calculus → SymPy
- Matrices → SymPy
- Graphing → SymPy + NumPy + Matplotlib
- Regression → scikit-learn
- Statistics → NumPy + Pandas

The separation between interface and calculation logic makes the core functions reusable and testable. User expressions are parsed symbolically; Python `eval()` is not used.
