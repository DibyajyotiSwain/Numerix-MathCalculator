# NUMERIX – Mathematical Computing Studio

**An Interactive Desktop Application for Mathematical Computation, Analysis, and Visualisation**

---

## 1. Introduction

NUMERIX is a Python-based mathematical computing application designed to simplify complex mathematical operations through an interactive graphical user interface.

The application brings together various mathematical tools, allowing users to perform calculations, solve equations, analyse mathematical functions, work with matrices, visualise graphs, and conduct statistical analysis within a single desktop environment.

Built using Python and modern scientific computing libraries, NUMERIX aims to make mathematical computation more accessible, organised, and efficient for students, educators, and individuals interested in mathematics and computational problem-solving.

## 2. Project Objectives

The primary objectives of NUMERIX are:

- To develop an integrated platform for mathematical computation.
- To simplify complex mathematical calculations through an interactive interface.
- To provide tools for algebra, calculus, complex numbers, and matrix operations.
- To enable graphical representation and visual analysis of mathematical functions.
- To introduce statistical analysis and regression techniques.
- To demonstrate the practical application of Python in mathematical computing.

## 3. Key Features

### Complex Numbers
- Addition, subtraction, multiplication, and division.
- Complex number calculations and properties.
- Support for mathematical expressions involving imaginary numbers.

### Algebra Solver
- Expression simplification.
- Polynomial expansion and factorisation.
- Equation solving.

### Calculus Studio
- Differentiation.
- Indefinite integration.
- Definite integration.
- Limit calculations.

### Matrix Operations
- Matrix addition and multiplication.
- Determinant calculation.
- Matrix inverse.
- Matrix transpose.

### Graphing Studio
- Graphical representation of mathematical functions.
- Function plotting using numerical computation.
- Visual exploration of mathematical relationships.

### Regression Lab
- Simple linear regression.
- Slope and intercept calculation.
- R-squared evaluation.
- Root Mean Squared Error (RMSE).

### Statistics
- Descriptive statistical analysis.
- Mean, median, and standard deviation.
- Numerical data analysis using scientific computing libraries.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PySide6 | Graphical User Interface |
| SymPy | Symbolic mathematical computation |
| NumPy | Numerical computation |
| SciPy | Scientific computing |
| Matplotlib | Mathematical graphs and visualisation |
| Pandas | Data handling and analysis |
| Scikit-learn | Machine learning and regression |

## 5. Project Structure

```text
NUMERIX_Math_Studio/
│
├── main.py
├── requirements.txt
│
├── numerix/
│   ├── core/
│   │   ├── complex_numbers.py
│   │   ├── algebra.py
│   │   ├── calculus.py
│   │   ├── matrices.py
│   │   ├── graphing.py
│   │   ├── regression.py
│   │   └── statistics.py
│   │
│   └── ui/
│       ├── pages.py
│       └── main_window.py
│
├── tests/
│   └── test_core.py
│
├── docs/
│   ├── PROJECT_HISTORY.md
│   ├── ARCHITECTURE.md
│   ├── USER_GUIDE.md
│   └── ROADMAP.md
│
├── examples/
│   └── example_expressions.md
│
├── README.md
├── LICENSE
└── .gitignore
```

## 6. Installation and Setup

### Prerequisites

Before installing NUMERIX, ensure that you have:

- Python 3.10 or later.
- pip package manager.
- Visual Studio Code or another Python-compatible IDE.
- Windows, macOS, or Linux.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Alternatively, download and extract the project ZIP file.

### Step 2: Navigate to the Project Directory

```bash
cd NUMERIX_Math_Studio
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
python -m pip install --upgrade pip
```

```bash
python -m pip install PySide6 sympy numpy scipy matplotlib scikit-learn pandas
```

Alternatively:

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python main.py
```

NUMERIX will launch as a desktop application.

## 7. Testing

The project includes unit tests for its core mathematical functionality.

To execute the test suite, run:

```bash
python -m unittest discover -s tests -v
```

This helps verify the correctness of the implemented mathematical operations.

## 8. Application Architecture

NUMERIX follows a modular architecture that separates the user interface from the mathematical computation modules.

**Presentation Layer:** Built using PySide6 to provide an interactive desktop interface.

**Core Computation Layer:** Uses SymPy, NumPy, and SciPy for mathematical and numerical operations.

**Visualisation Layer:** Uses Matplotlib to represent mathematical functions graphically.

**Data Analysis Layer:** Uses Pandas and Scikit-learn for statistical analysis and regression.

This modular approach makes the application easier to maintain, test, and extend.

## 9. Future Enhancements

Potential future developments include:

- Advanced equation-solving capabilities.
- Three-dimensional mathematical visualisation.
- Differential equation solver.
- Numerical methods and optimisation tools.
- Advanced statistical modelling.
- Machine learning-based mathematical analysis.
- Calculation history and export functionality.
- Improved user interface and customisation.
- Additional mathematical modules.

## 10. Project Background

NUMERIX is an expanded development of an earlier academic concept focused on complex mathematical computation using Python and SymPy.

The current version builds upon that concept by introducing a modular architecture, a graphical desktop interface, and additional mathematical and analytical capabilities.

It is intended to serve as a foundation for further development in mathematical computing and scientific applications.

## 11. Security and Usage Notes

NUMERIX is designed primarily for local educational and computational use.

Mathematical expression evaluation should only be performed with trusted input. Some symbolic and numerical evaluation methods used in the project are not hardened sandboxes for arbitrary untrusted expressions.

The application should not be exposed as a public service without appropriate security controls and input validation.

## 12. License

This project is distributed under the license included in this repository. Please refer to the `LICENSE` file for the applicable terms and conditions.

---

SCREENSHOTS:
<img width="1877" height="484" alt="Screenshot 2026-11-06 172523" src="https://github.com/user-attachments/assets/3b752665-2811-43d2-bbff-b11a040773bc" />
<img width="2259" height="1158" alt="Screenshot 2026-11-06 170929" src="https://github.com/user-attachments/assets/fc68632b-cd75-45e0-b7a9-686402c6ce08" />
<img width="2264" height="1272" alt="Screenshot 2026-11-06 170858" src="https://github.com/user-attachments/assets/92be3348-88f2-4979-a1f4-d8c7485f380b" />


## NUMERIX

**Mathematical Computing Studio**

*Making Mathematical Computation More Accessible Through Technology.*
-BY Dibyajyoti Swain

