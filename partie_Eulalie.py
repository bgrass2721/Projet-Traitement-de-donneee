import pandas as pd
import csv
import os
import matplotlib.pyplot as plt
import seaborn as sns

athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)
pays = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/noc_regions.csv"
    )

# Question 1:
# min et max de chaque pays
# ne garde que les athlètes de 2016


def bornes_medailles(annee):
    """Renvoie les bornes inférieures et supérieures des médailles
    pour chaque pays

    parameters:
    annee (int): L'année des Jeux Olympiques

    Returns:
    DataFrame: Tableau avec les pays, bornes inférieures et supérieures
    """
    athlete_2016 = athlete[athlete["Year"] == annee]
    athlete_2016_pays = athlete_2016.merge(pays, on="NOC", how="left")
    # supprimer les doubles: quand l'épreuve est par équipe
    # ainsi on peut enlever tous les doublons
    #  tous les joueurs d'une même équipe auront les mêmes informations
    athletes_medailles = athlete_2016_pays[["Medal", "region", "Event"]]
    athletes_medailles_min = athletes_medailles.drop_duplicates()

    # compte le nombre de médailles par pays
    # on séprare le code en deuc étapes pour min, pour respecter falk8
    regroup = (
        athletes_medailles_min.groupby("region")["Medal"].value_counts()
        )

    regroup_min = regroup.groupby("region")

    # compteur max
    regroup_max = (
        athletes_medailles.groupby("region")["Medal"].value_counts().groupby("region")
        )

    # borne inférieure des médailles remportées JO 2016
    nb_min = regroup_min.sum()
    table_min = pd.DataFrame(nb_min).reset_index("region")

    # nombre maximum avec sport par equipe et cas exaequo dans le même pays
    nb_max = regroup_max.sum()
    table_max = pd.DataFrame(nb_max).reset_index("region")

    # renommer le noms des colonnes
    table_min = table_min.rename(columns={"Medal": "Bornes inférieures"})
    table_max = table_max.rename(columns={"Medal": "Bornes supérieures"})

    table_max_min = pd.merge(
        table_max[["region", "Bornes supérieures"]],
        table_min[["region", "Bornes inférieures"]],
        on="region"
        )
    table_max_min.to_csv("tableau_bornes_sup_et_inf.csv", index=False)

    return table_max_min


##############################

# Question 2: Le nombre de disc accessibles aux femmes et aux hommes équivalent?
# Si oui, depuis quand l'est-il devenu?
# on sépare les disciplines hiver et été, pour avoir une estimation plus précise

