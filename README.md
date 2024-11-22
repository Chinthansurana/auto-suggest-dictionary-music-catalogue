# Auto-Suggest in Dictionary and Music Catalogue

This project implements an auto-suggest feature using Trie data structures, caching with Redis, and a simple collaborative filtering machine learning model to improve search accuracy and speed.

## Features:
- Trie-based auto-suggest for fast lookups.
- Redis cache to optimize repeated searches.
- Basic collaborative filtering model for ranking suggestions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/auto-suggest-dictionary-music-catalogue.git
   cd auto-suggest-dictionary-music-catalogue
2. Install dependencies:
    bash
    Copy code
    pip install -r requirements.txt
3. Set up Redis on your machine:
    Install Redis from redis.io
    Start the Redis server: 
        redis-server
4. Run the program:
    python src/main.py
5. Enter a prefix when prompted to get suggested words from the dictionary and music catalog.