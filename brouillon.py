import pandas as pd
import os
import csv

# Table athlètes liste
res = []
with open(
        os.path.join(
            "donnees_jeux_olympiques", "donnees_jeux_olympiques", "athlete_events.csv"
        )
    ) as fd:
        file = csv.reader(fd)
        for line in file:
            res.append(line)

# Table NOC liste
country = []
with open(
        os.path.join(
            "donnees_jeux_olympiques", "donnees_jeux_olympiques", "noc_regions.csv"
        )
    ) as fd:
        file = csv.reader(fd)
        for line in file:
            country.append(line)

# Combien de médaillés les pays participants ont-ils compté en moyenne par JO ?

def annees_participation(noc):
    """Donne le nombre d'années de participation d'un pays aux JO.
    """
    nb_annees = 0
    games = []  # Liste des années de participation d'un pays.
    for i in range(1, len(res)):
        if noc == res[i][7]:
        # if isinstance(res[i][3], int):
            if res[i][8] not in games:
                # print("True")
                nb_annees += 1
                games.append(res[i][8])
            # else:
            #     print("False", res[i][7])
    # print(games)
    return nb_annees, games


def participants_pays(noc, games):
    """Donne le nombre total de participants, mais en comptant plusieurs fois ceux qui ont participé plusieurs fois.
    """
    compte = 0
    participant = []
    for i in range(1, len(res)):
        if noc == res[i][7]:
            # print("Noc OK")
            if games == res[i][8]: 
                # print("Games OK")
                if res[i][1] not in participant:
                    compte += 1
                    participant.append(res[i][1])
    # print(participant)
    return compte


def moyenne_participants(noc):
    nb_annees, liste_jeux = annees_participation(noc)
    total = 0
    for jeu in liste_jeux:
        compte_participants = participants_pays(noc, jeu)
        print(f"{jeu}. {compte_participants}")
        total += compte_participants
    moyenne = total / nb_annees
    return moyenne

