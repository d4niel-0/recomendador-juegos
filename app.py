import streamlit as st  # 1. Importamos Streamlit y lo renombramos como 'st' para escribir menos
import random

# Tu lista de juegos de siempre
juegos = [
    "Elden Ring", "God of War", "Minecraft", "Grand Theft Auto V", "Hollow Knight",
    "Cuphead", "The Witcher 3: Wild Hunt", "Devil May Cry 5", "Red Dead Redemption 2",
    "Cyberpunk 2077", "Sekiro: Shadows Die Twice", "Dark Souls III", "Bloodborne",
    "Lies of P", "Black Myth: Wukong", "Ghost of Tsushima", "Marvel's Spider-Man Remastered",
    "Spider-Man: Miles Morales", "Hades", "Hades II", "Celeste", "Ori and the Blind Forest",
    "Ori and the Will of the Wisps", "Dead Cells", "Blasphemous", "Blasphemous II",
    "Nine Sols", "Terraria", "Stardew Valley", "Subnautica", "No Man's Sky", "Palworld",
    "Valheim", "The Forest", "Sons of the Forest", "Resident Evil 2", "Resident Evil 4",
    "Resident Evil Village", "Silent Hill 2 Remake", "Alan Wake 2", "DOOM Eternal",
    "Titanfall 2", "Helldivers 2", "Monster Hunter: World", "Monster Hunter Wilds",
    "Clair Obscur: Expedition 33", "Baldur's Gate 3", "Persona 5 Royal", "Metaphor: ReFantazio",
    "Final Fantasy VII Remake", "Final Fantasy XVI", "Nier: Automata", "Kingdom Come: Deliverance II",
    "Assassin's Creed IV: Black Flag", "Assassin's Creed Shadows", "Batman: Arkham Knight",
    "Control", "Death Stranding", "Uncharted 4: A Thief's End", "The Last of Us Part I",
    "Dying Light", "A Plague Tale: Requiem"
]

# 2. Configurar la pestaña del navegador
st.set_page_config(page_title="Recomendador", page_icon="🎮")

# 3. Poner elementos visuales en la pantalla (Equivalente a tus prints de bienvenida)
st.title("🎯 ¿A qué jugamos hoy?")
st.write("Deja que la lógica decida por ti.")

# 4. Cambiamos el input() de texto por botones de opción (Radio Buttons)
# Así el usuario no escribe disparates y controlamos la entrada.
st.write("¿Quieres una recomendación?")
st.write("seleciona...")
opcion = st.radio(
    ( "Sí", "Tal vez", "No")
)

# 5. La estructura lógica (Tu IF/ELIF/ELSE de antes)
if opcion in ["Sí", "Tal vez"]:
    # Ponemos un botón web. Si el usuario le hace clic, se ejecuta lo de adentro.
    if st.button("Elegir Juego 🎲"):
        juego_elegido = random.choice(juegos)
        # st.success muestra un cuadro verde bonito en la pantalla
        st.success(f"🔥 Te toca jugar: **{juego_elegido}**")

elif opcion == "No":
    # st.info muestra un cuadro azul de información
    st.info("ve de hay gay.")