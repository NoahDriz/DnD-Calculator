from unittest import case

import streamlit as st
import math
import base64

def set_background(image_file):
    with open(image_file, "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{img_data}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("Assets/DnDCalcBackground.png")

st.title("DnD Damage Calculator")
enemies = []
EnemyAmount = st.number_input("How many enemies are there?", min_value=1, step=1, format="%d", key = "enemyamount")
for i in range(EnemyAmount):
    Hp = st.text_input(f"How many Hitpoints does character {i+1} have?", key = f"hp_{i}")
    #Caculating Damage based on the following:
    Type = st.text_input("Resistance, Vulnerability, Immunity, or Straight? ", key = f"type_{i}")
    match Type:
        case "Straight":
            import math
            D = st.number_input("How much Damage?", min_value=0, format="%d", key = f"damage_{i}")
            TD =(D) 
        case "Resistance":
            import math
            #D = Damage
            D = st.number_input("How much Damage?", min_value=0, format="%d", key = f"damage_{i}")
            #TD = Total Damage
            TD = math.floor((D)/2)
        case "Vulnerability":
            import math
            #D = Damage
            D = st.number_input("How much Damage?", min_value=0, format="%d", key = f"damage_{i}")
            #TD = Total Damage
            TD = math.floor((D)*2)
        case "Immunity":
            D = 0
            TD = 0
            st.write("No Damage!")
        case _:
            D = 0
            TD = 0
            st.write("Please enter one of the following above.")
    enemies.append({"hp": Hp, "type": Type, "damage": D, "total_damage": TD})
if st.button("Calculate All"):
    for i, enemy in enumerate(enemies):
        RemainingHp = int(enemy["hp"]) - int(enemy["total_damage"])
        st.write(f"Enemy {i+1}: Remaining Hitpoints: {RemainingHp:,}")
def reset_form():
    for j in range(EnemyAmount):
            st.session_state[f"hp_{j}"] = ""
            st.session_state[f"type_{j}"] = ""
            st.session_state[f"damage_{j}"] = 0
            st.session_state[f"enemyamount"] = 1 
st.button("Reset", on_click=reset_form)