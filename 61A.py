s=input("Введите имя:\n")
print (s)
s1=""
for z in s:
    if z=="а": z="б"
    elif z=="б": z="а"
    elif z=="А": z="Б"
    elif z=="Б": z="А"
    s1=s1+z
print (s1)
