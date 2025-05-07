import pandas as pd
import csv
import os
import matplotlib.pyplot as plt


# # Table athlètes df
# athlete = pd.read_csv(
#     "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
# )

# # Table noc df
# country_df = pd.read_csv(
#     "donnees_jeux_olympiques/donnees_jeux_olympiques/noc_regions.csv"
# )

###############################################################################

def prop_athletes_femmes():
    """Renvoie la proportion de femme associée à chaque édition des JO et
    affiche le barplot correspondant.

    Parameters
    ----------
    None

    Returns
    -------
    str
    """

    # Table athlètes df
    athlete = pd.read_csv(
        "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
    )

    year = []
    for i in range(1896, 2017, 4):
        year.append(i)

    # Argument vide ou mettre la table comme argument ?
    athlete_femme = athlete[athlete["Sex"] == "F"]
    nb_femme_an = athlete_femme.groupby("Year")["Name"].\
        value_counts().groupby("Year").sum()
    nb_athlete_an = athlete.groupby("Year")["Name"].\
        value_counts().groupby("Year").sum()
    proportion_femme_an = nb_femme_an.div(nb_athlete_an)
    proportion_femme_an = proportion_femme_an.\
        reset_index(name="Proportion de femmes")

    proportion_femme_an.to_csv("proportion_femme_an.csv", index=False)

    plt.bar(
        proportion_femme_an["Year"],
        proportion_femme_an["Proportion de femmes"],
        width=1.5
    )
    plt.grid(which="both", axis="y")
    plt.xticks(year, rotation=90)
    plt.yticks([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5])
    plt.xlabel("Année")
    plt.ylabel("Proportion de femmes")
    plt.title("Proportion de femmes par an parmi les athlètes olympiques")
    plt.savefig("Proportion_femmes.png")
    plt.show()

    return "\nLes femmes sont de plus en plus représentées depuis 1896."


###############################################################################

# La moyenne des médailles remportées par les athlètes de la Chine

def perf_chine():
    """Donne le nombre de médaillés chinois par année, ainsi que la moyenne
    des médaillés, et affiche un barplot qui permet la comparaison entre les
    deux.

    Parameters
    ----------
    None

    Returns
    -------
    str
    """
    # Table athlètes df
    athlete = pd.read_csv(
        "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
    )

    med = []
    for i in range(0, 191, 20):
        med.append(i)

    athlete_chine = athlete[athlete["NOC"] == "CHN"]
    athlete_chine_ete = athlete_chine[athlete_chine["Season"] == "Summer"]

    medailles_chine_ete = athlete_chine_ete.groupby("Year")["Medal"].\
        value_counts().groupby("Year").sum()
    moyenne = medailles_chine_ete.mean()

    medailles_chine_ete = medailles_chine_ete.reset_index(name='Medals')
    medailles_chine_ete.to_csv("performance_chine.csv", index=False)

    plt.bar(
        medailles_chine_ete["Year"],
        medailles_chine_ete["Medals"],
        width=3
    )
    plt.grid(which="both", axis="y")
    plt.axhline(y=moyenne, xmin=0, xmax=2018, color="red")
    plt.text(1981.25, 104, "Moyenne", color="red")
    plt.text(2006.125, -20, "(Pékin)")
    plt.xticks(medailles_chine_ete["Year"])
    plt.yticks(med)
    plt.xlabel("Année")
    plt.ylabel("Médailles de la Chine")
    plt.title("Performance de la Chine aux Jeux Olympiques")
    plt.savefig("Chine.png")
    plt.show()

    return f"""\nLes JO de Pékin 2008 se démarquent par rapport à la moyenne
    de la Chine, qui est de {moyenne}."""

###############################################################################

# Combien d'athlètes ont participé en moyenne par pays (question en Python) ?

# # Table athlètes liste
# res = []
# with open(
#         os.path.join(
#             "donnees_jeux_olympiques",
#             "donnees_jeux_olympiques",
#             "athlete_events.csv"
#         )
#     ) as fd:
#         file = csv.reader(fd)
#         for line in file:
#             res.append(line)

