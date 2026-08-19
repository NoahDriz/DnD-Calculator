import streamlit as st
import math
st.title("DnD Damage Calculator")
Hp = st.text_input("How many Hitpoints does the character have?", key = "hp")
# Caculating Damage based on the following:
Type = st.text_input("Resistance, Vulnerability, Immunity, or Straight? ", key = "type")
match Type:
    case "Straight":
        import math
        D = st.number_input("How much Damage?", min_value=0, step=1, format="%d", key = "damage")
        TD =(D) 
    case "Resistance":
        import math
        #D = Damage
        D = st.number_input("How much Damage?", min_value=0, step=1, format="%d", key = "damage")
        #TD = Total Damage
        TD = math.floor((D)/2)
    case "Vulnerability":
        import math
        #D = Damage
        D = st.number_input("How much Damage?", min_value=0, step=1, format="%d", key = "damage")
        #TD = Total Damage
        TD = math.floor((D)*2)
    case "Immunity":
        st.write("No Damage!")
    case _:
        st.write("Please enter one of the following above.")
if st.button("Calculate"):
    RemainingHp = (int(Hp) - int(TD))
    st.write(f"Remaining Hitpoints: {RemainingHp:,}")
def reset_form():
    st.session_state["hp"] = ""
    st.session_state["type"] = ""
    st.session_state["damage"] = 0 
st.button("Reset", on_click=reset_form)