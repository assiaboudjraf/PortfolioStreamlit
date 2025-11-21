import streamlit as st
import time
from PIL import Image
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Assia Boudjraf | Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# -------------------
# Couleurs et style CSS
# -------------------
PRIMARY_COLOR = "#59B2F4"
BG_COLOR = "#191f36"
SECOND_BG_COLOR = "#262B40"
TEXT_COLOR = "#6497A7"

st.markdown(
    f"""
    <style>
    .main {{background-color: {BG_COLOR}; color: {TEXT_COLOR}; font-family: 'Nunito', sans-serif;}}
    h1,h2,h3,h4 {{color: {PRIMARY_COLOR};}}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: {BG_COLOR};
        border-radius: 2rem;
        padding: 0.5rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        margin-top: 1rem;
    }}
    .stButton>button:hover {{background-color: #40a0e0;}}
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {{
        background-color: {SECOND_BG_COLOR};
        color: {TEXT_COLOR};
        border-radius: 0.5rem;
        padding: 0.7rem;
    }}
    </style>
    """, unsafe_allow_html=True
)

# -------------------
# Sidebar navigation
# -------------------
st.sidebar.title("Navigation")
section = st.sidebar.radio("Aller à :", [
    "Accueil", "À propos", "Expérience", "Éducation", "Projets", "Application", "Contact"
])


# -------------------
# Accueil
# -------------------
if section == "Accueil":
    st.title("Bonjour, je suis Assia Boudjraf 👋")
    st.subheader("Passionnée par l'analyse de données, la modélisation statistique et la gestion de projets.")
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.write("""
        Suivez-moi sur les réseaux sociaux :
        - [Facebook](https://www.facebook.com/univpariscite)
        - [X/Twitter](https://x.com/univ_paris_cite)
        - [Instagram](https://www.instagram.com/univ_paris_cite/)
        - [LinkedIn](https://www.linkedin.com/in/assia-b-364813270/)
        """)
        st.download_button(
            label="Télécharger mon CV",
            data=open("AssiaBoudjraf_CV.pdf", "rb").read(),
            file_name="AssiaBoudjraf_CV.pdf",
            mime="application/pdf"
        )
    with col2:
        img = Image.open("image.jpg")
        st.image(img, width=350)
    
    placeholder = st.empty()
    texts = ["Étudiante en Sciences des données", "International Data Analyst & Associate Segmentation "]
    
    for txt in texts:  
        for i in range(len(txt)+1):
            placeholder.markdown(f"### Et je suis **{txt[:i]}**")
            time.sleep(0.05)
        time.sleep(0.8)
        for i in range(len(txt), -1, -1):
            placeholder.markdown(f"### Et je suis **{txt[:i]}**")
            time.sleep(0.03)

# -------------------
# À propos
# -------------------
elif section == "À propos":
    st.header("À propos de moi")
    st.subheader("Étudiante en sciences des données")
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.write("""
         Étudiante en troisième année de BUT Sciences des Données, j’ai développé une expertise solide en statistiques, en programmation et en analyse de données. Mon intérêt pour l’informatique remonte à mon plus jeune âge : j’ai grandi dans un environnement où les technologies étaient omniprésentes, ce qui m’a naturellement conduite à explorer les langages, les algorithmes et les systèmes dès mes premières années d’apprentissage.

 Aujourd’hui, je poursuis mon formation en alternance chez SAS Institute, où j’occupe le poste d’Associate Segmentation et International Data Analyst. Mon rôle consiste à garantir la qualité de la base de données pour les régions EMEA et AMERICAS, en veillant à la cohérence, à la fiabilité et à la pertinence des informations utilisées par les équipes internationales. Cette mission me permet de mettre en pratique mes compétences en data cleaning, en segmentation et en gestion de bases complexes, tout en évoluant dans un contexte multiculturel stimulant.

Passionnée par les données et leur pouvoir décisionnel, je m’investis dans chaque projet avec rigueur et curiosité. Mon profil allie technicité, sens de l’analyse et capacité à collaborer dans des environnements internationaux. Je suis toujours en quête de nouveaux défis qui me permettront de grandir, d’apprendre et de contribuer à des projets à fort impact.
        """)

    with col2:
        img = Image.open("sas.png")
        st.image(img, width=400)


# -------------------
# Expérience
# -------------------
elif section == "Expérience":
    st.header("Expérience professionnelle")
    st.subheader("SAS Institute - Associate Segmentation and Data Analyst (Depuis septembre 2024)")
    st.write("""
    - Responsable de la qualité de la base de données pour les régions EMEA et AMERICAS
    - Gestion des doublons et amélioration des informations
    - Maintien et intégration des données dans le CRM
    - Pilotage de projets selon les besoins de l’équipe
    - Développement de compétences sur Enterprise Guide
    - Data visualisation via Visual Analytics
    - Support aux équipes vente et marketing
    - Collaboration avec différents pays pour l’amélioration de la base de données
    """)

# -------------------
# Éducation
# -------------------
elif section == "Éducation":
    st.header("Éducation")
    st.subheader("IUT Paris Rives de Seine - BUTSD3 VCOD FA")
    st.write("Spécialisation en Visualisation et Conception d'Outils Décisionnels")
    st.image("upc.jpg", width=400)
    
    st.subheader("Lycée Maurice Utrillo - Baccalauréat Général (Mention Bien)")
    st.write("""
    - Spécialité NSI (Numérique et Sciences Informatiques)
    - Spécialité LLCER (Langues, Littératures et Cultures Étrangères)
    - Mention Bien
    """)

# -------------------
# Projets
# -------------------
elif section == "Projets":
    st.header("Projets universitaires")
    
    projects = [
    (
        "Enquête sur l’IA",
        "Projet en groupe visant à réaliser un sondage auprès des étudiants et du personnel universitaire afin d’évaluer l’utilisation et la perception de l’intelligence artificielle dans le cadre scolaire. L’objectif était de recueillir des données qualitatives et quantitatives sur l’intégration de l’IA dans les méthodes d’enseignement et d’apprentissage, aussi bien du point de vue des enseignants que des élèves. Ce travail a inclus la conception, la diffusion et l’analyse d’un questionnaire spécifique.",
        "ia.jpg"
    ),
    (
        "Concours Dataviz",
        "Participation collective à un concours de datavisualisation où nous avons conçu et développé plusieurs tableaux de bord interactifs à l’aide de PowerBI. Ce projet nous a permis de travailler sur la présentation visuelle de données complexes, afin de faciliter leur interprétation et de répondre à des problématiques concrètes via des outils graphiques performants.",
        "courbe.jpg"
    ),
    (
        "Structuration données film",
        "Projet en groupe consistant à traiter et restructurer des données issues de fichiers CSV portant sur des informations relatives à des films. En utilisant Python, nous avons automatisé la transformation et le nettoyage des données pour les rendre exploitables dans des analyses ultérieures, améliorant ainsi la qualité et la cohérence des datasets.",
        "cinema.jpg"
    ),
    (
        "Implémentation commerce",
        "Travail collaboratif visant à aider un commerce à déterminer le meilleur emplacement pour son installation. Nous avons extrait des données à partir d’une base SQL puis réalisé une analyse approfondie sur Excel en croisant différentes variables économiques et géographiques, dans le but de proposer des recommandations basées sur des données concrètes.",
        "commerce.jpg"
    ),
    (
        "Digitalisation commerces parisiens",
        "Projet de groupe orienté vers la digitalisation des commerces parisiens, impliquant l’ajout et la mise à jour de données dans la base BCOM2023 via des scripts Python. Ce travail a permis d’enrichir et de structurer une base de données essentielle pour des analyses urbaines et commerciales, contribuant ainsi à la modernisation des outils de suivi des commerces.",
        "logo_apur.jpg"
    ),
    (
        "Efficacité sonde médicale",
        "Projet collectif portant sur le nettoyage, le traitement et l’analyse de données issues de sondes médicales, réalisé sous RStudio. Le but était d’évaluer l’efficacité des dispositifs à partir de données brutes, en produisant un rapport détaillé incluant des visualisations et recommandations pour améliorer l’usage clinique de ces sondes.",
        "medical.jpg"
    )
]

    
    for title, desc, img_path in projects:
        st.subheader(title)
        st.write(desc)
        st.image(img_path, width=400)

