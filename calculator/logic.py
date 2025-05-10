# calculator/logic.py

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание b из a"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление a на b (с проверкой деления на ноль)"""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b

