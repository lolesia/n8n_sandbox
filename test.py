import json
import random

FILE_NAME = 'songs.json' 

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
            {'artist': artist_name.replace('_', ' '), 'song': t['song'], 'year': t['year']}
            for t in tracks
        ])
    
    if not all_tracks:
        return {"error": "Song list is empty"}
        
    return random.choice(all_tracks)


# --- Main part of the program ---
# 1. Load data
playlist_data = load_data_from_file(FILE_NAME)

# 2. Use the function if the data was loaded successfully
if playlist_data:
    random_track = get_random_song_python(playlist_data)
    # A random song was selected:
    print("A random song was selected:")
    print(json.dumps(random_track, indent=4, ensure_ascii=False))