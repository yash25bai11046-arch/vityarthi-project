#Scientific calculator GUI

from tkinter import *
import math

root = Tk()
root.title("Scientific Calculator")
root.configure(background='white')
root.resizable(width=False, height=False)
root.geometry("944x568+200+50")  # width of the calculator

calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
        self.expression = ""  # Store the full expression

    def numberEnter(self, num):
        self.result = False
        if self.input_value:
            self.current = str(num)
            self.input_value = False
        else:
            if num == '.' and '.' in self.current:
                return
            self.current = self.current + str(num)
        self.expression += str(num)  # Append the number to the expression
        self.display(self.expression)

    def sum_of_total(self):
        self.result = True
        try:
            self.current = float(self.current)
            if self.check_sum:
                self.valid_function()
            else:
                self.total = float(self.current)
            self.expression += " = " + str(self.total)  # Show the result in the expression
            self.display(self.expression)
        except ZeroDivisionError:
            self.display("Error: Division by zero")
        except Exception as e:
            self.display(f"Error: {e}")

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        try:
            if self.op == "+":
                self.total += self.current
            elif self.op == "-":
                self.total -= self.current
            elif self.op == "x":
                self.total *= self.current
            elif self.op == "/":
                if self.current != 0:
                    self.total /= self.current
                else:
                    self.total = "Error: Division by zero"
            elif self.op == "mod":
                self.total %= self.current
            self.input_value = True
            self.check_sum = False
            self.display(self.total)
            self.expression = str(self.total)  # Reset the expression after calculating
        except Exception as e:
            self.display(f"Error: {e}")

    def operation(self, op):
        if self.result:  # Prevent further operations after a result
            self.expression = str(self.total)
            self.result = False
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = float(self.current)
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.expression += " " + op + " "  # Append the operator to the expression
        self.display(self.expression)

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.expression = ""  # Reset the expression
        self.display("0")
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    # --- SCIENTIFIC FUNCTIONS ---
    def pi(self): self.display(self.expression + " π = " + str(math.pi))
    def tau(self): self.display(self.expression + " τ = " + str(math.tau))
    def e(self): self.display(self.expression + " e = " + str(math.e))
    def mathPM(self): self.display(self.expression + " = " + str(-(float(txtDisplay.get()))))
    def squared(self): self.display(self.expression + " √ = " + str(math.sqrt(float(txtDisplay.get()))))
    def cos(self): self.display(self.expression + " cos = " + str(math.cos(math.radians(float(txtDisplay.get())))))
    def cosh(self): self.display(self.expression + " cosh = " + str(math.cosh(math.radians(float(txtDisplay.get())))))
    def tan(self): self.display(self.expression + " tan = " + str(math.tan(math.radians(float(txtDisplay.get())))))
    def tanh(self): self.display(self.expression + " tanh = " + str(math.tanh(math.radians(float(txtDisplay.get())))))
    def sin(self): self.display(self.expression + " sin = " + str(math.sin(math.radians(float(txtDisplay.get())))))
    def sinh(self): self.display(self.expression + " sinh = " + str(math.sinh(math.radians(float(txtDisplay.get())))))
    def log(self): self.display(self.expression + " log = " + str(math.log(float(txtDisplay.get()))))
    def exp(self): self.display(self.expression + " exp = " + str(math.exp(float(txtDisplay.get()))))
    def acosh(self): self.display(self.expression + " acosh = " + str(math.acosh(float(txtDisplay.get()))))
    def asinh(self): self.display(self.expression + " asinh = " + str(math.asinh(float(txtDisplay.get()))))
    def expm1(self): self.display(self.expression + " expm1 = " + str(math.expm1(float(txtDisplay.get()))))
    def lgamma(self): self.display(self.expression + " gamma = " + str(math.lgamma(float(txtDisplay.get()))))
    def degrees(self): self.display(self.expression + " deg = " + str(math.degrees(float(txtDisplay.get()))))
    def log2(self): self.display(self.expression + " log2 = " + str(math.log2(float(txtDisplay.get()))))
    def log10(self): self.display(self.expression + " log10 = " + str(math.log10(float(txtDisplay.get()))))
    def log1p(self): self.display(self.expression + " log1p = " + str(math.log1p(float(txtDisplay.get()))))

added_value = Calc()

