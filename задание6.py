a = 'a' 
e = 'e' 
i = 'i'  
o = 'o'  
u = 'u' 
word = input("Введите слово: ")
if not (a or e or i or o or u) in word:
    print("Слово не содержит все гласные буквы.")
else:
    print("Слово содержит все гласные буквы.")