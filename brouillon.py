import pandas as pd
import os
import csv



# Table athlètes
athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)


# La moyenne des médailles remportées par les athlètes du Royaume-Uni.

# athlete_UK = athlete[athlete["NOC"] == "GBR"]
# # print("Athlètes du Royaume-Uni : ", athlete_UK)
# athlete_UK_ete = athlete_UK[athlete_UK["Season"] == "Summer"]
# medailles_UK_ete = athlete_UK_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()

# print("Médailles du Royaume-Uni : ", medailles_UK_ete)
# print("Moyenne des médailles du Royaume-Uni : ", medailles_UK_ete.mean())


# La moyenne des médailles remportées par les athlètes de la Chine


athlete_chine = athlete[athlete["NOC"] == "CHN"]
# print("Athlètes de la Chine : ", athlete_chine)
athlete_chine_ete = athlete_chine[athlete_chine["Season"] == "Summer"]

test = athlete_chine_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()
test_df = pd.DataFrame(athlete_chine_ete.groupby("Year")["Medal"])

print("test_df", type(test_df))
print(test_df)


# medailles_chine_ete = athlete_chine_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()
# moyenne = medailles_chine_ete.mean()

# print("Médailles de la Chine : ", medailles_chine_ete)
# print("Moyenne des médailles de la Chine : ", moyenne)

# f = lambda nb_medailles : nb_medailles >= moyenne
# medailles_chine_ete["Supérieur à la moyenne ?"] = medailles_chine_ete.apply(f, axis=1)
# print(medailles_chine_ete)


# La moyenne des médailles remportées par les athlètes des US


# athlete_US = athlete[athlete["NOC"] == "USA"]
# # print("Athlètes des Etats-Unis : ", athlete_US)
# athlete_US_ete = athlete_US[athlete_US["Season"] == "Summer"]
# medailles_US_ete = athlete_US_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()

# print("Médailles des Etats-Unis : ", medailles_US_ete)
# print("Moyenne des médailles des Etats-Unis : ", medailles_US_ete.mean())



# Combien de médaillés les pays participants ont-ils compté en moyenne par JO ?

# medailles = []
# for athlete in res:
#     if ("Bronze" in athlete[-1]) or ("Silver" in athlete[-1]) or ("Gold" in athlete[-1]):
#         medailles.append(athlete)

