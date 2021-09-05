user_str: str = ''

while True:
    tmp = input("Введите строку: ")
    user_str += f'{tmp}\n'
    if tmp == "":
        break

with open(r"session_data.txt", "w", encoding="utf=8") as session:
    session.write(user_str)
    session.close()
