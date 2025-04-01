import pandas as pd


athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)
# question 1
# min et max de chaque pays
athlete_2016 = athlete[athlete["Year"] == 2016]


athletes_medailles = athlete_2016[athlete_2016["Medal"].isin([
    "Bronze", "Gold", "Silver"])]

regroup = (
    athletes_medailles.groupby("NOC")["Medal"].value_counts().groupby("NOC")
    )

nb_max = max(regroup.sum())


# nombre minimum
sans_medaille = athlete_2016[not(athlete_2016["Medal"].isin([
    "Bronze", "Gold", "Silver"]))]
