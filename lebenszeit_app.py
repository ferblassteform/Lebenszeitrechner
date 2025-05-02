import streamlit as st
from datetime import date, datetime

# Durchschnittliches Todesalter (z. B. Deutschland: 81 Jahre)
LEBENSMITTELALTER = 81

st.set_page_config(page_title="Lebenszeit-Rechner", layout="centered")

st.title("🧬 Lebenszeit-Rechner")
st.write("Finde heraus, wie viel Prozent deiner erwarteten Lebenszeit du schon gelebt hast.")

# Eingabe: Geburtstag
geburtstag = st.date_input("Gib deinen Geburtstag ein:", min_value=date(1900, 1, 1), max_value=date.today())

# Heutiges Datum und Alter berechnen
heute = date.today()
alter_in_tagen = (heute - geburtstag).days
alter_in_jahren = alter_in_tagen / 365.25

# Prozent des durchschnittlichen Lebensalters berechnen
prozente = min(100, round((alter_in_jahren / LEBENSMITTELALTER) * 100, 2))

# Fortschrittsanzeige
st.subheader(f"Du hast ca. {prozente}% deiner erwarteten Lebenszeit gelebt.")
st.progress(prozente / 100)

# Zusätzliche Info
sterbedatum = geburtstag.replace(year=geburtstag.year + LEBENSMITTELALTER)
sterbedatum_string = sterbedatum.strftime("%d.%m.%Y")

st.caption(f"(Basierend auf einem durchschnittlichen Lebensalter von {LEBENSMITTELALTER} Jahren)")
st.caption(f"Voraussichtliches Lebensende: {sterbedatum_string}")
