s=input("Введите строку: \n").split()
b=s[0]
for i in range(len(s)):
    if len(s[i-1])>len(s[i]):
        b=s[i-1]
print("Самое длинное слово:",b, "длина" ,len(b))