txtDisplay = Entry(calc, font=('Arial',20,'bold'), bg='White',fg='Black', bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
btn = []
i = 0

# --- NUMBER BUTTONS ---
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, bg='White', fg='Black',
                          font=('Helvetica',20,'bold'), bd=4, text=numberpad[i],
                          command=lambda x=numberpad[i]: added_value.numberEnter(x)))
        btn[i].grid(row=j, column=k, pady=1)
        i += 1

# --- BASIC OPERATION BUTTONS ---
Button(calc, text="C", width=6, height=2, bg='red',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.Clear_Entry)\
       .grid(row=1, column=0)

Button(calc, text="CE", width=6, height=2, bg='red',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.All_Clear_Entry)\
       .grid(row=1, column=1)

Button(calc, text="√", width=6, height=2, bg='powder blue',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.squared)\
       .grid(row=1, column=2)

Button(calc, text="+", width=6, height=2, bg='powder blue',
       font=('Helvetica',20,'bold'), bd=4, command=lambda: added_value.operation("+"))\
       .grid(row=1, column=3)

Button(calc, text="-", width=6, height=2, bg='powder blue',
       font=('Helvetica',20,'bold'), bd=4, command=lambda: added_value.operation("-"))\
       .grid(row=2, column=3)

Button(calc, text="x", width=6, height=2, bg='powder blue',
       font=('Helvetica',20,'bold'), bd=4, command=lambda: added_value.operation("x"))\
       .grid(row=3, column=3)

Button(calc, text="/", width=6, height=2, bg='powder blue',
       font=('Helvetica',20,'bold'), bd=4, command=lambda: added_value.operation("/"))\
       .grid(row=4, column=3)

Button(calc, text="0", width=6, height=2, bg='White', fg='Black',
       font=('Helvetica',20,'bold'), bd=4, command=lambda: added_value.numberEnter(0))\
       .grid(row=5, column=1)

Button(calc, text="±", width=6, height=2, bg='powder blue',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.mathPM)\
       .grid(row=5, column=2)

Button(calc, text=".", width=6, height=2, bg='powder blue',
       font=('Helvetica',20,'bold'), bd=4, command=lambda: added_value.numberEnter("."))\
       .grid(row=5, column=0)

Button(calc, text="=", width=6, height=2, bg='Yellow',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.sum_of_total)\
       .grid(row=5, column=3)

# --- SCIENTIFIC BUTTONS ---
Button(calc, text="pi", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.pi)\
       .grid(row=1, column=4)

Button(calc, text="sin", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.sin)\
       .grid(row=1, column=5)

Button(calc, text="cos", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.cos)\
       .grid(row=1, column=6)

Button(calc, text="tan", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.tan)\
       .grid(row=1, column=7)

Button(calc, text="2π", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.tau)\
       .grid(row=2, column=4)

Button(calc, text="sinh", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.sinh)\
       .grid(row=2, column=5)

Button(calc, text="cosh", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.cosh)\
       .grid(row=2, column=6)

Button(calc, text="tanh", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.tanh)\
       .grid(row=2, column=7)

Button(calc, text="log", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.log)\
       .grid(row=3, column=4)

Button(calc, text="exp", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.exp)\
       .grid(row=3, column=5)

Button(calc, text="mod", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=lambda: added_value.operation("mod"))\
       .grid(row=3, column=6)

Button(calc, text="e", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.e)\
       .grid(row=3, column=7)

Button(calc, text="log10", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.log10)\
       .grid(row=4, column=4)

Button(calc, text="log1p", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.log1p)\
       .grid(row=4, column=5)

Button(calc, text="expm1", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.expm1)\
       .grid(row=4, column=6)

Button(calc, text="gamma", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.lgamma)\
       .grid(row=4, column=7)

Button(calc, text="log2", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.log2)\
       .grid(row=5, column=4)

Button(calc, text="deg", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.degrees)\
       .grid(row=5, column=5)

Button(calc, text="acosh", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.acosh)\
       .grid(row=5, column=6)

Button(calc, text="asinh", width=6,height=2, bg='White',
       font=('Helvetica',20,'bold'), bd=4, command=added_value.asinh)\
       .grid(row=5, column=7)

# HEADER LABEL
Label(calc, text="Scientific Calculator",
      font=('Helvetica',30,'bold'), fg='Black', justify=CENTER)\
      .grid(row=0, column=4, columnspan=4)

root.mainloop()
