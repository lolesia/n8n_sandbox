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

def get_random_song_python(data):
    """
    Выбирает случайную песню из загруженного словаря данных.
    (Код функции такой же, как в предыдущем ответе)
    """
    if not data or 'artists' not in data:
        return {"error": "Некорректные или отсутствующие данные"}

    all_tracks = []
    for artist_name, tracks in data['artists'].items():
        # Добавляем имя артиста к каждому треку при объединении
        all_tracks.extend([
            {'artist': artist_name.replace('_', ' '), 'song': t['song'], 'year': t['year']}
            for t in tracks
        ])
    
    if not all_tracks:
        return {"error": "Список песен пуст"}
        
    return random.choice(all_tracks)


# --- Основная часть программы ---
# 1. Загружаем данные
playlist_data = load_data_from_file(FILE_NAME)

# 2. Используем функцию, если данные успешно загружены
if playlist_data:
    random_track = get_random_song_python(playlist_data)
    print("Выпала случайная песня:")
    print(json.dumps(random_track, indent=4, ensure_ascii=False))
