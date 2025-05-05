import pandas as pd
import csv
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Table athlètes
athlete = pd.read_csv(
    "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
)

# La moyenne des médailles remportées par les athlètes de la Chine


athlete_chine = athlete[athlete["NOC"] == "CHN"]
# print("Athlètes de la Chine : ", athlete_chine)
athlete_chine_ete = athlete_chine[athlete_chine["Season"] == "Summer"]

# test = athlete_chine_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()
# test_df = pd.DataFrame(athlete_chine_ete.groupby("Year")["Medal"])

# print("test_df", type(test_df))
# print(test_df)


medailles_chine_ete = athlete_chine_ete.groupby("Year")["Medal"].value_counts().groupby("Year").sum()
moyenne = medailles_chine_ete.mean()


medailles_chine_ete = medailles_chine_ete.reset_index(name='Medals')


print("Médailles de la Chine : ", medailles_chine_ete)
print("Moyenne des médailles de la Chine : ", moyenne)


# f = lambda nb_medailles : nb_medailles >= moyenne
# medailles_chine_ete["Supérieur à la moyenne ?"] = medailles_chine_ete["Medals"].apply(f, axis=1)
# print(medailles_chine_ete)

plt.bar(medailles_chine_ete["Year"], medailles_chine_ete["Medals"])
plt.axhline(y=moyenne, xmin=0, xmax=2018, color="red")
plt.text(1983, 105, 'Moyenne des médailles de la Chine', color="red")
plt.text(2005, 170, "JO de Pékin", color="black")
plt.xlabel("Année")
plt.ylabel("Médailles de la Chine")
plt.title("Nombre de médailles obtenues par la Chine aux JO")
plt.show()

# # graphique côte à côte des disciplines été et hiver
# fig, axes = plt.subplots(1, 2, figsize=(14, 6))
# fig.tight_layout(pad=5.0)  # espacement entre les sous-graphiques

# # Graphique pour l'été
# sns.barplot(data=athlete_chine_ete, x=athlete_chine_ete["Year"], y=athlete_chine_ete["Medals"], color="blue", ax=axes[0])
# axes[0].set_title("Performance de la Chine aux JO aux alentours des JO de Pékin")
# axes[0].set_ylabel("Nombre de médailles")
# axes[0].tick_params(axis='x', rotation=45)


# # Sauvegarde des graphiques dans des fichiers
# plt.savefig("perf_Chine_Pekin.png")
# plt.show()

