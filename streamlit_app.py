import streamlit as st

# Inisialisasi halaman
if "page" not in st.session_state:
    st.session_state.page = "page1"

def next_page():
    st.session_state.page = "page2"

# HALAMAN 1
if st.session_state.page == "page1":
    st.title("Trayek Praktikum")

    st.write("Selamat Praktikum!")

    input_NIM = st.text_input("Masukkan NIM: ")
    pilihan_praktikum = ["LKD", "LFD"]

    pilihan_terpilih = st.selectbox(
        "Praktikum yang akan dilakukan:",
        pilihan_praktikum
    )

    st.button("Enter", on_click=next_page)

# HALAMAN 2
elif st.session_state.page == "page2":
    st.title("Halaman berikutnya")
    st.write("Ini halaman lanjutan setelah kamu tekan Enter.")



