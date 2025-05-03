import pandas as pd
import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import warnings
from partie_benjamin import Question_1
from partie_benjamin import Question_2
from partie_benjamin import Question_3
from partie_Eulalie import bornes_medailles
from partie_Eulalie import parite_disc_hommes_femmes
from partie_Eulalie import disciplines_disp
from partie_Eulalie import classement_competiteurs

warnings.filterwarnings("ignore")

def questionnaire():
    print("Voici nos différentes questions : \n")
    print("1: Combien de médailles Michael Phelps a-t-il gagné dans sa carrière?")
    print("2: Quelles sont les caractéristiques (poids, taille, âge) qui remportent le plus de médailles?")
    print("3: Quel est le classement des pays aux JO toutes années confondues?")
    print("4: Quelle peuvent être une borne inférieure et une borne supérieure du nombre de médailles gagnées par pays pour les JO 2016?")
    print("5: Le nombre de disciplines accessibles aux hommes et aux femmes est-il équivalent? Les JO sont-ils devenus équitables? Si oui, depuis quand?")
    print("6: Quel est le classement des athlètes toutes années confondues?")
    print("7: Des disciplines pratiquées à des JO précédents ont-elles disparu? Si oui, lesquelles?")
    print("8: Quelle proportion des participants les femmes représentent-elles aux JO chaque année?")
    print("9: La Chine a-t-elle eu de meilleures performances durant les JO de Pékin en 2008 (par rapport à la moyenne de ses performances)? Est-ce le cas pour les jeux qui les ont précédés et suivis?")
    print("10: Combien de médailles les pays ont-ils gagné en moyenne depuis 1896?")

    question = input("Tapez le numéro de la question dont vous souhaitez en apprendre plus, tapez 0 pour quitter")
    return question
def interface():
    print("Bienvenue sur notre projet traitement de donnée \n")
    for i in range(10):
        question = questionnaire()
        if question == "0":
            print("J'espère que notre projet vous a plu !")
            return "fin"
        elif question == "1":
            print("\nSi vous souhaitez avoir le nombre de médaille de Phelps, tapez 1 ")
            print("Si vous souhaitez connaître le nombre de médaille cumulé d'un nom de votre choix, tapez 2")
            choix = input()
            if choix == "1":
                print(f"Le nombre total de médailles obtenues par Phelps est {Question_1('Michael Fred Phelps, II')}") 
            elif choix == "2":
                nom = input("Tapez le nom dont vous voulez le nombre de médaille cumulé")
                print(f"Le nombre total de médailles obtenues par {nom} est {Question_1(nom)}") 
            else:
                print("Vous n'avez pas tapé un nombre valide")
        elif question == "2":
            print(Question_2())
        elif question == "3":
            nombre = int(input("\n Tapez le nombre de pays que vous voulez afficher dans le classement"))
            print(Question_3(nombre))
            print("\nPour voir l'intégralité du classement, voir le tableau 'classement_final")
        elif question =="4":
            print("\nSi vous souhaitez avoir le résultat pour les JO 2016, tapez 1 ")
            print("Si vous souhaitez connaître le résultat pour une année de votre choix, tapez 2")
            choix = input()
            if choix == "1":
                print(bornes_medailles(2016))
                print("\nSi vous souhaitez voir le tableau en entier, regardez le tableau 'tableau_bornes_sup_et_inf.csv' qui a été téléchargé")
            elif choix == "2":
                annee = int(input("Tapez le numéro de l'année dont vous souhaitez avoir la réponse"))
                print(bornes_medailles(annee)) 
                print("\nSi vous souhaitez voir le tableau en entier, regardez le tableau 'tableau_bornes_sup_et_inf.csv' qui a été téléchargé")

            else:
                print("Vous n'avez pas tapé un nombre valide")
        elif question == "5":
            print(parite_disc_hommes_femmes())
        elif question == "6":
            print("\nVoici 10 exemples aléatoires de disciplines qui ont disparues")
            print(disciplines_disp())
            print("\nN'hésitez pas à relancer la question pour avoir d'autres disciplines disparues")
            print("Si vous souhaitez voir l'intégralité des disciplines, allez voir les tableaux 'anciennes_dis_hiv.csv' et 'anciennes_dis_ete.csv'")
        elif question == "7":
            nombre = int(input("\nTapez le nombre d'athlètes que vous voulez afficher dans le classement\n"))
            tableau = (classement_competiteurs(nombre))
            for i in range(len(tableau)):
                print(f"{tableau[i][0]} avec {tableau[i][1]} médailles")




        input("\nAppuyez sur entrer quand vous voulez continuer")



interface()