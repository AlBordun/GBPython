# Задача 34:
def count_vowels(word):
    i = 0
    for s in word:
        if s.lower() in vowels: i=i+1
    return i
#phrase = intput()
phrase =  "пара-ра-рам  рам-пам-папам  па-ра-па-да".split()

res = 0
def_vowels = count_vowels(phrase[0])
for w in phrase:
    res = res + count_vowels(w)
print(["Парам пам-пам" if (res / def_vowels == len(phrase)) else "Пам парам"])