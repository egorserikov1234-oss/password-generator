def main():
    """
    Главная функция запуска приложения.
    """
    print("---------------------------------------")
    print("Привет! Это мой генератор безопасных паролей")
    print("Приложение запущено и готово к работе.")
    print("---------------------------------------")

if __name__ == "__main__":
    main()

import random
import string

def generate_password(length):
    """Генерирует случайную строку из букв и цифр."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def add_entry(history):
    """Запрашивает данные у пользователя и добавляет новый пароль в историю."""
    service = input("Для какого сервиса пароль? (например, VK, Google): ")
    try:
        length = int(input("Введите длину пароля (например, 12): "))
        password = generate_password(length)
        
        # Создаем словарь с данными
        entry = {
            "service": service,
            "password": password
        }
        
        history.append(entry)
        print(f"\n[Успех] Пароль для {service} создан: {password}")
    except ValueError:
        print("\n[Ошибка] Длина должна быть числом!")

def show_history(history):
    """Выводит список всех созданных паролей."""
    if not history:
        print("\nИстория пока пуста.")
        return

    print("\n--- Ваша история паролей ---")
    for i, item in enumerate(history, 1):
        print(f"{i}. Сервис: {item['service']} | Пароль: {item['password']}")
    print("----------------------------")

def main():
    # Наш список для хранения данных в оперативной памяти
    password_history = []
    
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Сгенерировать новый пароль")
        print("2. Показать историю")
        print("3. Выход")
        
        choice = input("Выберите действие (1-3): ")
        
        if choice == "1":
            add_entry(password_history)
        elif choice == "2":
            show_history(password_history)
        elif choice == "3":
            print("Программа завершена. До встречи!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()