from random import randint


class Buffer:
    def __init__(self):
        self.subsequence: list = list()
        self.sum_of_five_elements: int = 0

    def add(self, *args) -> None:
        for number in args:
            self.subsequence.append(number)

            if len(self.subsequence) == 5:
                for element in self.subsequence:
                    self.sum_of_five_elements += element
                self.subsequence.clear()
                print(f"Sum of five elements: {self.sum_of_five_elements}")
                self.sum_of_five_elements = 0

    def get_current_part(self) -> list:
        return self.subsequence


if __name__ == "__main__":
    buffer = Buffer()

    for i in range(10):
        elements: list = [randint(0, 25) for j in range(randint(1, 15))]
        print(f"Generated sequence: {elements}")
        buffer.add(*elements)
        print(f"Current part in buffer: {buffer.get_current_part()}")
