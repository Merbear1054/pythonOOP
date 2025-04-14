from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """Special Word Finder that ignores blank lines and comments."""

    def _read_words(self, path):
        """Return list of words, skipping blank lines and comments."""
        with open(path) as file:
            return [
                line.strip()
                for line in file
                if line.strip() and not line.startswith("#")
            ]
