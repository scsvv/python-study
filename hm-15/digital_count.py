class NoWorkingSpace(Exception):
    """
    Exception, raised when in DigitalCounter use false space.
    """
    message: str = "Max value is less then minimal value"

    def __init__(self, message=None) -> None:
        if message:
            self.message = message

    def __str__(self):
        return self.message


class DigitalCounter:

    def __init__(self, min_value: int = 0, max_value: int = 0):
        """
        Create Counter with working space (start - end)

        :param min_value: start number
        :param max_value: end number
        """

        if min_value < max_value:
            self.value = min_value
            self.min_value = min_value
            self.max_value = max_value
        elif min_value > max_value:
            raise NoWorkingSpace

    def increment(self):
        if self.max_value != self.value:
            self.value += 1
        return self.value

    def decrement(self):
        if self.min_value != self.value:
            self.value -= 1
        return self.value

    def get_value(self):
        return self.value


if __name__ == "__main__":
    counter = DigitalCounter(1, 10)

    for i in range(1, 15):
        counter.increment()
    print(counter.get_value())

    for i in range(1, 15):
        counter.decrement()
    print(counter.get_value())
