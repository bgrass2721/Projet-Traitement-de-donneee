import pandas as pd
import csv
import os

athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)
pays = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/noc_regions.csv"
    )

# Question 1:
# min et max de chaque pays
# ne garde que les athlètes de 2016
athlete_2016 = athlete[athlete["Year"] == 2016]
athlete_2016_pays = athlete_2016.merge(pays, on="NOC", how="left")

# supprimer les doubles: quand l'épreuve est par équipe
athletes_medailles = athlete_2016_pays[["Medal", "region", "Event"]]
athletes_medailles_min = athletes_medailles.drop_duplicates()

# compte le nombre de médailles par pays
regroup_min = (
    athletes_medailles_min.groupby("region")["Medal"].value_counts().groupby("region")
    )

regroup_max = (
    athletes_medailles.groupby("region")["Medal"].value_counts().groupby("region")
    )
# borne inférieure des médailles remportées JO 2016
nb_min = regroup_min.sum()


# nombre minimum
nb_max = regroup_max.sum()


##############################

# Question 2: Le nombre de disc accessibles aux femmes et aux hommes équivalent?
# Si oui, depuis quand l'est-il devenu?
# on sépare les disciplines hiver et été, pour avoir une estimation plus précise
dis_ete = athlete[athlete["Season"] == "Summer"]
dis_hiv = athlete[athlete["Season"] == "Winter"]

# on ne garde que les colonnes utiles
evenement_ete = dis_ete[["Year", "Sex", "Event"]]
evenement_hiv = dis_hiv[["Year", "Sex", "Event"]]


# on regroupe en fonction de l'année et du sexe
disc_annee_hf_ete = evenement_ete.groupby(["Year", "Sex"])
disc_annee_hf_hiv = evenement_hiv.groupby(["Year", "Sex"])

# on compte le nombre de disciplines 
disc_triees_ete = disc_annee_hf_ete["Event"].nunique()
disc_triees_hiv = disc_annee_hf_hiv["Event"].nunique()
# ici, value_count n'aurait pas fonctionné: compte le nb d'oc d'une modalité
print(disc_triees_ete)
print(disc_triees_hiv)


##############################


# Question 3: Des disciplines ont-elles disparu au fil des ans ? Lesquelles ?
d_ann = athlete[["Year", "Event", "Season"]]

# séparation des disciplines par saison
dis_an_ete = d_ann[d_ann["Season"] == "Summer"]
dis_an_hiv = d_ann[d_ann["Season"] == "Winter"]

# sélection de données que l'on veut comparer
c_ete = dis_an_ete[(dis_an_ete["Year"] == 2016) | (dis_an_ete["Year"] == 2012)]
c_hiv = dis_an_hiv[(dis_an_hiv["Year"] == 2014) | (dis_an_hiv["Year"] == 2010)]

# discplines qui existent aujourd'hui:
dis_ete_a = c_ete[["Event"]].drop_duplicates()
dis_hiv_a = c_hiv[["Event"]].drop_duplicates()

# comparaison:
# on enlève les doublons des disciplines totales et on compare
dis_tot_ete = dis_an_ete[["Event"]].drop_duplicates()
anciennes_dis_ete = dis_tot_ete[~dis_tot_ete["Event"].isin(dis_ete_a["Event"])]

dis_tot_hiv = dis_an_hiv[["Event"]].drop_duplicates()
anciennes_dis_hiv = dis_tot_hiv[~dis_tot_hiv["Event"].isin(dis_hiv_a["Event"])]


anciennes_dis_hiv.to_csv("anciennes_dis_hiv.csv", index=False)
anciennes_dis_ete.to_csv("anciennes_dis_ete.csv", index=False)


##############################

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

# création d'une liste de liste contenant le nombre de victoires associé au nom
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
