def add(a, b):
    # Версия 2: сложение с проверкой типов
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    """Деление двух чисел."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль запрещено!")
    return a / b

if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("2 * 3 =", multiply(2, 3))
    print("6 / 3 =", divide(6, 3))
