import pandas as pd
import os
import csv


res = []
with open(
    os.path.join(
        "donnees_jeux_olympiques", "donnees_jeux_olympiques", "athlete_events.csv"
    )
) as fd:
    for line in fd:
        res.append(line.strip("\n").split(","))

athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)

with open(os.path.join(
    "donnees_jeux_olympiques", "donnees_jeux_olympiques", "athlete_events.csv"
)) as fd:
    file = csv.reader(fd)
    for line in file:
        res.append(line)

country = []
with open(os.path.join(
    "donnees_jeux_olympiques", "donnees_jeux_olympiques", "noc_regions.csv"
)) as fd:
    file = csv.reader(fd)
    for line in file:
        country.append(line)

'''

# Le nombre de femmes parmi les participants par année.

athlete_femme = athlete[athlete["Sex"] == "F"]
# nb_femme_an = athlete_femme.groupby("Year")["Sex"].value_counts().groupby("Year").sum()

nb_femme_an = athlete_femme.groupby("Year")["Name"].value_counts().groupby("Year").sum()
nb_athlete_an = athlete.groupby("Year")["Name"].value_counts().groupby("Year").sum()

print("Nombre de participants par année :", nb_athlete_an)

print("Nombre de femmes parmi les participants par année : ", nb_femme_an)


proportion_femme_an = nb_femme_an.div(nb_athlete_an)
print("Proportion de femmes par année : ", proportion_femme_an)


# La moyenne des médailles remportées par les athlètes du Royaume-Uni.

athlete_UK = athlete[athlete["NOC"] == "GBR"]
print("Athlètes du Royaume-Uni : ", athlete_UK)
athlete_UK_ete = athlete_UK[athlete_UK["Season"] == "Summer"]
medailles_UK_ete = athlete_UK_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()

print("Médailles du Royaume-Uni : ", medailles_UK_ete)
print("Moyenne des médailles du Royaume-Uni : ", medailles_UK_ete.mean())


# La moyenne des médailles remportées par les athlètes de la Chine


athlete_chine = athlete[athlete["NOC"] == "CHN"]
print("Athlètes de la Chine : ", athlete_chine)
athlete_chine_ete = athlete_chine[athlete_chine["Season"] == "Summer"]
medailles_chine_ete = athlete_chine_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()

print("Médailles de la Chine : ", medailles_chine_ete)
print("Moyenne des médailles de la Chine : ", medailles_chine_ete.mean())



# La moyenne des médailles remportées par les athlètes de la Chine


athlete_US = athlete[athlete["NOC"] == "USA"]
print("Athlètes des Etats-Unis : ", athlete_US)
athlete_US_ete = athlete_US[athlete_US["Season"] == "Summer"]
medailles_US_ete = athlete_US_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()

print("Médailles des Etats-Unis : ", medailles_US_ete)
print("Moyenne des médailles des Etats-Unis : ", medailles_US_ete.mean())
'''



# Combien de médailles les pays participants ont-ils gagné en moyenne par JO ?


[ligne.pop(14) for ligne in res]
[ligne.pop(12) for ligne in res]
[ligne.pop(11) for ligne in res]
[ligne.pop(8) for ligne in res]
[ligne.pop(6) for ligne in res]
[ligne.pop(5) for ligne in res]
[ligne.pop(4) for ligne in res]
[ligne.pop(3) for ligne in res]
[ligne.pop(2) for ligne in res]
[ligne.pop(1) for ligne in res]

medailles = []
for athlete in res:
    if ("Bronze" in athlete[-1]) or ("Silver" in athlete[-1]) or ("Gold" in athlete[-1]):
        medailles.append(athlete)
'''
annee_ = [-1]
for athlete in medailles:
    if athlete[-1] not in

# print(medailles)

medailles_pays
for noc in country:
    for cas in medailles:
        if medailles[cas][1] == noc:
            medailles_pays.append()
'''

pays = []


def annees_participation(noc):
    nb_annees = 0
    doublons = []
    for annee in res[9]:
        if annee not in doublons:
            if noc == res[7]:
                nb_annees += 1
                doublons.append(annee)
    return nb_annees


def total_medailles(noc):
    nb_medailles = 0
    doublons = []
    for (discipline, medaille, annee) in (res[-2], res[-1], res[9]):
        if noc == res[7]:
            if (discipline, medaille, annee) not in doublons:
                nb_medailles += 1
                doublons.append((discipline, medaille, annee))
    return nb_medailles


moyenne_medaille_pays = []
for ligne in country:
    moyenne = total_medailles(ligne[0]) / annees_participation(ligne[0])
    moyenne_medaille_pays.append([ligne[0], ligne[1], moyenne])

print(moyenne_medaille_pays)
