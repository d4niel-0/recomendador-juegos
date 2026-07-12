import streamlit as st
import random

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(
    page_title="Recomendador",
    page_icon="🎮",
    layout="centered"
)

# ---------------- LISTA DE JUEGOS ----------------
juegos = [
    "Elden Ring", "God of War", "Minecraft", "Grand Theft Auto V", "Hollow Knight",
    "Cuphead", "The Witcher 3: Wild Hunt", "Devil May Cry 5", "Red Dead Redemption 2",
    "Cyberpunk 2077", "Sekiro: Shadows Die Twice", "Dark Souls III", "Bloodborne",
    "Lies of P", "Black Myth: Wukong", "Ghost of Tsushima",
    "Marvel's Spider-Man Remastered", "Spider-Man: Miles Morales",
    "Hades", "Hades II", "Celeste", "Ori and the Blind Forest",
    "Ori and the Will of the Wisps", "Dead Cells", "Blasphemous",
    "Blasphemous II", "Nine Sols", "Terraria", "Stardew Valley",
    "Subnautica", "No Man's Sky", "Palworld", "Valheim",
    "The Forest", "Sons of the Forest", "Resident Evil 2",
    "Resident Evil 4", "Resident Evil Village", "Silent Hill 2 Remake",
    "Alan Wake 2", "DOOM Eternal", "Titanfall 2", "Helldivers 2",
    "Monster Hunter: World", "Monster Hunter Wilds",
    "Clair Obscur: Expedition 33", "Baldur's Gate 3",
    "Persona 5 Royal", "Metaphor: ReFantazio",
    "Final Fantasy VII Remake", "Final Fantasy XVI",
    "Nier: Automata", "Kingdom Come: Deliverance II",
    "Assassin's Creed IV: Black Flag", "Assassin's Creed Shadows",
    "Batman: Arkham Knight", "Control", "Death Stranding",
    "Uncharted 4: A Thief's End", "The Last of Us Part I",
    "Dying Light", "A Plague Tale: Requiem"
]

# ---------------- CSS ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

html, body, [data-testid="stAppViewContainer"], .main {
    font-family: 'Montserrat', sans-serif !important;
    background: linear-gradient(135deg, #1e1e2f 0%, #111119 100%) !important;
}

h1, h2, h3, p, label {
    color: #f0f0f5 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- INTERFAZ ----------------
st.title("🎯 ¿A qué jugamos hoy?")

st.write("Deja que la lógica decida por ti.")
st.write("### ¿Quieres una recomendación?")

opcion = st.radio(
    "Selecciona una opción:",
    ("Sí", "Tal vez", "No"),
    horizontal=True
)

# ---------------- LÓGICA ----------------
if opcion in ["Sí", "Tal vez"]:

    if st.button("🎲 Elegir Juego"):
        juego_elegido = random.choice(juegos)

        st.success(f"🔥 Hoy te toca jugar **{juego_elegido}**")

elif opcion == "No":
    st.info("Bueno... vuelve cuando quieras 😎")