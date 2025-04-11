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

# supprimer les doubles: quand l'épreuve est par équipe
athletes_medailles = athlete_2016[["Medal", "NOC", "Event"]]
athletes_medailles = athletes_medailles.drop_duplicates()

# compte le nombre de médailles par pays
regroup = (
    athletes_medailles.groupby("NOC")["Medal"].value_counts().groupby("NOC")
    )

# max des médailles remportées
nb_max = max(regroup.sum())

# nombre minimum
nb_min = min(regroup.sum())

# Question 2: Le nombre de disc accesibles aux femmes et aux hommes équivalent?
# Si oui, depuis quand le sont-ils devenus?
evenement = athlete[["Year", "Sex", "Event"]]
disc_annee_hf = evenement.groupby(["Year", "Sex"])
# regroupe par année et par sexe

disc_triees = disc_annee_hf["Event"].nunique()
# ici, value_count n'aurait pas fonctionné: compte le nb d'oc d'une modalité
# Question 3: Des disciplines ont-elles disparu au fil des ans ? Lesquelles ?
d_ann = athlete[["Year", "Event"]]

# séparation des disciplines par saison
dis_an_ete = d_ann[d_ann["Year"] % 4 == 0]
dis_an_hiv = d_ann[d_ann["Year"] % 4 != 0]

# sélection de données que l'on veut comparer
c_ete = dis_an_ete[(dis_an_ete["Year"] == 2016) | (dis_an_ete["Year"] == 2012)]
c_hiv = dis_an_hiv[(dis_an_hiv["Year"] == 2014) | (dis_an_hiv["Year"] == 2010)]

# discplines qui existent aujourd'hui:
dis_ete_a = c_ete[["Event"]].drop_duplicates()

# comparaison:
dis_tot = athlete[["Event"]].drop_duplicates()
anciennes_dis = dis_tot[~dis_tot["Event"].isin(dis_ete_a["Event"])]
print(anciennes_dis)

# Question 4 en python: Classement des Athletes JO ?
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

# création d'une liste de liste contenatn le nombre de victoires associé au nom
nom = []
medal = []

for athl in res:
    if ("Bronze" in athl[-1]):
        if athl[1] in nom:
            n = nom.index(athl[1])  # indice du nom
            medal[n] += 1  # on rajoute 1 à l'indice du nom
        else:
            nom.append(athl[1])
            medal.append(1)
    if ("Silver" in athl[-1]):
        if athl[1] in nom:
            n = nom.index(athl[1])
            medal[n] += 2
        else:
            nom.append(athl[1])
            medal.append(2)
    if ("Gold" in athl[-1]):
        if athl[1] in nom:
            n = nom.index(athl[1])
            medal[n] += 3
        else:
            nom.append(athl[1])
            medal.append(3)
    liste_med = [nom, medal]
# calcule du score: point 1 pt bronze , 2 argent et 3 or
# regouper le nom et le score dans une liste de deux listes
joueur_plus_med = []
for i in range(len(medal)):
    joueur_plus_med.append([nom[i], medal[i]])

classement = sorted(joueur_plus_med, key=lambda x: x[1])
