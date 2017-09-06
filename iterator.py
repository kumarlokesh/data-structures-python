class Sample(object):
    def __init__(self, value, max_iterations):
        self.value = value
        self.max_iterations = max_iterations
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_iterations:
            raise StopIteration
        self.count += 1
        return self.value

    # Ensure iterator compatibility for Python version 2.x
    def next(self):
        return self.__next__()
