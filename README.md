## Scientific Calculator GUI

## Project Title
**Scientific Calculator using Tkinter** 

---

##  Overview of the Project
This project implements a fully functional **Scientific Calculator** as a desktop application.Built using **Python** and the **Tkinter** library for the Graphical User Interface (GUI), the calculator aims to provide a comprehensive tool for both **basic arithmetic** and **advanced scientific computations**

The goal of this project is to apply core programming and object-oriented concepts to build a practical application.

---

## Features (Functional Requirements) 
The application is structured into three major functional modules, providing a logical workflow and clear input/output.

| Module | Features Provided | Corresponding Project Concept |
| :--- | :--- | :--- |
| **1. Basic Arithmetic Module** | Addition (`+`), Subtraction (`-`), Multiplication (`x`), Division (`/`), Modulo (`mod`), and sign change (`±`). | **CRUD Operations** (Partial: Data Processing)  |
| **2. Scientific Functions Module** | Trigonometric (`sin`, `cos`, `tan`, `sinh`, `cosh`, `tanh`), Logarithmic (`log`, `log2`, `log10`, `log1p`), Exponential (`exp`, `expm1`), constants (`pi`, `tau`, `e`), Square Root (`√`), and unit conversion (`deg`). | **Simulation or Visualization** (Mathematical Simulation)  |
| **3. Input/Output Control Module** | Clear Entry (`C`), All Clear (`CE`), and persistent display of the current expression and result. | **Data Input & Processing**  |

---

## Technologies/Tools Used 
* **Programming Language:** Python
* **GUI Framework:** Tkinter
* **Scientific Library:** Python's built-in `math` module
* **Version Control:** Git / GitHub 
---

##  Steps to Install & Run the Project 

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

## Instructions for Testing 
The project utilizes **Validation and Error Handling**  techniques for robust operations.

### Key Test Scenarios

| Test ID | Test Description | Input Sequence | Expected Output / Result |
| :--- | :--- | :--- | :--- |
| **T01** | Basic Arithmetic (Multi-Step) | `5 + 3 x 2 =` | `11.0` |
| **T02** | Square Root Calculation | `81` $\rightarrow$ `√` | `9.0` |
| **T03** | Error Handling: Division by Zero | `10` $\rightarrow$ `/` $\rightarrow$ `0` $\rightarrow$ `=` | `Error: Division by zero` |
| **T04** | Trigonometric Function | `90` $\rightarrow$ `sin` | Result close to `1.0` |
| **T05** | Total Reset | `5 + 5` $\rightarrow$ `CE` | Display `0`, internal total `0` |

---

##  Screenshots: 
<img width="1589" height="746" alt="image" src="https://github.com/user-attachments/assets/74336af1-ecde-46c1-8450-78d2938f0601" />
<img width="1585" height="745" alt="image" src="https://github.com/user-attachments/assets/be739750-bca1-40c9-904a-08039269eef0" />
<img width="1589" height="739" alt="image" src="https://github.com/user-attachments/assets/a25e3088-4ab5-4e45-91ec-ac3e3d9d4b5e" />
<img width="1584" height="735" alt="image" src="https://github.com/user-attachments/assets/72626f30-4277-4972-97ad-ce19c3c66c63" />



