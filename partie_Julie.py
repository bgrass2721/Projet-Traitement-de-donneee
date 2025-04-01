import pandas as pd

athlete = pd.read.csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)

# Le nombre de femmes parmi les participants par année.

athlete_femme = athlete[athlete["Sex"] == "F"]
nb_femme_an = athlete_femme.groupby("Year")["Sex"].value_counts().groupby("Year").sum()

print(nb_femme_an)