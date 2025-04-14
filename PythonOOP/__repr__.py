class SerialGenerator:
    """Class for generating unique serial numbers."""

    def __init__(self, start=0):
        """Create new generator starting at `start`."""
        self.start = start
        self.next = start

    def generate(self):
        """Return next serial number."""
        current = self.next
        self.next += 1
        return current

    def reset(self):
        """Reset number to original start."""
        self.next = self.start

    def __repr__(self):
        """Return a string representation of the object for debugging."""
        return f"<SerialGenerator start={self.start} next={self.next}>"
