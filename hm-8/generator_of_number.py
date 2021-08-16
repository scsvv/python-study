def prime_numbers(start, stop):
    prime_numbers_list = []    

    for number in range(start, stop):
        if number < 2:
            continue

        for i in range(2, number):
            if number % i == 0:
                break
        else:
            prime_numbers_list.append(number)

    print(prime_numbers_list)

prime_numbers(1, 100)
prime_numbers(100, 200)
