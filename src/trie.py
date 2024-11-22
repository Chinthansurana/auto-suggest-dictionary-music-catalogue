from collections import defaultdict, Counter
import redis

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(node.suggestions) < 5:
                node.suggestions.append(word)
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.suggestions

class TrieWithFrequency(Trie):
    def __init__(self):
        super().__init__()
        self.word_freq = Counter()

    def insert(self, word):
        super().insert(word)
        self.word_freq[word] += 1

    def search_with_ranking(self, prefix):
        suggestions = super().search(prefix)
        return sorted(suggestions, key=lambda x: -self.word_freq[x])

class TrieWithRedisCache(TrieWithFrequency):
    def __init__(self, redis_host='localhost', redis_port=6379):
        super().__init__()
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    def insert(self, word):
        super().insert(word)
        self.redis.hincrby('word_freq', word, 1)

    def search_with_cache(self, prefix):
        cached = self.redis.get(f'prefix:{prefix}')
        if cached:
            return cached.decode('utf-8').split(',')
        suggestions = super().search(prefix)
        self.redis.set(f'prefix:{prefix}', ','.join(suggestions))
        return suggestions
