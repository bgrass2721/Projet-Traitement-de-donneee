import pandas as pd


athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)
# Question 1:
# min et max de chaque pays
# ne garde que les athlètes de 2016
athlete_2016 = athlete[athlete["Year"] == 2016]

# suprpime les doubles: quand l'épreuve est par équipe
athletes_medailles = athlete_2016[["Medal", "NOC", "Event"]]
athletes_medailles = athletes_medailles.drop_duplicates()

# compte le nombre de médaille par pays
regroup = (
    athletes_medailles.groupby("NOC")["Medal"].value_counts().groupby("NOC")
    )

# max des médailles remportées
nb_max = max(regroup.sum())

# nombre minimum
nb_min = min(regroup.sum())

# Question 2: Evolution des médailles hommes/femmes au fil des ans ?

# Question 3 en python: athlete ayant le plus de médailles
 
