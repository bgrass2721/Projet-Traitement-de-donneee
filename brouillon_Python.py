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

medailles = []
for athlete in res:
    if ("Bronze" in athlete[-1]) or ("Silver" in athlete[-1]) or ("Gold" in athlete[-1]):
        medailles.append(athlete)




# annee_ = [-1]
# for athlete in medailles:
#     if athlete[-1] not in

# # print(medailles)

# # medailles_pays
# for noc in country:
#     for cas in medailles:
#         if medailles[cas][1] == noc:
#             medailles_pays.append()


# [print(res[i][2]) for i in range(1, len(res))]
print(type(country[1][0]))

pays = []

def annees_participation(noc):
    """Donne le nombre d'années de participation d'un pays aux JO.
    """
    nb_annees = 0
    doublons = []  # Liste des années de participation d'un pays.
    for i in range(1, len(res)):
        if noc == res[i][7]:
        # if isinstance(res[i][3], int):
            if res[i][8] not in doublons:
                # print("True")
                nb_annees += 1
                doublons.append(res[i][8])
            # else:
            #     print("False", res[i][7])
    print(doublons)
    return nb_annees


print("Années participation USA :", annees_participation("USA"))


compte = 0
doublons = []
for i in range(1, len(medailles)):
    if "FRA" == medailles[i][7]:
        if medailles[i][8] == "2016 Summer":
           if medailles[i][1] not in doublons:
                compte += 1
                doublons.append(medailles[i][1])
print(doublons)
print("Compte :", compte)

def medailles_pays(noc):
    """Donne le nombre total d'athlètes médaillés, mais en comptant plusieurs fois ceux qui ont gagné plusieurs fois.
    """
    compte = 0
    doublons = []
    for i in range(1, len(medailles)):
        if noc == medailles[i][7]:
            if medailles[i][8] == 
            if medailles[1][1] not in doublons:
                if medailles[-1] in ("Bronze", "Silver", "Gold"):
                    compte += 1
                    doublons.append((medailles[1][0], medailles[i][8]))
    return compte

print("Médailles France :", medailles_pays("FRA"))


# def total_medailles(noc):
#     nb_medailles = 0
#     doublons = []
#     for i in range(1, len(res)):
#         if noc == res[i][7]:
#             if res[i][] not in doublons:
#                 nb_medailles += 1
#                 doublons.append((discipline, medaille, annee))
#     return nb_medailles

'''
[ligne.pop(14) for ligne in res]
[ligne.pop(12) for ligne in res]
[ligne.pop(11) for ligne in res]
[ligne.pop(8) for ligne in res]
[ligne.pop(6) for ligne in res]
[ligne.pop(5) for ligne in res]
[ligne.pop(4) for ligne in res]
[ligne.pop(3) for ligne in res]
[ligne.pop(2) for ligne in res]
'''

'''
def total_medailles(noc):
    nb_medailles = 0
    doublons = []
    for (discipline, medaille, annee) in (res[-2], res[-1], res[9]):
        if noc == res[7]:
            if (discipline, medaille, annee) not in doublons:
                nb_medailles += 1
                doublons.append((discipline, medaille, annee))
    return nb_medailles
'''
'''
moyenne_medaille_pays = []
for ligne in country:
    moyenne = total_medailles(ligne[0]) / annees_participation(ligne[0])
    moyenne_medaille_pays.append([ligne[0], ligne[1], moyenne])

print(moyenne_medaille_pays)
'''
