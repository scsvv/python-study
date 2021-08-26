def count_first(nums, n: int) -> list:
    def loop(k: int) -> int:
        if k == 1:
            return 1
        return loop(k - loop(k - 1)) + 1

    sequence = list()

    for i in range(1, n + 1):
        sequence.append(loop(i))

    return sequence


if __name__ == "__main__":
    print(count_first(None, 2))
    print(count_first(None, 5))