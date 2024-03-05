import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Sidebar Layout
st.sidebar.title("Sidebar")

# Sidebar Widgets
selected_option = st.sidebar.radio("Select an option", ["Chemie", "Biologie", "Informatik"])
user_name = st.sidebar.text_input("Gib deinen Namen ein")

# Main Content
st.title("Wähle dein Fach")

# Main Container
with st.container():
    st.header("Inhalt")

    # Container 1
    with st.expander("Bilder"):
        st.write("Container 1")
        if selected_option == "Chemie":
            st.image("img1.jpg", caption="Chemie", use_column_width=True)
            st.write("Chemie")
        elif selected_option == "Biologie":
            st.image("img2.jpg", caption="Biologie", use_column_width=True)
            st.write("Biologie")
        else:
            st.image("img3.jpg", caption="Informatik", use_column_width=True)
            st.write("Informatik")

    # Container 2
    with st.expander("Text"):
        st.write("Container 2")
        if selected_option == "Chemie":
            st.code("Du hast Chemie ausgewählt", language="python")
        elif selected_option == "Biologie":
            st.code("Du hast Biologie ausgewählt", language="python")
        else:
            st.code("Du hast Informatik ausgewählt", language="python")

    # Chat Element
    with st.expander("Kommentar"):
        st.subheader("Schreibe ein Kommentar")
        chat_input = st.text_area("Dein Kommentar:")
        if st.button("Senden"):
            st.write(f"Du: {chat_input}")
            # Hier könntest du die Eingabe analysieren und eine Antwort generieren (Bot-Logik).

# Display User Input
st.write(f"Hallo {user_name}, du hast {selected_option} gewählt.")

st.header('Fächer', divider='rainbow')

columns = ["Biologie", "Chemie", "English", "Informatik", "Mathematik", "Physik", "Klinische Chemie", "Histologie"]
data = np.random.randn(10, len(columns))
df = pd.DataFrame(data, columns=columns)
st.dataframe(df)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["schwer", "einfach", "mittel"])
st.line_chart(chart_data)

start_time = st.slider(
    "Wann starte ich?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
