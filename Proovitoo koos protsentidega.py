"""Proovitöö"""
import re
import matplotlib.pyplot as plt
from tabulate import tabulate

"""
Write a program that takes input text and returns up to 10
most frequent letter compound with their percentage of occurrence presented as a table and as a bar chart.
"""
filename = input("Enter a file name:")

with open(filename, "r") as file:  # Loeb antud failist teksti sisse.
    text = file.read()
     text = text.lower()  # Muudab teksti kõik tähed väiketähtedeks.
words = re.findall(r"\w{4,}", text)  # Leiab tekstist kõik tühikuga eraldatud sõnad mis on 4 või rohkem tähte pikad.
combinations = {}
for word in words:
    for length in range(4, len(word) + 1):  # Tekitab vahemiku iga leitud sõna pikkuse kohta.
        for item in range(len(word) - length + 1):  # Leiab sõna esimese tähe vastavalt sõna pikkusest.
            if word[item: item + length] in combinations.keys():  # Kui sõna esineb sõnastikus, tõstetakse väärtust.
                combinations[word[item: item + length]] += 1
            else:
                combinations[word[item: item + length]] = 1  # Kui sõna ei ole sõnastikus, lisatakse see sinna.
# Leiab kõikide sõnade koguarvu.
total_sum_of_words = sum(combinations.values())

# Sorteerib elemendid vastavalt esinemisväärtusele.
sorted_items = sorted(combinations.items(), key=lambda x: x[1], reverse=True)
sorted_items = sorted_items[:10]

 # Tabeli loomine:
table_headers = ['Täheühend', 'Esinemise arv', 'Esinemise protsent']  # Loob tabeli esimese rea
table_data = []

for word, count in sorted_items:  # Leiab informatsiooni iga täheühendi kohta.
    percentage = (count / total_sum_of_words) * 100
    table_data.append([word, count, f'{percentage:.2f}%'])

# Tabel konsoolis esitatult:
table_str = tabulate(table_data, headers=table_headers, tablefmt="pretty")
print(table_str)

plt.figure(figsize=(8, 4))
# Määrab tabelis kuvatava info ja vorminduse.
table = plt.table(cellText=table_data, colLabels=table_headers, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
plt.axis('off')  # Eemaldab ebavajaliku skaala.
plt.title('Sõnaühendite esinemise protsent failis')
plt.show()

# Tulpdiagrammi loomine:
# Leiab informatsiooni iga täheühendi kohta.
words = [word for word, _ in sorted_items]
percentages = [(count / total_sum_of_words) * 100 for _, count in sorted_items]
max_percentage = max(percentages)  # Leiab kõige kõrgema esinemise protsendi.
max_percentage += 5

plt.figure(figsize=(10, 6))
bars = plt.bar(words, percentages, color='blue')  # Määrab kuvatava info.
# Diagrammi eri osade pealkirjad:
plt.xlabel('Täheühendid')
plt.ylabel('Esinemise protsent')
plt.title('Sõnaühendite esinemise protsent failis')
plt.xticks(rotation=0, ha='right')

# Protsentide kuvamine tulpade tipus:
for bar, percentage in zip(bars, percentages):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
             f'{percentage:.2f}%', ha='center', color='black')
plt.ylim(0, max_percentage)  # Pikendab tabelit 5% võrra.
plt.tight_layout()
plt.show()
