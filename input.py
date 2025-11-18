import streamlit as st

st.title("Trayek Praktikum")

st.write(
    "sjnxjksbcjks"
)

st.write(
    "Selamat Praktikum!"
)

input_NIM = st.text_input("Masukkan NIM: ", )
pilihan_praktikum = ["LKD", "LFD"]

pilihan_terpilih = st.selectbox(
    "Praktikum yang akan dilakukan:",
    pilihan_praktikum
)

st.button("Enter")


