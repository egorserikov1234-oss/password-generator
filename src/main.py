import random
import string
import json
import os

# Имя файла, где будут лежать пароли
FILE_PATH = "passwords.json"

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def load_data():
    """Загружает данные из файла. Если файла нет, возвращает пустой список."""
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_data(history):
    """Сохраняет список паролей в файл JSON."""
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def main():
    # ТЕПЕРЬ МЫ ЗАГРУЖАЕМ ДАННЫЕ ПРИ СТАРТЕ
    history = load_data()
    
    while True:
        print("\n--- ГЕНЕРАТОР ПАРОЛЕЙ (С СОХРАНЕНИЕМ) ---")
        print("1. Создать новый пароль")
        print("2. Показать историю")
        print("3. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            service = input("Для какого сервиса пароль?: ")
            try:
                length = int(input("Введите длину: "))
                new_pass = generate_password(length)
                history.append({"service": service, "password": new_pass})
            
            # СОХРАНЯЕМ СРАЗУ ПОСЛЕ СОЗДАНИЯ
                save_data(history)
                print(f"Готово! Ваш новый пароль: {new_pass}") # <-- ВОТ ЭТА СТРОКА
                print(f"Пароль для {service} успешно записан в файл.")

            except ValueError:
                print("Ошибка: введите число для длины!")
                
        elif choice == "2":
            print("\n--- ВАШИ ПАРОЛИ ---")
            if not history:
                print("Список пуст.")
            for item in history:
                print(f"Сервис: {item['service']} | Пароль: {item['password']}")
                
        elif choice == "3":
            print("Данные сохранены. До встречи!")
            break
if __name__ == "__main__":
    main()