import math

def get_positive_integer():
    while True:
        user_input = input("Введите положительное целое число: ")
        try:
            number = int(user_input)
            if number < 0:
                print("Ошибка: число должно быть неотрицательным.")
            else:
                return number
        except ValueError:
            print("Ошибка: введите целое число.")

def calculate_factorial(n):
    return math.factorial(n)

def main():
    num = get_positive_integer()
    result = calculate_factorial(num)
    print(f"Факториал числа {num} равен {result}")
    input("\nНажмите Enter, чтобы завершить программу...")

if __name__ == "__main__":
    main()
