import streamlit as st

# Inisialisasi halaman
if "page" not in st.session_state:
    st.session_state.page = "page1"

def go_to_page():
    if st.session_state.pilihan == "LKD":
        st.session_state.page = "page2"
    elif st.session_state.pilihan == "LFD":
        st.session_state.page = "page3"

def pilih_modul(modul):
    st.session_state.page = f"modul_{modul}"

# HALAMAN 1
if st.session_state.page == "page1":
    st.title("Trayek Praktikum")

    st.write("Selamat Praktikum!")

    input_NIM = st.text_input("Masukkan NIM: ", key="input_nim")
    pilihan_praktikum = ["LKD", "LFD"]

    pilihan_terpilih = st.selectbox(
        "Praktikum yang akan dilakukan:",
        pilihan_praktikum,
        key="pilihan"
    )

    st.button("Enter", on_click=go_to_page)
    
# HALAMAN 2 (MENU LKD)
elif st.session_state.page == "page2":
    st.title("Praktikum LKD")
    st.write("Selamat datang di praktikum LKD!")

    st.subheader("🎯 Modul Praktikum")
    FILE_ID = "1f8bEu46KVdLVC_pZjucA7H-dtIyj09Us"

    st.components.v1.html(
        f"""
        <iframe src="https://drive.google.com/file/d/{FILE_ID}/preview"
            width="100%" height="600"></iframe>
        """,
            height=600,
        )

    st.subheader("Jurnal Praktikum")
    FILE_ID2 = "114LSosxqP_GIZ8KGI1nZpno_0L1e23BR"
        
    st.components.v1.html(
        f"""
        <iframe src="https://drive.google.com/embeddedfolderview?id={FILE_ID2}"
            width="100%" height="200"></iframe>
        """,
            height=200,
        )

    st.subheader("Video Praktikum")
    FILE_ID3 = "1qQ4ROgoR1X3yalDSmubNbIP3OSDJLTT4"
        
    st.components.v1.html(
        f"""
        <iframe src="https://drive.google.com/embeddedfolderview?id={FILE_ID3}"
            width="100%" height="200"></iframe>
        """,
            height=200,
        )
    
    st.write("---")
    st.button("⬅️ Kembali ke halaman awal", on_click=lambda: st.session_state.update(page="page1"))

# HALAMAN 3 (MENU LFD)
elif st.session_state.page == "page3":
    st.title("Praktikum LFD")
    st.write("Selamat datang di praktikum LFD!")

    st.button("⬅️ Kembali ke daftar modul", 
              on_click=lambda: st.session_state.update(page="page3"))
