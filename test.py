import streamlit as st
import json
import pandas as pd
import requests
from streamlit_lottie import st_lottie

# === TITRE DE L'APPLICATION ===
st.write("""
# Application Gestion RH Aveni-Re
*Cette Application a pour but d'automatiser et de fluidifier les interactions entre le Personnel et la Direction des Ressources Humaines.*
""")

# === CHARGEMENT DE LOTTIE ===
def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Utiliser un fichier local OU une URL externe
lottie_coding = load_lottiefile("hello.json")  # Assure-toi que ce fichier est dans le même dossier que test.py

# Fallback si le fichier local ne marche pas
if not lottie_coding:
    lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_4kx2q32n.json")

st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="high",
    height=None,
    width=None,
    key=None,
)

with st.expander("See more !"):
    st.write("Consulter notre charte interne :")
    st.write("Visiter notre site web :", "https://www.aveni-re.com/")

# === BASE DES UTILISATEURS ===
utilisateurs = {
    "12345": {"nom": "Mme Awa AW", "password": "Awa"},
    "23456": {"nom": "M Charlemagne NGUESSAN", "password": "Charli"},
    "34567": {"nom": "Mlle Melissa KANGAH", "password": "Melissa"},
    "45678": {"nom": "Mr Yann BEUGRE", "password": "sln"},
    "56789": {"nom": "Mr AW Seybatou", "password": "PDG"},
}

# === INTERFACE SIDEBAR ===
st.sidebar.title("Mon Espace RH")
utilisateur = st.sidebar.selectbox("Je suis ...", ["RH", "Employé", "Futur Employé"])

# === EMPLOYE ===
if utilisateur == "Employé":
    matricule = st.sidebar.text_input("Entrez votre matricule")
    password = st.sidebar.text_input("Entrez votre Password", type="password")
    valider1 = st.sidebar.button("Valider")

    if valider1:
        if matricule in utilisateurs:
            if utilisateurs[matricule]["password"] == password:
                st.sidebar.success(f"Bienvenue {utilisateurs[matricule]['nom']}")

                # Ouverture d'un nouvel onglet (à adapter en déploiement local)
                js = f"window.open('http://localhost:8501/?matricule={matricule}')"
                st.components.v1.html(f"<script>{js}</script>", height=0)
            else:
                st.sidebar.error("Mot de passe incorrect")
        else:
            st.sidebar.error("Matricule inconnu")

# === RH ===
elif utilisateur == "RH":
    nom_RH = st.sidebar.text_input("Entrez votre Nom")
    code_RH = st.sidebar.text_input("Entrez votre Code RH")
    valider2 = st.sidebar.button("Valider")

# === FUTUR EMPLOYE ===
elif utilisateur == "Futur Employé":
    nom_candidat = st.sidebar.text_input("Entrez votre Nom")
    prenom_candidat = st.sidebar.text_input("Entrez votre Prénom")
    niveau_candidat = st.sidebar.selectbox("Quel est votre niveau d'étude ?", ["Bac", "Licence", "Master", "Doctorat"])
    email_candidat = st.sidebar.text_input("Entrer votre adresse E-mail")
    valider3 = st.sidebar.button("Valider")

    if valider3:
        st.sidebar.success("Bien reçu, à bientôt !")
