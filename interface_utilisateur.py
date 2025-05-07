import warnings
from partie_benjamin import Question_1
from partie_benjamin import Question_2
from partie_benjamin import Question_3
from partie_Eulalie import bornes_medailles
from partie_Eulalie import parite_disc_hommes_femmes
from partie_Eulalie import disciplines_disp
from partie_Eulalie import classement_competiteurs
from partie_apprentissage import Question_apprentissage
from fonctions_Julie import prop_athletes_femmes
from fonctions_Julie import perf_chine
from fonctions_Julie import moyenne_participants

warnings.filterwarnings("ignore")


def questionnaire():
    print("Voici nos différentes questions : \n")
    print("1: Combien de médailles Michael Phelps a-t-il gagnées dans sa carrière ?")
    print(
        "2: Quelles sont les caractéristiques (poids, taille, âge) qui remportent le"
        " plus de médailles ?"
    )
    print("3: Quel est le classement des pays aux JO toutes années confondues ?")
    print(
        "4: Quelles peuvent être une borne inférieure et une borne supérieure du nombre"
        " de médailles gagnées par pays pour les JO 2016?"
    )
    print(
        "5: Le nombre de disciplines accessibles aux hommes et aux femmes est-il"
        " équivalent? Les JO sont-ils devenus équitables ? Si oui, depuis quand ?"
    )
    print("6: Quel est le classement des athlètes toutes années confondues?")
    print(
        "7: Des disciplines pratiquées à des JO précédents ont-elles disparu ? Si oui,"
        " lesquelles ?"
    )
    print(
        "8: Quelle proportion des participants les femmes représentent-elles aux JO"
        " chaque année ?"
    )
    print(
        "9: La Chine a-t-elle eu de meilleures performances durant les JO de Pékin en"
        " 2008 (par rapport à la moyenne de ses performances) ? Est-ce le cas pour les"
        " jeux qui les ont précédés et suivis ?"
    )
    print("10: Combien de médailles les pays ont-ils gagné en moyenne depuis 1896 ?")
    print(
        "11: Quelles disciplines vous correspondent le mieux en se basant sur les"
        " profils d'athlètes similaires ?"
    )

    question = input(
        "\nTapez le numéro de la question dont vous souhaitez avoir la réponse, tapez 0"
        " pour quitter.\n"
    )
    return question


def interface():
    print("\nBienvenue sur notre projet traitement de données ! \n")
    while True:
        question = questionnaire()
        if question == "0":
            print("\nOn espère que notre projet vous a plu !\n")
            return "fin"
        elif question == "1":
            print(
                "\nSi vous souhaitez avoir le nombre de médailles de Michael Phelps,"
                " tapez 1. "
            )
            print(
                "Si vous souhaitez connaître le nombre cumulé de médailles d'un athlète"
                " de votre choix, tapez 2.\n"
            )
            choix = input()
            if choix == "1":
                print(
                    f"Le nombre total de médailles obtenues par Phelps "
                    f"est {Question_1('Michael Fred Phelps, II')}."
                )
            elif choix == "2":
                nom = input(
                    "\nTapez le nom dont vous voulez le nombre de médaille cumulé\n"
                )
                print(
                    f"Le nombre total de médailles obtenues par {nom} est"
                    f" {Question_1(nom)}."
                )
            else:
                print("\nVous n'avez pas tapé un nombre valide\n")
        elif question == "2":
            print(Question_2())
        elif question == "3":
            nombre = int(
                input(
                    "\n Tapez le nombre de pays que vous voulez afficher dans"
                    " le classement.\n"
                )
            )
            print(Question_3(nombre))
            print(
                "\nPour voir l'intégralité du classement, voir le tableau"
                " 'classement_final'."
            )
        elif question == "4":
            print("\nSi vous souhaitez avoir le résultat pour les JO 2016, tapez 1. ")
            print(
                "Si vous souhaitez connaître le résultat pour une année de votre choix,"
                " tapez 2.\n"
            )
            choix = input()
            if choix == "1":
                print(bornes_medailles(2016))
                print(
                    "\nSi vous souhaitez voir le tableau en entier, regardez le tableau"
                    " 'tableau_bornes_sup_et_inf.csv' qui a été téléchargé."
                )
            elif choix == "2":
                annee = int(
                    input(
                        "\nTapez le numéro de l'année dont vous souhaitez avoir"
                        " la réponse.\n"
                    )
                )
                print(bornes_medailles(annee))
                print(
                    "\nSi vous souhaitez voir le tableau en entier, regardez le tableau"
                    " 'tableau_bornes_sup_et_inf.csv' qui a été téléchargé."
                )

            else:
                print("\nVous n'avez pas tapé un nombre valide.\n")
        elif question == "5":
            print(
                "Vous pouvez voir les nombres d'épreuves féminines et totales dans le"
                " tableau ci-dessous, n'oubliez pas de fermer l'onglet du graphique"
                " qui s'affiche."
            )
            print(parite_disc_hommes_femmes())
        elif question == "6":
            nombre = int(
                input(
                    "\nTapez le nombre d'athlètes que vous voulez afficher dans le"
                    " classement.\n"
                )
            )
            tableau = classement_competiteurs(nombre)
            for i in range(len(tableau)):
                print(f"{i}: {tableau[i][0]} avec un score de {tableau[i][1]}. ")
        elif question == "7":
            print(
                "\n360 disciplines pratiquées ont disparu. Voici 10 exemples"
                " aléatoires de disciplines qui ont disparu des JO d'été et d'hiver."
            )
            disciplines_disp()
            print(
                "\nN'hésitez pas à relancer la question pour avoir d'autres"
                " disciplines disparues."
            )
            print(
                "Si vous souhaitez voir l'intégralité des disciplines, allez voir les"
                " tableaux 'anciennes_dis_hiv.csv' et 'anciennes_dis_ete.csv'."
            )
        elif question == "8":
            print(prop_athletes_femmes())
        elif question == "9":
            print(perf_chine())
        elif question == "10":
            print(
                "Entrez le comité national olympique du pays dont vous voulez"
                " connaître la taille moyenne des déléguations."
            )
            NOC = input("\n")
            print(moyenne_participants(NOC))

        elif question == "11":
            print(
                "\nA l'aide d'un algorithme des k plus proches voisins et en utilisant"
                " les caractéristiques physiques (poids,taille,âge,sexe),"
            )
            print(
                "nous déterminons les 3 sports où vos caractéristiques ont le plus de"
                " chance de gagner une médaille."
            )
            choix = input(
                "\nSi vous voulez rentrer vos caractéristiques tapez 1, si vous voulez"
                " un exemple tapez 2.\n"
            )
            if choix == "1":
                poids = int(input("Tapez votre poids (en kg).\n"))
                taille = int(input("Tapez votre taille (en cm).\n"))
                age = int(input("Tapez votre age (en année).\n"))
                sexe = int(
                    input("Tapez 0 si vous êtes une femme, 1 si vous êtes un homme.\n")
                )
                print("\nAttendez quelques instants...\n")
                print(Question_apprentissage(poids, taille, age, sexe))
            elif choix == "2":
                print(
                    "\nNous prendrons l'exemple ici d'un homme de 22 ans, de 175 cm et"
                    " de 65 kg\n"
                )
                print("\nUn petit instant...\n")
                print(Question_apprentissage(65, 175, 22, 1))
            else:
                print("\nLe nombre tapé n'est pas valide.\n")

        else:
            print("\nLe nombre tapé n'est pas valide.\n")

        input("\nAppuyez sur entrer quand vous voulez continuer.")


interface()
