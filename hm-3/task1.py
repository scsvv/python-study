#ожидаемая фраза 
PASSWORD = "qwerty" 

#фраза, которую вводит юзер
client_password = input("Введите пароль: ") 

#проверка введенных значений с ожидаемым
if client_password == PASSWORD: print("В вошли в учётную запись")
else: print("Не верный пароль")