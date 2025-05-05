import pandas as pd
import os
import csv


# Table athlètes df
athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)

# Table noc df
country_df = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/noc_regions.csv"
)



def prop_athletes_femmes():
    # Argument vide ou mettre la table comme argument ?
    athlete_femme = athlete[athlete["Sex"] == "F"]
    nb_femme_an = athlete_femme.groupby("Year")["Name"].value_counts().groupby("Year").sum()
    nb_athlete_an = athlete.groupby("Year")["Name"].value_counts().groupby("Year").sum()
    proportion_femme_an = nb_femme_an.div(nb_athlete_an)
    return proportion