# # Table NOC liste
# country = []
# with open(
#         os.path.join(
#             "donnees_jeux_olympiques",
#             "donnees_jeux_olympiques",
#             "noc_regions.csv"
#         )
#     ) as fd:
#         file = csv.reader(fd)
#         for line in file:
#             country.append(line)


# def annees_participation(noc):
#     """Donne le nombre de participation d'un pays aux JO et la liste des
#     jeux en question.

#     Parameters
#     ----------
#     noc : str
#         Le NOC du pays dont on veut connaitre le nombre d'années de
#         participation.

#     Returns
#     -------
#     int
#     list
#     """
#     nb_annees = 0
#     games = []  # Liste des années de participation d'un pays.
#     for i in range(1, len(res)):
#         if noc == res[i][7]:
#         # if isinstance(res[i][3], int):
#             if res[i][8] not in games:
#                 # print("True")
#                 nb_annees += 1
#                 games.append(res[i][8])
#             # else:
#             #     print("False", res[i][7])
#     # print(games)
#     return nb_annees, games


# def participants_pays(noc, games):
#     """Donne le nombre d'athlètes participant à une édition des JO donnée.

#     Parameters
#     ----------
#     noc : str
#         Le NOC du pays dont on veut connaitre le nombre de participants pour
#         une édition des JO donnée.
#     games : str
#         L'édition des JO.
#     """
#     compte = 0
#     participant = []
#     for i in range(1, len(res)):
#         if noc == res[i][7]:
#             # print("Noc OK")
#             if games == res[i][8]:
#                 # print("Games OK")
#                 if res[i][1] not in participant:
#                     compte += 1
#                     participant.append(res[i][1])
#     # print(participant)
#     return compte


def moyenne_participants(noc):
    """Donne la moyenne des participants d'un pays aux JO.

    Parameters
    ----------
    noc : str
        Le NOC du pays dont on veut connaitre la moyenne des participants.

    Returns
    -------
    float
    """

    # Table athlètes liste
    res = []
    with open(
            os.path.join(
                "donnees_jeux_olympiques",
                "donnees_jeux_olympiques",
                "athlete_events.csv"
            )
    ) as fd:
        file = csv.reader(fd)
        for line in file:
            res.append(line)

    # Table NOC liste
    country = []
    with open(
            os.path.join(
                "donnees_jeux_olympiques",
                "donnees_jeux_olympiques",
                "noc_regions.csv"
            )
    ) as fd:
        file = csv.reader(fd)
        for line in file:
            country.append(line)

    def annees_participation(noc):
        """Donne le nombre de participation d'un pays aux JO et la liste des
        jeux en question.

        Parameters
        ----------
        noc : str
            Le NOC du pays dont on veut connaitre le nombre d'années de
            participation.

        Returns
        -------
        int
        list
        """
        nb_annees = 0
        games = []  # Liste des années de participation d'un pays.
        for i in range(1, len(res)):
            if noc == res[i][7]:
                if res[i][8] not in games:
                    nb_annees += 1
                    games.append(res[i][8])
        return nb_annees, games

    def participants_pays(noc, games):
        """Donne le nombre d'athlètes participant à une édition des JO donnée.

        Parameters
        ----------
        noc : str
            Le NOC du pays dont on veut connaitre le nombre de participants
            pour une édition des JO donnée.
        games : str
            L'édition des JO.
        """
        compte = 0
        participant = []
        for i in range(1, len(res)):
            if noc == res[i][7]:
                if games == res[i][8]:
                    if res[i][1] not in participant:
                        compte += 1
                        participant.append(res[i][1])
        # print(participant)
        return compte

    nb_annees, liste_jeux = annees_participation(noc)
    total = 0
    for jeu in liste_jeux:
        compte_participants = participants_pays(noc, jeu)
        # print(f"{jeu}. {compte_participants}")
        total += compte_participants
    moyenne = total / nb_annees

    return f"""\nLe pays correspondant au NOC {noc} a envoyé des délégations
     de {moyenne} athlète(s) en moyenne."""
