# minted pour implementer du code en latex
import pandas as pd
import os
import csv
import numpy as np

# Charger un fichier CSV
athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)
noc = pd.read_csv("donnees_jeux_olympiques/donnees_jeux_olympiques/noc_regions.csv")

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
# print(nombre_medaille_phelps)


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
# print(len(m))


##############################

# question 2: quelles sont les caractéristiques physiques +age qui remportent le plus de
# médailles

athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)
noc = pd.read_csv("donnees_jeux_olympiques/donnees_jeux_olympiques/noc_regions.csv")

athlete_medaille = athlete[athlete["Medal"].isin(["Bronze", "Gold", "Silver"])]

taille_mode = athlete_medaille["Height"].value_counts()

taille_plus_frequente = taille_mode.idxmax()
nb_personnes = taille_mode.max()
# print(taille_plus_frequente, nb_personnes)

poids_mode = athlete_medaille["Weight"].value_counts()

poids_plus_frequent = poids_mode.idxmax()
nb_personnes = poids_mode.max()
# print(poids_plus_frequent, nb_personnes)

age_mode = athlete_medaille["Age"].value_counts()

age_plus_frequent = age_mode.idxmax()
nb_personnes = age_mode.max()
# print(age_plus_frequent, nb_personnes)

##############################

# question 3: Classement des JO toutes années confondues

# classement = pd.DataFrame({"NOC": noc["NOC"], "Score": 0})
# print(classement)


def ajouter_points_si_condition(df, df_score):
    for i, ligne in df.iterrows():
        if ligne["Medal"] == "Bronze":
            df_score.loc[df_score["NOC"] == ligne["NOC"], "Score"] += 1
        if ligne["Medal"] == "Silver":
            df_score.loc[df_score["NOC"] == ligne["NOC"], "Score"] += 2
        if ligne["Medal"] == "Gold":
            df_score.loc[df_score["NOC"] == ligne["NOC"], "Score"] += 3


# ajouter_points_si_condition(athlete, classement)
# classement_gen = classement.sort_values(by="Score", ascending=False)
# classement_gen = classement_gen.reset_index(drop=True)
# print(classement_gen)

# Création du DataFrame de classement initial
classement = pd.DataFrame({"NOC": noc["NOC"], "Score": 0})

# Ajouter des points en fonction de la médaille dans athlete
athlete["Points"] = np.select(
    [
        athlete["Medal"] == "Bronze",
        athlete["Medal"] == "Silver",
        athlete["Medal"] == "Gold",
    ],
    [1, 2, 3],
    default=0,
)

# Agréger les points par NOC dans athlete
athlete_points = athlete.groupby("NOC")["Points"].sum().reset_index()

# Fusionner les DataFrames avec les scores agrégés
classement = classement.merge(athlete_points, on="NOC", how="left")

# Ajouter les points au classement
classement["Score"] += classement["Points"].fillna(0).astype(int)

# Trier le classement par score en ordre décroissant et réinitialiser l'index
classement_gen = classement.sort_values(by="Score", ascending=False).reset_index(
    drop=True
)
classement_gen.index = classement_gen.index + 1  # Ajuster pour commencer à 1
classement_fin = classement_gen[["NOC", "Score"]]

# Afficher le classement final
# print(classement_fin)
# Exporter le DataFrame vers un fichier CSV
classement_fin.to_csv("classement_final.csv", index=False)
