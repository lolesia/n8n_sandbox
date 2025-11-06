# 🎼 Random Song Picker Utility

A Python script to load song data from a JSON file and randomly select a single track.

## 🚀 Quick Start

1.  Ensure you have **Python 3** installed.
2.  Create a file named `songs.json` in the same directory.
3.  Run the script: `python your_script_name.py` (replace `your_script_name.py` with your file name).

## ⚙️ Logic Overview

The script relies on two core functions to perform the operation:

1.  **Data Loading (`load_data_from_file`)**:
    * Reads and parses the JSON file specified by `FILE_NAME`.
    * Handles **`FileNotFoundError`** and **`json.JSONDecodeError`**.

2.  **Random Selection (`get_random_song_python`)**:
    * Takes the parsed dictionary (`data`).
    * **Flattens** the nested structure (Artist -> List of Songs) into a single list of track objects.
    * **Injects** the `artist` name into each track object (converting `Artist_Name` to `Artist Name`).
    * Uses `random.choice()` to return a single, randomly selected track.

## 📁 Data Structure (`songs.json`)

The input file **must** contain a top-level `"artists"` key, where values are lists of song objects with `"song"` and `"year"` keys.

```json
{
    "artists": {
        "Artist_Name_One": [
            {"song": "Track Title A", "year": 1999},
            // ...
        ],
        "Artist_Name_Two": [
            {"song": "Track Title B", "year": 2005}
        ]
    }
}
