# minted pour implementer du code en latex
import pandas as pd
import os
import csv

# Charger un fichier CSV
athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)
noc = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/noc_regions.csv"
    )

# Afficher les premières lignes du fichier
# print(athlete.head(), noc.head())
# print(athlete)

# Déterminez le nombre de médailles gagnées par Michael Phelps. Son nom complet est
# Michael Fred Phelps, II.

# Sélectionner les lignes où la colonne 'a' vaut 'b'
m_p = athlete[athlete["Name"] == "Michael Fred Phelps, II"]
m_p_g = m_p[m_p["Medal"].isin(["Bronze", "Gold", "Silver"])]
# Afficher le résultat
# print(m_p_g)

nombre_medaille_phelps = len(m_p_g)
print(nombre_medaille_phelps)


# python pur


res = []

with open(
    os.path.join(
        "donnees_jeux_olympiques", "donnees_jeux_olympiques", "athlete_events.csv"
    )
) as fd:
    file = csv.reader(fd)
    for line in file:
        res.append(line)

m = []
for athlete in res:
    if "Michael Fred Phelps, II" in athlete[1]:
        if (
            ("Bronze" in athlete[-1])
            or ("Silver" in athlete[-1])
            or ("Gold" in athlete[-1])
        ):
            m.append(athlete)
print(len(m))


##############################

# question 2:
