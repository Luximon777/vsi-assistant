import streamlit as st

st.title("Assistant IA - Comptes rendus VSI")

nom = st.text_input("Nom du participant")
projet = st.text_input("Projet professionnel")
freins = st.text_area("Freins identifiés")

if st.button("Générer le compte rendu"):

    texte = f"""
Compte rendu entretien diagnostic

Participant : {nom}

Projet professionnel :
{projet}

Freins identifiés :
{freins}

Synthèse :
Le participant s'engage dans la prestation VSI afin de renforcer sa
confiance et préparer ses futurs entretiens professionnels.
"""

    st.write(texte)
