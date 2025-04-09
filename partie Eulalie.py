import pandas as pd
import csv
import os


athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)
# Question 1:
# min et max de chaque pays
# ne garde que les athlètes de 2016
athlete_2016 = athlete[athlete["Year"] == 2016]

# suprpime les doubles: quand l'épreuve est par équipe
athletes_medailles = athlete_2016[["Medal", "NOC", "Event"]]
athletes_medailles = athletes_medailles.drop_duplicates()

# compte le nombre de médaille par pays
regroup = (
    athletes_medailles.groupby("NOC")["Medal"].value_counts().groupby("NOC")
    )

# max des médailles remportées
nb_max = max(regroup.sum())

# nombre minimum
nb_min = min(regroup.sum())

# Question 2: Le nombre de disc accesibles aux femmes et aux hommes est-il équilavent?
# Si oui, depuis quand le sont-ils devenus?

# Question 3 en python: Classement des Athletes JO ?
res = []
# transfomartion données
with open(
    os.path.join(
        "donnees_jeux_olympiques", "donnees_jeux_olympiques", "athlete_events.csv"
    )
) as fd:
    file = csv.reader(fd)
    for line in file:
        res.append(line)

nom = []
medal = []

for athlete in res:
    if ("Bronze" in athlete[-1]):
        if athlete[1] in nom:
            n = nom.index(athlete[1])  # indice du nom
            medal[n] += 1  # on rajoute 1 à l'indice du nom
        else:
            nom.append(athlete[1])
            medal.append(1)
    if ("Silver" in athlete[-1]):
        if athlete[1] in nom:
            n = nom.index(athlete[1])
            medal[n] += 2
        else:
            nom.append(athlete[1])
            medal.append(2)
    if ("Gold" in athlete[-1]):
        if athlete[1] in nom:
            n = nom.index(athlete[1])
            medal[n] += 3
        else:
            nom.append(athlete[1])
            medal.append(3)
    liste_med = [nom, medal]


joueur_plus_med = []
for i in range(len(medal)):
    joueur_plus_med.append([nom[i], medal[i]])

classement = sorted(joueur_plus_med, key=lambda x: x[1])
# prénom dans liste rajouter point 1 pt bronze , 2 argent et 3 or

# Question 4: Des disciplines ont-elles disparu au fil des ans? Si oui, lesquelles?
