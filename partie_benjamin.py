# minted pour implementer du code en latex
import pandas as pd
import os
import csv
import numpy as np


# python pur
# "Michael Fred Phelps, II"
def Question_1(nom_athlete):
    if not isinstance(nom_athlete, str):
        raise TypeError("Le nom de l'athlete doit être une chaîne de caractères")
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
    test = False
    for athlete in res:
        if nom_athlete in athlete[1]:
            test = True
            if (
                ("Bronze" in athlete[-1])
                or ("Silver" in athlete[-1])
                or ("Gold" in athlete[-1])
            ):
                m.append(athlete)
    if not test:
        raise Exception(
            "Cet athlete n'est pas dans la base de donnée, avez-vous bien utilisé son"
            " prénom et nom complet ?"
        )
    return f"{len(m)}"


print(Question_1("Michael Fred Phelps, II"))

##############################

# question 2: quelles sont les caractéristiques physiques +age qui remportent le plus de
# médailles


def Question_2():

    athlete = pd.read_csv(
        "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
    )
    noc = pd.read_csv("donnees_jeux_olympiques/donnees_jeux_olympiques/noc_regions.csv")

    athlete_medaille = athlete[athlete["Medal"].isin(["Bronze", "Gold", "Silver"])]

    taille_mode = athlete_medaille["Height"].value_counts()

    taille_plus_frequente = taille_mode.idxmax()
    nb_personnes_taille = taille_mode.max()
    # print(taille_plus_frequente, nb_personnes)

    poids_mode = athlete_medaille["Weight"].value_counts()

    poids_plus_frequent = poids_mode.idxmax()
    nb_personnes_poids = poids_mode.max()
    # print(poids_plus_frequent, nb_personnes)

    age_mode = athlete_medaille["Age"].value_counts()

    age_plus_frequent = age_mode.idxmax()
    nb_personnes_age = age_mode.max()
    # print(age_plus_frequent, nb_personnes)
    return (
        f"La taille qui a remporté le plus de médaille est {taille_plus_frequente}"
        f" avec {nb_personnes_taille} médailles. \n"
        f"Le poids qui a remporté le plus de médaille est {poids_plus_frequent}"
        f" avec {nb_personnes_poids} médailles. \n"
        f"L'âge qui a remporté le plus de médaille est {age_plus_frequent}"
        f" avec {nb_personnes_age} médailles."
    )


print(Question_2())

##############################

# question 3: Classement des JO toutes années confondues


# classement = pd.DataFrame({"NOC": noc["NOC"], "Score": 0})
# print(classement)
def Question_3(i):
    athlete = pd.read_csv(
        "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
    )
    noc = pd.read_csv("donnees_jeux_olympiques/donnees_jeux_olympiques/noc_regions.csv")

    def ajouter_points_si_condition(df, df_score):
        for i, ligne in df.iterrows():
            if ligne["Medal"] == "Bronze":
                df_score.loc[df_score["NOC"] == ligne["NOC"], "Score"] += 1
            if ligne["Medal"] == "Silver":
                df_score.loc[df_score["NOC"] == ligne["NOC"], "Score"] += 2
            if ligne["Medal"] == "Gold":
                df_score.loc[df_score["NOC"] == ligne["NOC"], "Score"] += 3

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
    return classement_fin.head(i)


print(Question_3(10))
