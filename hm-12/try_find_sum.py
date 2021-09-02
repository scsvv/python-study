def find_sum_of_number(a: str, b: str):
    try:
        return float(a) + float(b)
    except ValueError:
        return str(a) + str(b)


if __name__ == "__main__":
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    print(find_sum_of_number(a, b))
