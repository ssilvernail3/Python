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
    def __init__(self, start=0):
        """Make a new generator, staring with start """
        self.start = self.next = start

    def __repr__(self):
        return f'<SerialGenerator start ={self.start} next = {self.next}'
        
    def generate(self):
        """Generate next sequential number after start"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """reset serial generator to start value"""
        self.next = self.start
        