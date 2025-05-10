# main.py

import tkinter as tk
from calculator.logic import add, subtract, multiply, divide

# Создаём главное окно
root = tk.Tk()
root.title("Калькулятор от Сазонова В.С.")
root.geometry("300x400")
root.resizable(False, False)

# Ставит иконку (если есть)
try:
    root.iconbitmap('calculator.ico')
except tk.TclError:
    pass  # если нет — ок

# Состояние
current_input = ""
operation = None
first_number = None

# Обработчики
def on_digit_click(digit):
    global current_input
    current_input += str(digit)
    display.config(text=current_input)

def on_operation_click(op):
    global current_input, operation, first_number
    if current_input:
        first_number = float(current_input)
        current_input = ""
        operation = op
        op_display.config(text=f"{first_number} {operation}")

def calculate_result():
    global current_input, operation, first_number
    if current_input and operation:
        second = float(current_input)
        try:
            if operation == '+':
                res = add(first_number, second)
            elif operation == '-':
                res = subtract(first_number, second)
            elif operation == '*':
                res = multiply(first_number, second)
            elif operation == '/':
                res = divide(first_number, second)
            else:
                res = "Ошибка"
        except ZeroDivisionError:
            res = "Деление на 0!"
        display.config(text=str(res))
        current_input = ""
        operation = None
        op_display.config(text="")

def clear_all():
    global current_input, operation, first_number
    current_input = ""
    operation = None
    first_number = None
    display.config(text="")
    op_display.config(text="")

# Виджеты
display = tk.Label(root, text="", font=("Arial", 20), bg="white", anchor="e", bd=1, relief="solid")
display.place(x=10, y=10, width=280, height=50)

op_display = tk.Label(root, text="", font=("Arial", 16), bg="lightgray", anchor="e", bd=1, relief="solid")
op_display.place(x=10, y=70, width=280, height=30)

# Кнопки
frame = tk.Frame(root)
frame.place(x=10, y=110, width=280, height=270)

# Цифры
digits = [
    ("7",1,0), ("8",1,1), ("9",1,2),
    ("4",2,0), ("5",2,1), ("6",2,2),
    ("1",3,0), ("2",3,1), ("3",3,2),
    ("0",4,1)
]
for txt, r, c in digits:
    btn = tk.Button(frame, text=txt, font=("Arial",16),
                    command=lambda t=txt: on_digit_click(t))
    btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# Операции
ops = [("+",1,3), ("-",2,3), ("*",3,3), ("/",4,3)]
for txt, r, c in ops:
    btn = tk.Button(frame, text=txt, font=("Arial",16),
                    command=lambda o=txt: on_operation_click(o))
    btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# Равно и Очистка
eq = tk.Button(frame, text="=", font=("Arial",16), command=calculate_result)
eq.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

cl = tk.Button(root, text="C", font=("Arial",16), command=clear_all)
cl.place(x=10, y=380, width=280, height=40)

# Растягивание
for i in range(5):
    frame.rowconfigure(i, weight=1)
    frame.columnconfigure(i, weight=1)

root.mainloop()
