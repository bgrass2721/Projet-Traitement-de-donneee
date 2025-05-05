import pandas as pd
import csv
import os
import matplotlib.pyplot as plt
import seaborn as sns


# Table athlètes df
athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)

# Table noc df
country_df = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/noc_regions.csv"
)

#######################################################################################

def prop_athletes_femmes():
    # Argument vide ou mettre la table comme argument ?
    athlete_femme = athlete[athlete["Sex"] == "F"]
    nb_femme_an = athlete_femme.groupby("Year")["Name"].value_counts().groupby("Year").sum()
    nb_athlete_an = athlete.groupby("Year")["Name"].value_counts().groupby("Year").sum()
    proportion_femme_an = nb_femme_an.div(nb_athlete_an)
    return proportion_femme_an

#######################################################################################

# La moyenne des médailles remportées par les athlètes de la Chine

def perf_chine():

    athlete_chine = athlete[athlete["NOC"] == "CHN"]
    athlete_chine_ete = athlete_chine[athlete_chine["Season"] == "Summer"]

    medailles_chine_ete = athlete_chine_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()
    moyenne = medailles_chine_ete.mean()

    medailles_chine_ete = medailles_chine_ete.reset_index(name='Medals')

    print("Médailles de la Chine : ", medailles_chine_ete)
    print("Moyenne des médailles de la Chine : ", moyenne)

    plt.bar(medailles_chine_ete["Year"], medailles_chine_ete["Medals"])
    plt.axhline(y=moyenne, xmin=0, xmax=2018, color="red")
    plt.text(1983, 105, "Moyenne", color="red")
    plt.text(2005, 170, "JO de Pékin", color="black")
    plt.xlabel("Année")
    plt.ylabel("Médailles de la Chine")
    plt.show()

#######################################################################################


