string = "sit Lorem ipsum dolor ipsum sit amet ipsum consectetur sit adipiscing elit"
string = string.split()

# словарь в котором хранятся все слова, где ключ - количество раз, а значение список из слов
words_repeats: dict = dict()


# алгоритм для хранинения в словаре под значением слова, а под ключ'м количество повторений
for word in string:
    key = string.count(word)
    
    if words_repeats.get(key) == None:
        words_repeats[key] = list()
    
    if key > 1 and words_repeats[key].count(word) == 1:
        continue

    words_repeats[key].append(word)


print(words_repeats)