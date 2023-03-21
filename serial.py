"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        # set start and next to given start value
        self.start = self.next = start
    
    def __repr__(self):
        # representation of the instabce
        return f"SerialGenerator start={self.start} and next={self.next}"
    
    def generate(self):
        # increment self by 1 and return the previous value of next
        self.next += 1
        return self.next - 1
    
    def reset(self):
        self.next = self.start