# -------------------
# Contact
# -------------------

elif section == "Contact":
    st.header("Contactez-moi")

    with st.form("contact_form"):
        name = st.text_input("Nom complet")
        email = st.text_input("Adresse mail")
        phone = st.text_input("Numéro de téléphone")
        subject = st.text_input("Sujet")
        message = st.text_area("Votre message")
        submit = st.form_submit_button("Envoyer le message")

        if submit:
            if not name or not email or not message:
                st.error("Veuillez remplir au minimum votre nom, email et message.")
            else:
                formspree_url = "https://formspree.io/f/mldzqwjn" 
                data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "subject": subject,
                    "message": message
                }

                try:
                    response = requests.post(formspree_url, json=data) 
                    if response.status_code == 200:
                        st.success(" Merci ! Votre message a bien été envoyé.")
                    else:
                        st.error(f"Erreur lors de l'envoi ({response.status_code}) : {response.text}")
                except Exception as e:
                    st.error(f"Une erreur est survenue : {e}")

# -------------------
# Application
# -------------------
elif section == "Application":
    st.header("Application : Analyse des défibrillateurs RATP")

    # --- Chargement des données ---
    df = pd.read_csv("Z:/BUT3/Data Viz/Portfolio/defibrillateurs-du-reseau-ratp.csv", sep=";")

    # --- Préparation des données ---
    df.rename(columns={
        "lat_coor1": "Latitude",
        "long_coor1": "Longitude",
        "Localisation": "Station",
        "Code postal": "CodePostal",
        "Ville": "Ville",
        "Accès": "Acces",
        "Accès Libre": "AccesLibre",
        "Complément de localisation": "Complement",
        "Disponibilité Semaine": "DisponibiliteSemaine",
        "Disponibilité Horaires": "DisponibiliteHoraires"
    }, inplace=True)

    # Nettoyage des valeurs
    df["Acces"] = df["Acces"].str.strip()
    df["Ville"] = df["Ville"].str.strip()

    # Séparation Paris vs autres villes
    df_paris = df[df["Ville"].str.upper() == "PARIS"]
    df_autres = df[df["Ville"].str.upper() != "PARIS"]

    # --- Widgets d’interaction ---
    villes = sorted(df["Ville"].unique())
    ville_choice = st.multiselect("Choisir une ou plusieurs villes :", options=villes, default=["PARIS"])
    acces_choice = st.multiselect("Type d'accès :", options=df["Acces"].unique(), default=df["Acces"].unique())

    # Filtrage
    df_filtered = df[df["Ville"].isin(ville_choice) & df["Acces"].isin(acces_choice)]

    # --- Affichage tableau ---
    st.subheader("Données filtrées")
    st.dataframe(df_filtered)

    # --- Carte interactive ---
    st.subheader("Carte des défibrillateurs filtrés")
    fig_map = px.scatter_mapbox(
        df_filtered,
        lat="Latitude",
        lon="Longitude",
        hover_name="Station",
        hover_data=["Ville", "Acces", "AccesLibre", "Complement"],
        color="Acces",
        zoom=9,
        height=500
    )
    fig_map.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig_map, use_container_width=True)

    # --- Graphique : uniquement banlieue ---
    st.subheader("Répartition des défibrillateurs hors Paris")
    fig_autres = px.bar(
        df_autres.groupby(["Ville", "Acces"]).size().reset_index(name="Nombre"),
        x="Ville",
        y="Nombre",
        color="Acces",
        barmode="group",
        title="Défibrillateurs hors Paris (Intérieur vs Extérieur)"
    )
    st.plotly_chart(fig_autres, use_container_width=True)

    # --- KPI ---
    st.subheader("Indicateurs clés")
    st.metric("Nombre total de défibrillateurs", len(df))
    st.metric("Nombre filtré", len(df_filtered))
    st.metric("Nombre à Paris (Intérieur)", len(df_paris))   
    st.metric("Nombre hors Paris", len(df_autres))