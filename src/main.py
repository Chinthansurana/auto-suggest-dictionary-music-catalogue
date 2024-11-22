from trie import TrieWithRedisCache
from ml_model import CollaborativeFilteringModel
from data_loader import load_data, load_music_data
import time

def main():
    # Load data from files
    dictionary_words = load_data('data/dictionary.txt')
    music_catalog_data = load_music_data('data/music_catalog.txt')

    # Initialize Trie and ML Model
    trie = TrieWithRedisCache(redis_host='localhost', redis_port=6379)
    ml_model = CollaborativeFilteringModel(user_data=np.random.rand(10, 100))  # Random data for now

    # Insert words into Trie and train the ML model
    for word in dictionary_words:
        trie.insert(word)

    ml_model.train()

    # Handle music catalog with basic suggestions
    song_catalog = [f"{song}, {artist}, {genre}" for song, artist, genre in music_catalog_data]

    # Accept user input for prefix search
    prefix = input("Enter a prefix to search: ")

    # First try cache
    cached_suggestions = trie.search_with_cache(prefix)
    if not cached_suggestions:
        # If no cache, search and update cache
        suggestions = trie.search_with_ranking(prefix)
        cache_prefix(trie.redis, prefix, suggestions)
    else:
        suggestions = cached_suggestions

    print(f"Suggested words for prefix '{prefix}': {suggestions}")

if __name__ == "__main__":
    main()
