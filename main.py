import csv

release = input("Are you oldfag? (Yes/No) ")

lang = input("Do you need english?(Yes/No) ")
if type(lang) != str:
    lang = 0
elif lang == "Yes":
    lang = 1
else:
    lang = 0

plats = input("What platforms you will play on?(windows/linux/mac split with \", \") ").split(", ")

age = input("How old are you? ")
try:
    age = int(age)
except ValueError:
    pass
if type(age) != int:
    age = 18
elif age < 18:
    print("Let's say it's 18 ;)")
    age = 18

genres = input("What genres do you prefer?(split with \", \") ").split(", ")

online = input("Do you want to play multiplayer?(Yes/No) ")

price = input("What max price is possible for you? ")
try:
    price = float(price)
except ValueError:
    pass

with open("steam.csv", encoding='utf-8') as file_in, open("out.txt", 'w', encoding='utf-8') as file_out:
    cvs_file = csv.reader(file_in)
    next(cvs_file)
    file_out.write("Factorio" + '\n')
    for line in cvs_file:
        if float(int(line[12]) / (int(line[12]) + int(line[13]))) * 100 < 50:
            continue

        if release == "Yes" and int(line[2].split("-")[0]) > 2000:
            continue

        if int(line[3]) < lang:
            continue

        if genres != ['']:
            j = 0
            for i in range(len(genres) + 1):
                if i != len(genres):
                    if genres[i] in line[9].split(';'):
                        break
                j = i
            if j == len(genres):
                continue

        if plats != ['']:
            for i in range(len(plats) + 1):
                if i != len(plats):
                    if plats[i] in line[6].split(';'):
                        break
                j = i
            if j == len(plats):
                continue

        if online == "Yes" and "Multi-player" not in line[8]:
            continue
        if online == "No" and "Multi-player" in line[8]:
            continue

        if age < int(line[7]):
            continue

        if type(price) == float:
            if price < float(line[len(line) - 1]):
                continue

        file_out.write(line[1] + '\n')
