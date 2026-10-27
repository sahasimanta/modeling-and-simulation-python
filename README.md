# Modeling and Simulation with Python

**Numerical Computing · Linear Algebra · Scientific Visualization · Engineering Foundations**

A growing collection of Python implementations and computational exercises developed during my **M.Sc. in Electrical Systems Engineering at Paderborn University (Universität Paderborn), Germany**.

## About

During my undergraduate engineering studies, **C was my primary programming language**. I am now expanding my programming toolkit with **Python**, focusing on numerical methods, scientific computing, and translating mathematical ideas into working code.

This repository documents that learning process. My long-term goal is to apply these foundations to **signal processing, dynamic-system modeling, numerical simulation, and data-driven engineering**.

The current content represents foundational practice, not a completed engineering simulation platform.

## Current Implementations

| Topic | Implementation |
| --- | --- |
| Matrix construction | Create a structured 4 × 4 matrix with `numpy.diag` |
| NumPy operations | Array shapes and element-wise comparisons |
| Programming fundamentals | `for`/`while` loops, conditional logic, minimum/maximum searches, and lambda expressions |
| Function sampling | Calculate and plot 21 samples of `sin(x)` between 0 and π |
| Numerical linear algebra | Solve a 9 × 9 system using a custom Gaussian-elimination function |
| Solver implementation | Partial pivoting, forward elimination, singularity checks, and back substitution |
| Numerical verification | Validate the computed solution with `np.allclose(A @ x, b)` |
| 3D plotting | Visualize a parametric curve with Matplotlib |
| Modeling terminology | Explore physical, abstract, static, dynamic, deterministic, and stochastic model categories through examples |

### Gaussian Elimination

I implemented a numerical solver for **Ax = b** using partial pivoting, forward elimination, and back substitution. In the current example, **A** is a 9 × 9 matrix formed from a matrix of ones plus twice the identity matrix. The calculated result is checked using:

```python
np.allclose(A @ x, b)
```

This is an educational implementation for understanding the algorithm; it is not intended to replace established numerical libraries.

### Mathematical Visualization

The notebook includes a sampled sine function and a 3D parametric curve defined by:

```python
t = np.linspace(0, 2 * np.pi, 100)
x = np.cos(t)
y = np.sin(t)
z = np.sin(t)
```

These exercises help me connect mathematical expressions with their computational and geometric representations.

## Repository Contents

| File | Purpose |
| --- | --- |
| [Jupyter notebook](./ps_2_4110150.ipynb) | Interactive code, outputs, and mathematical plots |
| [Python exercise script](./ps_2_ex%201to6_4110150.py) | Consolidated Python implementations |
| [Gaussian-elimination helper](./ps_2_ex%204b_4110150.py) | Custom linear-system solver used by the notebook |

## Running the Code

**Requirements:** Python 3, NumPy, Matplotlib, and Jupyter Notebook (or VS Code with Python and Jupyter extensions).

1. Clone or download this repository, then open its folder in **VS Code**.
2. Install the required packages in a terminal:

   ```powershell
   py -m pip install numpy matplotlib jupyter
   ```

3. Open the `.ipynb` file, select a Python kernel, and run the cells.

**Important:** Keep the repository folder as the notebook's working directory. The Gaussian-elimination exercise loads its helper `.py` file using a relative path.

## Skills in Development

- Converting mathematical definitions into executable Python algorithms
- Working with NumPy arrays and linear systems
- Understanding basic numerical safeguards and solution verification
- Exploring mathematical visualization with Matplotlib
- Building more reproducible Python workflows with Jupyter, VS Code, Git, and GitHub

## Future Directions

The following are **areas I plan to explore**, rather than completed work in this repository:

- **Signal processing:** sampling, Fourier transforms, filtering, and noise analysis
- **Dynamic-system simulation:** differential equations, state-space models, and numerical solvers
- **Engineering applications:** control systems and sensor-data processing
- **Code quality:** reusable functions, automated tests, clearer documentation, and reproducible notebooks

## Project Context

The initial implementations are part of my learning exercises in **Modeling and Simulation**. This repository is a record of my technical development, not an official course solution repository or production-ready simulation library.

---

**Simanta Saha**  
M.Sc. Electrical Systems Engineering · Paderborn University
