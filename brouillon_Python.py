import pandas as pd
import csv
import os
import matplotlib.pyplot as plt
import seaborn as sns


# Table athlètes df
athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)


def perf_chine():

    athlete_chine = athlete[athlete["NOC"] == "CHN"]
    athlete_chine_ete = athlete_chine[athlete_chine["Season"] == "Summer"]

    medailles_chine_ete = athlete_chine_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()
    moyenne = medailles_chine_ete.mean()

    medailles_chine_ete = medailles_chine_ete.reset_index(name='Medals')

    print("Médailles de la Chine : ", type(medailles_chine_ete))
    print("Moyenne des médailles de la Chine : ", type(moyenne))

    plt.bar(medailles_chine_ete["Year"], medailles_chine_ete["Medals"], width=3)
    plt.axhline(y=moyenne, xmin=0, xmax=2018, color="red")
    plt.text(1983, 105, "Moyenne", color="red")
    plt.text(2007.375, 10, "JO de Pékin", color="white", weight="bold", rotation=90, size=18)
    plt.xticks(medailles_chine_ete["Year"])
    plt.xlabel("Année")
    plt.ylabel("Médailles de la Chine")
    plt.show()


perf_chine()