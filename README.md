# 🧮 Scientific Calculator GUI

## 💡 Project Title
[cite_start]**Scientific Calculator using Tkinter** [cite: 89]

---

## 📄 Overview of the Project
This project implements a fully functional **Scientific Calculator** as a desktop application. [cite_start]Built using **Python** and the **Tkinter** library for the Graphical User Interface (GUI), the calculator aims to provide a comprehensive tool for both **basic arithmetic** and **advanced scientific computations**[cite: 90].

[cite_start]The goal of this project is to apply core programming and object-oriented concepts to build a practical application[cite: 8].

---

## [cite_start]✨ Features (Functional Requirements) [cite: 65, 92]
[cite_start]The application is structured into three major functional modules [cite: 21][cite_start], providing a logical workflow [cite: 23] [cite_start]and clear input/output[cite: 22].

| Module | Features Provided | Corresponding Project Concept |
| :--- | :--- | :--- |
| **1. Basic Arithmetic Module** | Addition (`+`), Subtraction (`-`), Multiplication (`x`), Division (`/`), Modulo (`mod`), and sign change (`±`). | [cite_start]**CRUD Operations** (Partial: Data Processing) [cite: 29] |
| **2. Scientific Functions Module** | Trigonometric (`sin`, `cos`, `tan`, `sinh`, `cosh`, `tanh`), Logarithmic (`log`, `log2`, `log10`, `log1p`), Exponential (`exp`, `expm1`), constants (`pi`, `tau`, `e`), Square Root (`√`), and unit conversion (`deg`). | [cite_start]**Simulation or Visualization** (Mathematical Simulation) [cite: 31] |
| **3. Input/Output Control Module** | Clear Entry (`C`), All Clear (`CE`), and persistent display of the current expression and result. | [cite_start]**Data Input & Processing** [cite: 26] |

---

## [cite_start]🛠️ Technologies/Tools Used [cite: 93]
* **Programming Language:** Python
* **GUI Framework:** Tkinter
* **Scientific Library:** Python's built-in `math` module
* [cite_start]**Version Control:** Git / GitHub [cite: 55]

---

## [cite_start]🚀 Steps to Install & Run the Project [cite: 94]

### Prerequisites
* Python 3.x (Tkinter is included in standard Python installations)

### Installation
1.  **Clone the repository:**
    ```bash
    git clone [Your-GitHub-Repository-URL]
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd scientific-calculator-gui
    ```

### Execution
1.  Run the Python script directly from your terminal:
    ```bash
    python your_calculator_script.py
    ```

---

## [cite_start]🧪 Instructions for Testing [cite: 95]
[cite_start]The project utilizes **Validation and Error Handling** [cite: 54] techniques for robust operations.

### Key Test Scenarios

| Test ID | Test Description | Input Sequence | Expected Output / Result |
| :--- | :--- | :--- | :--- |
| **T01** | Basic Arithmetic (Multi-Step) | `5 + 3 x 2 =` | `11.0` |
| **T02** | Square Root Calculation | `81` $\rightarrow$ `√` | `9.0` |
| **T03** | Error Handling: Division by Zero | `10` $\rightarrow$ `/` $\rightarrow$ `0` $\rightarrow$ `=` | `Error: Division by zero` |
| **T04** | Trigonometric Function | `90` $\rightarrow$ `sin` | Result close to `1.0` |
| **T05** | Total Reset | `5 + 5` $\rightarrow$ `CE` | Display `0`, internal total `0` |

---

## [cite_start]📷 Screenshots (Optional but Recommended) [cite: 96]
