import streamlit as st
import pandas as pd
import joblib

# Charger le modèle
model = joblib.load("model_port.pkl")

# Titre
st.title("IA du Port Intelligent")

st.write("Prédiction du temps d'attente des camions")

# ----- INPUTS UTILISATEUR -----
heure = st.slider("Heure d'arrivée", 0, 23, 8)
nb_camions = st.number_input("Nombre de camions", 1, 200, 20)
nb_conteneurs = st.number_input("Nombre de conteneurs", 1, 100, 10)
meteo = st.selectbox("Météo", ["soleil", "pluie"])
type_marchandise = st.selectbox("Type de marchandise", ["import", "export"])

# ----- BOUTON PREDICTION -----
if st.button("Prédire le temps d'attente"):

    # Encodage EXACT comme dans le notebook
    meteo_soleil = 1 if meteo == "soleil" else 0
    type_import = 1 if type_marchandise == "import" else 0

    # Création DataFrame avec mêmes colonnes que modèle
    input_data = pd.DataFrame({
        "heure_arrivee": [heure],
        "nb_camions": [nb_camions],
        "nb_conteneurs": [nb_conteneurs],
        "meteo_soleil": [meteo_soleil],
        "type_marchandise_import": [type_import]
    })

    # Prédiction
    prediction = model.predict(input_data)[0]

    # Affichage
    st.success(f"Temps d'attente estimé : {int(prediction)} minutes")
