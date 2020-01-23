s=input("Введите строку: \n").split()
c=input("Что меняем: \n")
b=input("Чем заменить: \n")
s = [item.replace("'", "") for item in s]
print (s.replace(c,b))
