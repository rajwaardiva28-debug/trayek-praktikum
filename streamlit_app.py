import streamlit as st

st.title("Trayek Praktikum")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write(
    "ahsgdgafsd"
)

input_NIM = st.text_input("Masukkan NIM: ", )
pilihan_praktikum = ["LKD", "LFD"]

pilihan_terpilih = st.selectbox(
    "Praktikum yang akan dilakukan:",
    pilihan_praktikum
)
