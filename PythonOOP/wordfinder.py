import random

class WordFinder:
    """Word Finder: reads a file and returns random words."""

    def __init__(self, path):
        """Read file and report number of words read."""
        self.words = self._read_words(path)
        print(f"{len(self.words)} words read")

    def _read_words(self, path):
        """Read words from file and return as a list (stripping newlines)."""
        with open(path) as file:
            return [line.strip() for line in file if line.strip()]

    def random(self):
        """Return a random word."""
        return random.choice(self.words)
