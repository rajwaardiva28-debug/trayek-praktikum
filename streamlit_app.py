import streamlit as st

# Inisialisasi halaman
if "page" not in st.session_state:
    st.session_state.page = "page1"

def go_to_page():
    if st.session_state.pilihan == "LKD":
        st.session_state.page = "page2"
    elif st.session_state.pilihan == "LFD":
        st.session_state.page = "page3"

# HALAMAN 1
if st.session_state.page == "page1":
    st.title("Trayek Praktikum")

    st.write("Selamat Praktikum!")

    input_NIM = st.text_input("Masukkan NIM: ")
    pilihan_praktikum = ["LKD", "LFD"]

    pilihan_terpilih = st.selectbox(
        "Praktikum yang akan dilakukan:",
        pilihan_praktikum,
        key="pilihan"
    )

    st.button("Enter", on_click=go_to_page)

# HALAMAN 2 (KHUSUS LKD)
elif st.session_state.page == "page2":
    st.title("Halaman Praktikum LKD")
    st.write("Selamat datang di praktikum LKD!")
    st.write(f"Praktikum yang kamu pilih: **{st.session_state.pilihan}**")

    st.button("Kembali ke halaman awal", on_click=lambda: st.session_state.update(page="page1"))

# HALAMAN 3 (KHUSUS LFD)
elif st.session_state.page == "page3":
    st.title("Halaman Praktikum LFD")
    st.write("Selamat datang di praktikum LFD!")
    st.write(f"Praktikum yang kamu pilih: **{st.session_state.pilihan}**")

    st.button("Kembali ke halaman awal", on_click=lambda: st.session_state.update(page="page1"))



