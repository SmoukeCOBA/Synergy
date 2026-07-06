import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    max_attempts = 7 
    print("Я загадал число от 1 до 100. Попробуйте угадать его!")
    print(f"У вас {max_attempts} попыток.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Попытка {attempt}: Введите ваше предположение: "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        if guess < 1 or guess > 100:
            print("Число должно быть от 1 до 100.")
            continue

        if guess < secret_number:
            print("Слишком маленькое число.")
        elif guess > secret_number:
            print("Слишком большое число.")
        else:
            print(f"Поздравляем! Вы угадали число {secret_number} за {attempt} попыток.")
            break
    else:
        print(f"К сожалению, вы не угадали. Загаданное число было {secret_number}.")

def main():
    while True:
        guess_the_number()
        play_again = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
        if play_again not in ("да", "д", "yes", "y"):
            print("Спасибо за игру!")
            input("Нажмите Enter, чтобы выйти...")
            break

if __name__ == "__main__":
    main()
