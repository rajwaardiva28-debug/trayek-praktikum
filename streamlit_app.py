import streamlit as st
import pandas as pd

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

# Load sebaran peserta (convert PDF ke DataFrame untuk lookup)
@st.cache_data
def load_sebaran():
    df = pd.read_csv("/mnt/data/sebaran_LFD.csv")  
    return df

df_sebaran = load_sebaran()

def get_modul_LFD(nim):
    """Return list modul berdasarkan NIM"""
    row = df_sebaran[df_sebaran["NIM"] == int(nim)]
    if row.empty:
        return []
    
    modul_cols = ["08/09", "22/09", "06/10", "20/10", "03/11"]  # kolom modul
    raw_modul = list(row[modul_cols].values[0])

    # Contoh: ["M01","M07","M02","M08"] → ambil angka belakang
    modul_numbers = [int(m[1:]) for m in raw_modul if isinstance(m,str)]

    return modul_numbers

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
    st.write("Silakan pilih modul yang ingin kamu kerjakan:")

    # TOMBOL MODUL 1 – 5
    st.button("Modul 1", on_click=lambda: pilih_modul(1))
    st.button("Modul 2", on_click=lambda: pilih_modul(2))
    st.button("Modul 3", on_click=lambda: pilih_modul(3))
    st.button("Modul 4", on_click=lambda: pilih_modul(4))
    st.button("Modul 5", on_click=lambda: pilih_modul(5))

    st.write("---")
    st.button("⬅️ Kembali ke halaman awal", on_click=lambda: st.session_state.update(page="page1"))

# HALAMAN 3 (MENU LFD)
elif st.session_state.page == "page3":
    st.title("Praktikum LFD")
    st.write("Selamat datang di praktikum LFD!")

    nim = st.session_state.get("input_nim", "")

    if nim == "":
        st.warning("Masukkan NIM terlebih dahulu di halaman awal.")
    else:
        modul_list = get_modul_LFD(nim)

        if len(modul_list) == 0:
            st.error("NIM tidak ditemukan di sebaran praktikum.")
        else:
            st.subheader("Modul yang harus kamu kerjakan:")

            for modul in modul_list:
                label = f"Modul {modul:02d}"
                st.button(label, on_click=lambda m=modul: pilih_modul(m))

    st.write("---")
    st.button("⬅️ Kembali ke halaman awal", on_click=lambda: st.session_state.update(page="page1"))

elif st.session_state.page.startswith("modul_"):
    nomor_modul = int(st.session_state.page.split("_")[1])

    st.title(f"Modul LFD {nomor_modul:02d}")

    st.write("Selamat datang di modul praktikum!")

    # Ganti FILE_ID setiap modul jika punya file berbeda
    FILE_ID = "GOOGLE_DRIVE_ID_MODUL"  

    st.components.v1.html(
        f"""
        <iframe src="https://drive.google.com/file/d/{FILE_ID}/preview"
                width="100%" height="600"></iframe>
        """,
        height=600,
    )

    st.button("⬅️ Kembali ke daftar modul", 
              on_click=lambda: st.session_state.update(page="page3"))


# HALAMAN MODUL 1 
elif st.session_state.page.startswith("modul_"):
    nomor_modul = st.session_state.page.split("_")[1]

    if nomor_modul == "1":
        st.title("Modul 1 – Reaksi-reaksi Kimia")
        st.write("Selamat datang di Modul 1!")

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
        FILE_ID1 = "1wSQZtgceUIY-HjzbWspSWlK8KkViBtkG"
        st.components.v1.html(
            f"""
            <iframe src="https://drive.google.com/embeddedfolderview?id={FILE_ID1}"
                    width="100%" height="100"></iframe>
            """,
            height=100,
        )

        st.subheader("📘 Video Praktikum")
        VIDEO_URL = "https://itbdsti.sharepoint.com/:v:/r/sites/WI1112/Shared%20Documents/General/Modul%205.mp4?csf=1&web=1&e=7Kr7bi&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D"
        st.video(VIDEO_URL)
        
        st.button("⬅️ Kembali ke daftar modul", on_click=lambda: st.session_state.update(page="page2"))

    elif nomor_modul == "2":
        st.title("Modul 2 – Stokiometri Reaksi Kimia")
        st.write("Selamat datang di Modul 2!")

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

     
    elif nomor_modul == "3":
        st.title("Modul 3 – Stokiometri Reaksi Kimia")
        st.write("Selamat datang di Modul 3!")

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

    elif nomor_modul == "4":
        st.title("Modul 4 – Stokiometri Reaksi Kimia")
        st.write("Selamat datang di Modul 4!")

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

    elif nomor_modul == "5":
        st.title("Modul 5 – Stokiometri Reaksi Kimia")
        st.write("Selamat datang di Modul 5!")

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

    st.button("⬅️ Kembali ke daftar modul", on_click=lambda: st.session_state.update(page="page2"))
