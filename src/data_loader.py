def load_data(file_path):
    """
    Loads data from a text file and returns a list of words or song entries.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def load_music_data(file_path):
    """
    Loads music data with song, artist, and genre.
    """
    music_data = []
    with open(file_path, 'r') as file:
        for line in file:
            song, artist, genre = line.strip().split(', ')
            music_data.append((song, artist, genre))
    return music_data
