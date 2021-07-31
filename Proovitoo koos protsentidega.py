import string
import math

filename = input("Enter a file name: ")

with open(filename, "r") as file:
    text = file.read()
    words = text.split()
    table = str.maketrans("", "", string.punctuation)
    stripped = [char.translate(table) for char in words]
#Eemaldasin kirjavahemärgid tekstist

Count = len(stripped)
Percentage = Count *100

word_dict = dict()

for word in stripped:
    if word in word_dict:
        word_dict[word] = word_dict[word] + 1
    else:
        word_dict[word] = 1
#Loendan kõik sõnad hulga poolest ja lisan nad dictionarisse

for word in tuple(word_dict.keys()):
    if word.isdigit():
        del word_dict[word]
#Ei võimalda lisada nubmreid dictionarisse

#print(sorted(zip(word_dict.values(), word_dict.keys())))

from collections import Counter

C = Counter(word_dict)
high = C.most_common(10)

print("Top10 sõna")
print("Nimi: Kogus")

for i in high:
    print(i[0],':',(i[1] / Count * 100).__format__(".2f"), "%")


#Otsisin välja top10 enim esinevat sõna ja prindin need välja tabelina

import matplotlib.pyplot as plot

Top10 = dict(C.most_common(10))
x = list(Top10.keys())
y = list(Top10.values())

plot.bar(x, y)
plot.xticks(rotation=90)
plot.xlabel("Sõnad")
plot.ylabel("Kogus")
plot.title("Top10 enimesinevat sõna")
plot.show()
#Loon tulpdiagrammi kasutades varemloodud most_common listi, keeran s6nad vertikaalselt, et k6ik mahuks diagrammile.