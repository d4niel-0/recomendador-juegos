import streamlit as st
import random

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(
    page_title="¿Que Veremos Hoy?",
    page_icon="🍿",
    layout="centered"
)

# ---------------- LISTA DE JUEGOS ----------------
peliculas = [
    "Tenet",
    "Soul",
    "The Invisible Man",
    "Extraction",
    "The Trial of the Chicago 7",
    "Palm Springs",
    "The Father",
    "Sound of Metal",
    "Another Round",
    "Enola Holmes",

    "Dune",
    "Spider-Man: No Way Home",
    "No Time to Die",
    "Shang-Chi and the Legend of the Ten Rings",
    "The Suicide Squad",
    "Free Guy",
    "Cruella",
    "Encanto",
    "The French Dispatch",
    "Don't Look Up",

    "The Batman",
    "Top Gun: Maverick",
    "Avatar: The Way of Water",
    "Everything Everywhere All at Once",
    "The Northman",
    "The Black Phone",
    "Bullet Train",
    "Glass Onion: A Knives Out Mystery",
    "The Whale",
    "Puss in Boots: The Last Wish",

    "John Wick: Chapter 4",
    "Oppenheimer",
    "Barbie",
    "Guardians of the Galaxy Vol. 3",
    "Spider-Man: Across the Spider-Verse",
    "The Super Mario Bros. Movie",
    "Mission: Impossible: Dead Reckoning",
    "The Creator",
    "Napoleon",
    "Wonka",

    "Dune: Part Two",
    "Inside Out 2",
    "Deadpool & Wolverine",
    "Kingdom of the Planet of the Apes",
    "Godzilla x Kong: The New Empire",
    "Civil War",
    "Alien: Romulus",
    "Furiosa: A Mad Max Saga",
    "The Fall Guy",
    "Kung Fu Panda 4",

    "A Minecraft Movie",
    "How to Train Your Dragon",
    "Lilo & Stitch",
    "Mission: Impossible: The Final Reckoning",
    "Superman",
    "Jurassic World Rebirth",
    "The Fantastic Four: First Steps",
    "Thunderbolts*",
    "Captain America: Brave New World",
    "Sinners",

    "Avatar: Fire and Ash",
    "The Odyssey",
    "Project Hail Mary",
    "Toy Story 5",
    "The Devil Wears Prada 2",
    "Scream 7",
    "Michael",
    "Mortal Kombat II",
    "The Mandalorian & Grogu",
    "Hoppers",

    "The Killer",
    "Leave the World Behind",
    "Poor Things",
    "Killers of the Flower Moon",
    "The Menu",
    "The Banshees of Inisherin",
    "The Gray Man",
    "Prey",
    "The Woman King",
    "Elvis",

    "Turning Red",
    "Lightyear",
    "Doctor Strange in the Multiverse of Madness",
    "Black Panther: Wakanda Forever",
    "Thor: Love and Thunder",
    "Sonic the Hedgehog 2",
    "Sonic the Hedgehog 3",
    "Smile",
    "Smile 2",
    "M3GAN",

    "Five Nights at Freddy's",
    "The Hunger Games: The Ballad of Songbirds & Snakes",
    "Transformers: Rise of the Beasts",
    "Creed III",
    "The Flash",
    "Blue Beetle",
    "Elemental",
    "Wish",
    "IF",
    "Nosferatu"
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
st.title("🎯 ¿Que Veremos Hoy?")

st.write("Deja que la lógica decida por ti.")
st.write("### ¿Quieres una recomendación?")

opcion = st.radio(
    "Selecciona una opción:",
    ("Sí", "Tal vez", "No"),
    horizontal=True
)

# ---------------- LÓGICA ----------------
if opcion in ["Sí", "Tal vez"]:

    if st.button("🎲 Elegir Pelicula"):
        pelicula_elegida = random.choice(peliculas)

        st.success(f"🔥 Hoy te toca ver **{pelicula_elegida}**")

elif opcion == "No":
    st.info("Bueno... vuelve cuando quieras 😎")