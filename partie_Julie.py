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

# Le nombre de femmes parmi les participants par année.

athlete_femme = athlete[athlete["Sex"] == "F"]
nb_femme_an = athlete_femme.groupby("Year")["Sex"].value_counts().groupby("Year").sum()

print("Nombre de femmes parmi les participants par année : ", nb_femme_an)

proportion_femme_an = nb_femme_an.apply[]()

# La moyenne des médailles remportées par les athlètes du Royaume-Uni.

athlete_UK = athlete[athlete["NOC"] == "GBR"]
print("Athlètes du Royaume-Uni : ", athlete_UK)
athlete_UK_ete = athlete_UK[athlete_UK["Season"] == "Summer"]
medailles_UK_ete = athlete_UK_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()

print("Médailles du Royaume-Uni : ", medailles_UK_ete)
print("Moyenne des médailles du Royaume-Uni : ", medailles_UK_ete.mean())



# Combien de médailles les pays participants ont-ils gagné en moyenne par JO ?

