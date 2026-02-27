vowels = 'aeiou'
word = input("Введите слово: ")
for v in vowels:
    if v in word:
        print("Слово содержит гласные.")
        break
    else:
        print("Слово не содержит гласные.")
        break