import json
import random
import sys

if len(sys.argv) > 1:
    # Если аргумент передан, используем его как имя файла
    FILE_NAME = sys.argv[1]
else:
    # Иначе используем имя файла по умолчанию
    FILE_NAME = 'songs.json' 
    print(f"Using default file name: '{FILE_NAME}'. To specify a file, run: python script_name.py your_file.json")

def load_data_from_file(file_path):
    """
    Loads and parses JSON data from the specified file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        # Error: File 'filename' not found.
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        # Error: Invalid JSON format in file 'filename'.
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        return None

def check_award_status(track):
    """
    Checks if a song has any awards and returns a descriptive string.
    """
    awards = track.get('awards')
    
    if awards is None:
        return "Info: Awards data is missing for this track."
    
    if isinstance(awards, list) and len(awards) > 0:
        count = len(awards)
        return f"🏆 Awarded Track: This song has {count} listed award(s) including: {', '.join(awards[:2])}..." 
    return "💡 Note: This track has no listed awards."

def get_random_song_python(data):
    """
    Selects a random song from the loaded data dictionary.
    (The function code is the same as in the previous answer)
    """
    if not data or 'artists' not in data:
        return {"error": "Invalid or missing data"}

    all_tracks = []
    for artist_name, tracks in data['artists'].items():
        # Add the artist's name to each track during merging
        all_tracks.extend([
            {'artist': artist_name.replace('_', ' '), 'song': t['song'], 'year': t['year'], 'awards': t.get('awards', [])}
            for t in tracks
        ])
    
    if not all_tracks:
        return {"error": "Song list is empty"}
        
    return random.choice(all_tracks)


def get_random_film_python(data):
    """
    Selects a random film from the loaded data dictionary.
    (The function code is the same as in the previous answer)
    """
    if not data or 'directors' not in data:
        return {"error": "Invalid or missing data"}

    all_tracks = []
    for director_name, films in data['directors'].items():
        # Add the artist's name to each track during merging
        all_tracks.extend([
            {'directors': director_name.replace('_', ' '), 'film': f['film'], 'year': f['year'], 'awards': f.get('awards', [])}
            for f in films
        ])
    
    if not all_tracks:
        return {"error": "Song list is empty"}
        
    return random.choice(all_tracks)

# --- Main part of the program ---
# 1. Load data
playlist_data = load_data_from_file(FILE_NAME)

if FILE_NAME == "songs.json":
# 2. Use the function if the data was loaded successfully
    if playlist_data:
        random_track = get_random_song_python(playlist_data)
        # A random song was selected:
        print("A random song was selected:")
        print(json.dumps(random_track, indent=4, ensure_ascii=False))
        print("---------------------------------")

        award_status = check_award_status(random_track)
        print(award_status)
        print("---------------------------------")

if FILE_NAME == "films.json":
    # 2. Use the function if the data was loaded successfully
    if playlist_data:
        random_track = get_random_film_python(playlist_data)
        # A random song was selected:
        print("A random song was selected:")
        print(json.dumps(random_track, indent=4, ensure_ascii=False))
        print("---------------------------------")

        award_status = check_award_status(random_track)
        print(award_status)
        print("---------------------------------")