import streamlit as st
import json
import pandas as pd
import requests
from streamlit_lottie import st_lottie
st.write("""
# Application Gestion RH Aveni-Re
 *Cette Application a pour but d'automatiser et de fluidifier les interactions entre le Personnel et la Direction des Ressources Humaines.*
""")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = load_lottiefile("C:\\Users\\beugre\\Desktop\\hello.json")
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
    st.write("Visiter notre site web :","https://www.aveni-re.com/")

# Set up utilisateurs
utilisateurs = {
    "12345": {"nom": "Mme Awa AW", "password": "Awa"},
    "23456": {"nom": "M Charlemagne NGUESSAN", "password": "Charli"},
    "34567": {"nom": "Mlle Melissa KANGAH", "password": "Melissa"},
    "45678": {"nom": "Mr Yann BEUGRE", "password": "sln"},
    "56789": {"nom": "Mr AW Seybatou", "password": "PDG"}}
 

st.sidebar.title("Mon Espace RH")
# Ajouter un widget dans la sidebar
utilisateur = st.sidebar.selectbox("Je suis ...", ["RH", "Employé", "Futur Employé"])
# Si l'utilisateur est un employé
if utilisateur == "Employé":
    matricule = st.sidebar.text_input("Entrez votre matricule")
    password = st.sidebar.text_input("Entrez votre Password", type="password")
    valider1 = st.sidebar.button("Valider")
    if valider1:
        if matricule in utilisateurs:
            if utilisateurs[matricule]["password"] == password:
                st.sidebar.success(f"Bienvenue {utilisateurs[matricule]['nom']}")
                js = f"window.open('http://localhost:8501/?matricule={matricule}')"
                st.components.v1.html(f"<script>{js}</script>", height=0)
            else:
                st.sidebar.error("Mot de passe incorrect")
        else:
            st.sidebar.error("Matricule inconnu")


elif utilisateur == "RH":
    nom_RH = st.sidebar.text_input("Entrez votre Nom")
    code_RH = st.sidebar.text_input("Entrez votre Code RH")
    valider2 = st.sidebar.button("Valider")
    

elif utilisateur == "Futur Employé":
    nom_candidat = st.sidebar.text_input("Entrez votre Nom")
    prenom_candidat = st.sidebar.text_input("Entrez votre Prénom")
    niveau_candidat = st.sidebar.selectbox("Quel est votre niveau d'étude ?", ["Bac", "Licence", "Master", "Doctorat"])
    email_candidat = st.sidebar.text_input("Entrer votre adresse E-mail")
    valider3 = st.sidebar.button("Valider")
    if valider3 :
        st.sidebar.success("Bien recu, A bientot !!")

if valider1:
    if matricule in utilisateurs:
        if utilisateurs[matricule]["password"] == password:
            st.sidebar.success(f"Bienvenue {utilisateurs[matricule]['nom']}")

            # Redirection vers une autre application locale (par exemple sur le port 8504)
            js = "window.open('http://localhost:8501')"  # adapte le port à ton app cible
            st.components.v1.html(f"<script>{js}</script>", height=0)

        else:
            st.sidebar.error("Mot de passe incorrect")
    else:
        st.sidebar.error("Matricule inconnu")
