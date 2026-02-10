import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(
    page_title="PORTFOLIO - El hadj kader DIOP",
    page_icon="👨‍💼",
    layout="wide"
)

# CSS personnalisé pour améliorer le design
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    h1 {
        color: #1f77b4;
    }
    h2 {
        color: #2c3e50;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 10px;
    }
    h3 {
        color: #34495e;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# ===== SIDEBAR - ÉTAPE 1 =====
with st.sidebar:
    st.title("📋 Informations Personnelles")  
    # Informations de contact
    st.markdown("---")
    st.markdown("### 👤 Contact")
    
    st.markdown("*Prénom:*")
    st.write("El hadj kader")
    
    st.markdown("*Nom:*")
    st.write("DIOP")
    
    st.markdown("*Téléphone:*")
    st.write("📱 773597347")
    
    st.markdown("*Email:*")
    st.write("📧 kader_diop123@gmail.com")
    
    # Éducation
    st.markdown("---")
    st.markdown("### 🎓 Éducation")
    
    st.markdown("*Diplômes:*")
    st.write("🎓 *Bac* - 2025")
    st.write("📚 *BTS(Brevet de Technicien Superieur) en Géomatique*")

# ===== CONTENU PRINCIPAL - ÉTAPE 2 =====

# En-tête
st.title("👨‍💼 PORTFOLIO")

st.markdown("Géomaticien - Spécialiste SIG")
st.markdown("---")

# Profil Professionnel
st.header("🎯 Profil Professionnel")
st.markdown("""
Jeune professionnel diplômé en géomatique avec une solide formation en systèmes d'information 
géographique (SIG), cartographie et analyse spatiale. Passionné par les technologies géospatiales 
et motivé à contribuer à des projets innovants dans le domaine de l'aménagement du territoire 
et de la gestion des ressources.
""")

st.markdown("---")

# Projets Académiques
st.subheader("📚 Projet Académique:Étude Pédologique (les types de sols) de la région de Tambacounda avec ARCGIS")

st.markdown("""
    - *Description:**
    Réalisation d'une carte thématique du region de tambacounda afin de mieux comprendre leur repartition et permettre d'identifier les types de sols présents dans la région de Tambacounda
    """)

st.markdown("---")

# Expérience
st.header("💼 Expérience Professionnelle")

st.markdown("🔹 Création de cartes avec les outils SIG(Systeme d'Information Géographique) ")
st.markdown("🔹Numerisation de données géographiques") 
st.markdown("🔹Géoréférencement d'images et de cartes") 


st.markdown("🔹Maitrise de suites Office Microsoft 365 (Excel, Power Point, World) ")
st.markdown("🔹Maitrise de suites Bureautiques workspace ( Google,Meet,Docs)")


# Compétences
st.header("🛠️ Compétences")



st.markdown("💻Maitrise Logiciels SIG")
st.markdown("""
    -  QGIS
    -  ARCGIS
    """)

st.markdown("""
    - Maitrise des MNT(Modéle Numerique de Terrain)
    - GPS
    - Station totale
    - Mobile topographer
    """)
st.markdown("""
    - Base  en python (streamlit)
    - Developpeur SIG(Systeme d'Information Geographique)
""")
st.markdown("---")
# Articles / Publications
st.header("📝 Articles & Publications")
st.markdown("---")