def parite_disc_hommes_femmes():
    """Renvoie un graphique avec les porucentages de discplines féminines aux JO
    Les graphiques sont aussi sauvegardés

    parameters:

    Returns:
    plot: graphiques avec les pourcentages de femmes aux jo
    d'été et d'hver côte à côte
    """
    dis_ete = athlete[athlete["Season"] == "Summer"]
    dis_hiv = athlete[athlete["Season"] == "Winter"]

    # on ne garde que les colonnes utiles pour puvoir faire des group_by
    evenement_ete = dis_ete[["Year", "Sex", "Event"]]
    evenement_hiv = dis_hiv[["Year", "Sex", "Event"]]

    # on regroupe en fonction de l'année et du sexe
    disc_annee_hf_ete = evenement_ete.groupby(["Year", "Sex"])
    disc_annee_hf_hiv = evenement_hiv.groupby(["Year", "Sex"])
    disc_annee_ete = evenement_ete.groupby(["Year"])
    disc_annee_hiv = evenement_hiv.groupby(["Year"])

    # on compte le nombre de disciplines
    disc_triees_ete = disc_annee_hf_ete["Event"].nunique()
    disc_triees_hiv = disc_annee_hf_hiv["Event"].nunique()

    # en ne comptant qu'une fois les disciplines mixtes
    disc_tot_ete = disc_annee_ete["Event"].nunique()
    disc_tot_hiv = disc_annee_hiv["Event"].nunique()

    # ici, value_count n'aurait pas fonctionné: compte le nb d'oc d'une modalité
    # problème: si on convertit en dataframe, le Year et le Sexe disparaissent
    # ce ne sont plus des colonnes
    # en fait, le group_by a transformé en index ces colonnes,
    # donc il faut réinitialiser l'index

    disc_table_ete = disc_triees_ete.reset_index(name='Nb_disc_f')
    disc_table_hiv = disc_triees_hiv.reset_index(name='Nb_disc_f')
    disc_table_ete_tot = disc_tot_ete.reset_index(name='Nb_disc_tot')
    disc_table_hiv_tot = disc_tot_hiv.reset_index(name='Nb_disc_tot')

    # pour faire pourcentage ensuite
    disc_table_ete_f = disc_table_ete[disc_table_ete["Sex"] == "F"]
    disc_table_hiv_f = disc_table_hiv[disc_table_hiv["Sex"] == "F"]

    # calcul du pourcentage pour été
    disc_table_ete = pd.merge(
        disc_table_ete_f[["Year", "Nb_disc_f"]],
        disc_table_ete_tot[["Year", "Nb_disc_tot"]],
        on="Year"
        )

    disc_table_ete["Pct_f"] = disc_table_ete["Nb_disc_f"] / (
        disc_table_ete["Nb_disc_tot"]
        ) * 100

    # calcul du pourcentage pour hiver
    disc_table_hiv = pd.merge(
        disc_table_hiv_f[["Year", "Nb_disc_f"]],
        disc_table_hiv_tot[["Year", "Nb_disc_tot"]],
        on="Year"
    )

    # pourcentage hiver
    disc_table_hiv["Pct_f"] = disc_table_hiv["Nb_disc_f"] / (
        disc_table_hiv["Nb_disc_tot"]
    ) * 100

    # graphique côte à côte des disciplines été et hiver
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.tight_layout(pad=5.0)  # espacement entre les sous-graphiques

    # Graphique pour l'été
    sns.barplot(data=disc_table_ete, x="Year", y="Pct_f", color="blue", ax=axes[0])
    axes[0].set_title("Pourcentage de disciplines féminines aux JO d'été")
    axes[0].set_ylabel("Pourcentage de disciplines féminines (%)")
    axes[0].tick_params(axis='x', rotation=45)

    # Graphique pour l'hiver
    sns.barplot(data=disc_table_hiv, x="Year", y="Pct_f", color="blue", ax=axes[1])
    axes[1].set_title("Pourcentage de disciplines féminines aux JO d'hiver")
    axes[1].set_ylabel("Pourcentage de disciplines féminines (%)")
    axes[1].tick_params(axis='x', rotation=45)

    # Sauvegarde des graphiques dans des fichiers
    plt.savefig("pourcentage_disciplines_feminines_été_hiver.png")
    plt.show()
    return "\nOn peut voir que les JO se rapprochent d'une équité en terme de nombre de disciplines"

##############################


# Question 3: Des disciplines ont-elles disparu au fil des ans ? Lesquelles ?
def disciplines_disp():
    """Renvoie deux tableaux avec les disciplines disparues de JO
    Les disciplines sont considérées comme ayant disparues si cela fait 2 JO au moins
    qu'elles n'ont pas été aux JO. Il fallait donc comparer en fonction de 2012 et 2016.
    Pour ne pas afficher quelque chose de trop lourd, seul un dizaine de
    disciplines sont affichées de manière aléatoire.
    Les tableaux affichant toutes les disciplines disparus aux JO d'été et
    d'hiver sont aussi sauvegardées.

    parameters:

    Returns:
    dataframe: 2 dataframe avec disciplines disparues des JO
    """
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

    # échantillons aléatoires de dix discplines disparues
    ech_ete = anciennes_dis_ete.sample(n=min(10, len(anciennes_dis_ete))).reset_index(drop=True)
    ech_hiv = anciennes_dis_hiv.sample(n=min(10, len(anciennes_dis_hiv))).reset_index(drop=True)

    # meilleur affichage
    disc_disp_ete_hiv = {
        "Disciplines disparues aux JO d'été": ech_ete,
        "Disciplines disparues aux JO d'hiver": ech_hiv
    }

    return disc_disp_ete_hiv


# print(disciplines_disp())

##############################


# Question 4 en python: Classement des Athletes JO ?
def classement_competiteurs(nombre):
    """Renvoie un classement des compétiteurs les plus médaillés
    toutes disciplines confondues. Ne renvoie que les 10 premiers,
    le classement est trop long sinon.
    Le classement a été fait de cette manière:
    - 3 point pour une médaille d'or
    - 2 point pour une médaille d'argent
    - 1 point pour une médaille de bronze

    parameters:

    Returns:
    list[list[str]]: liste avec 10 premier du classements et leur score
    """
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

    # calcul du score: point 1 pt bronze , 2 argent et 3 or
    # regouper le nom et le score dans une liste de deux listes
    joueur_plus_med = []
    for i in range(len(medal)):
        joueur_plus_med.append([nom[i], medal[i]])

    classement = sorted(joueur_plus_med, key=lambda x: x[1])

    top10 = classement[-nombre:]
    # les 10 derniers éléments parce que liste ordre croissant
    top10 = top10[::-1]

    return top10
