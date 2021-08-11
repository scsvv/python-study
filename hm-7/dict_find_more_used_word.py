string = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure in dolor reprehenderit voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''

string: list = string.split()
words: set = set(string)

dict_of_word : dict = dict()

worked = False
count = 0

for word in words:
    key = string.count(word)
    
    if dict_of_word.get(key) == None:
        dict_of_word[key] = list()
    
    if key > 1 and dict_of_word[key].count(word) == 1:
        continue

    dict_of_word[key].append(word)

for i in dict_of_word.keys():
    if i > count:
        count = i

for item in string[::-1]:
    for element in dict_of_word[count]:
        if item == element:
            print(item)
            worked = True
            break     
    if(worked == True):
        break
     
