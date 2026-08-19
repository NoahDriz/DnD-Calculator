import streamlit as st
import math
st.title("DnD Damage Calculator")
Hp = st.text_input("How many Hitpoints does the character have?")
# Caculating Damage based on the following:
Type = st.text_input("Resistance,Vulnerability,Immunity, or Straight? ")
if Type == "Straight":
    D = st.text_input("How much Damage?")
    TD = (D)
if Type == "Resistance":
    import math
    # D = Damage
    D = st.text_input("How much Damage?")
    #TD = Total Damage
    TD = math.floor((D/2))
elif Type == "Vulnerability":
    import math
    #D = Damage
    D = st.text_input("How much Damage?")
    #TD = Total Damage
    TD = math.floor((D)*2)
elif Type == "Immunity":
    st.write("No Damage!")
if st.button("Calculate"):
    RemainingHp = (int(Hp) - int(TD))
    st.write(f"Remaining Hitpoints: {RemainingHp:,}")