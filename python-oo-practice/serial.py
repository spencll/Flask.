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
    def __init__(self, start):
        self.start = start
        self.next = self.start
    
    def generate(self):
        """counter prepares next function call but returns current num"""
        self.next  +=1 
        return self.next -1
    
    def reset(self):
        """resets back to start"""
        self.next = self.start 
    

