str = input("Введите два слова: ")
sentence = ''

str = str.split(" ")

for word in str[::-1]:
    for i in word[::-1]:
        sentence += i.lower()
    sentence += " "

sentence = sentence.title()
print(sentence)
