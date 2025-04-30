import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Charger les données
df = pd.read_csv("athlete_events.csv")

# Calcul du nombre d'athlètes par sport
athletes_par_sport = df["Sport"].value_counts()

# Filtrer les sports avec plus de 5000 athlètes
sports_filtrés = athletes_par_sport[athletes_par_sport > 5000].index

# Créer un DataFrame avec les sports sélectionnés
df_filtré = df[df["Sport"].isin(sports_filtrés)]

# Garder seulement les colonnes nécessaires
df_clean = df_filtré[["Age", "Height", "Weight", "Sport", "Sex"]]

df_clean.loc[:, "Sex"] = df_filtré["Sex"].map({"F": 0, "M": 1})
# Supprimer les lignes avec des valeurs manquantes
df_clean = df_clean.dropna()

# Supprimer les doublons (même caractéristiques, même sport)
df_clean = df_clean.drop_duplicates()

# Séparation des données en train, validation, et test
X = df_clean[["Height", "Weight", "Age", "Sex"]]
y = df_clean["Sport"]

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.2, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

# Mise à l'échelle des données
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)


# Fonction pour tester si le vrai sport est dans le top 3 des prédictions
def top_3_accuracy(model, X_test, y_test):
    correct_count = 0

    y_test = y_test.reset_index(drop=True)

    # Prédire les probabilités pour chaque athlète dans le test set
    probas = model.predict_proba(X_test)

    # Obtenir les sports (labels)
    sports_labels = model.classes_

    for i in range(len(y_test)):
        # Obtenir les indices des 3 sports les plus probables pour cet athlète
        top_3_indices = np.argsort(probas[i])[::-1][:3]

        # Récupérer les noms des 3 sports les plus probables
        top_3_sports = sports_labels[top_3_indices]

        # Vérifier si le vrai sport est dans le top 3
        if y_test.iloc[i] in top_3_sports:
            correct_count += 1

    # Calculer le pourcentage de succès
    accuracy = correct_count / len(y_test)
    return accuracy


# Tester différentes valeurs de k
def meilleur_k(n):
    best_k = 1
    best_accuracy = 0
    for k in range(1, n):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train_scaled, y_train)

        # Calculer l'accuracy sur l'ensemble de validation avec top 3
        accuracy = top_3_accuracy(knn, X_val_scaled, y_val)

        # Garder le meilleur k
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
    return best_k


best_k = 100
# Entraîner le modèle final avec le meilleur k sur l'ensemble d'entraînement +validation
knn_best = KNeighborsClassifier(n_neighbors=best_k)
knn_best.fit(X_train_scaled, y_train)

# Calculer l'accuracy finale sur l'ensemble de test avec top 3
final_accuracy = top_3_accuracy(knn_best, X_test_scaled, y_test)
# print(f"Accuracy finale sur l'ensemble de test (top 3) : {final_accuracy:.4f}")

nouvel_athlete = np.array([[158, 48, 20, 0]])
nouvel_athlete_scaled = scaler.transform(nouvel_athlete)

# Prédire les probabilités
probas = knn_best.predict_proba(nouvel_athlete_scaled)

# Récupérer les classes (noms des sports)
sports_labels = knn_best.classes_

# Obtenir les indices des 3 sports les plus probables
top_3_indices = np.argsort(probas[0])[::-1][:3]

# Obtenir les noms des 3 sports les plus probables
top_3_sports = sports_labels[top_3_indices]
top_3_probs = probas[0][top_3_indices]

# Afficher les résultats
print("Top 3 sports prédits :")
for sport, prob in zip(top_3_sports, top_3_probs):
    print(f"{sport} : {prob * 100:.2f}%")
