import json
import random

FILE_NAME = 'songs.json' 

def load_data_from_file(file_path):
    """
    Загружает и парсит JSON-данные из указанного файла.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный формат JSON в файле '{file_path}'.")
        return None

playlist_data = load_data_from_file(FILE_NAME)


def print_text(text):
    print(text)

# использование
print_text("Test!")