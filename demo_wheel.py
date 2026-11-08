from logiai.predict import Predictor

predictor = Predictor()

livraison = {
    "distance_km": 120,
    "poids_kg": 450,
    "heure_depart": 17,
    "pluie_mm": 8,
    "trafic_index": 7.5,
    "nb_arrets": 4,
    "type_vehicule": "camion"
}

resultat = predictor.predict(livraison)

print("Résultat de la prédiction :")
print(resultat)