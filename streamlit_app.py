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

    input_NIM = st.text_input("Masukkan NIM: ")
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
    st.write("Silakan pilih modul yang ingin kamu kerjakan:")

    # TOMBOL MODUL 1 – 5
    st.button("📘 Modul 1", on_click=lambda: pilih_modul(1))
    st.button("🤖 Modul 2", on_click=lambda: pilih_modul(2))
    st.button("📦 Modul 3", on_click=lambda: pilih_modul(3))
    st.button("🧪 Modul 4", on_click=lambda: pilih_modul(4))
    st.button("📝 Modul 5", on_click=lambda: pilih_modul(5))

    st.write("---")
    st.button("⬅️ Kembali ke halaman awal", on_click=lambda: st.session_state.update(page="page1"))

# HALAMAN 3 (MENU LFD)
elif st.session_state.page == "page3":
    st.title("Praktikum LFD")
    st.write("Selamat datang di praktikum LFD!")

    st.button("⬅️ Kembali ke halaman awal", on_click=lambda: st.session_state.update(page="page1"))

# HALAMAN MODUL 1 
elif st.session_state.page.startswith("modul_"):
    nomor_modul = st.session_state.page.split("_")[1]

    if nomor_modul == "1":
        st.title("Modul 1 – Reaksi-reaksi Kimia")
        st.write("Selamat datang di Modul 1!")

        st.subheader("🎯 PDF Praktikum")
        FILE_ID = "1f8bEu46KVdLVC_pZjucA7H-dtIyj09Us"

        st.components.v1.html(
            f"""
            <iframe src="https://drive.google.com/file/d/{FILE_ID}/preview"
                    width="100%" height="600"></iframe>
            """,
            height=600,
        )
        
        st.subheader("📘 Video Praktikum")
        VIDEO_URL = "https://itbdsti.sharepoint.com/:v:/r/sites/WI1112/Shared%20Documents/General/Modul%205.mp4?csf=1&web=1&e=F2LkE4"
        st.video(VIDEO_URL)

        st.subheader("📝 Referensi Jurnal Praktikum")
         FILE_ID = "1wSQZtgceUIY-HjzbWspSWlK8KkViBtkG"

        st.components.v1.html(
            f"""
            <iframe src="https://drive.google.com/file/d/{FILE_ID}/preview"
                    width="100%" height="600"></iframe>
            """,
            height=600,
        )
        
        st.button("⬅️ Kembali ke daftar modul", on_click=lambda: st.session_state.update(page="page2"))
