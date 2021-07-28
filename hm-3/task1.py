#ожидаемая фраза 
PASSWORD = "qwerty" 

#фраза, которую вводит юзер
client_password = input("Введите пароль: ") 

#проверка введенных значений с ожидаемым
print("В вошли в учётную запись" if client_password == PASSWORD else "Не верный пароль" )