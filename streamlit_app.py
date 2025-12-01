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
# --- HALAMAN 3 (MENU LFD - KHUSUS FTI) ---
elif st.session_state.page == "page3":
    st.title("Praktikum LFD (FTI)")
    nim_cari = st.session_state.get("input_nim", "").strip()

    if not nim_cari:
        st.warning("Silakan masukkan NIM di halaman awal.")
    else:
        try:
            # 1. BACA FILE (Header di baris pertama, jadi tidak perlu skiprows)
            df = pd.read_csv("Sebaran_LFD_FTI.csv")
            
            # Pastikan kolom NIM dibaca sebagai string
            df['NIM'] = df['NIM'].astype(str)
            
            # 2. CARI DATA MAHASISWA
            student_data = df[df['NIM'] == nim_cari]

            if not student_data.empty:
                # Ambil Data Diri
                nama_mhs = student_data.iloc[0]['NAMA']
                grup_mhs = student_data.iloc[0]['Grup']  # Mengambil data kolom Grup
                
                st.success(f"Mahasiswa ditemukan: **{nama_mhs}**")
                st.write(f"**NIM:** {nim_cari}")
                st.info(f"**Grup:** {grup_mhs}") # Menampilkan Grup
                
                st.subheader("Jadwal & Modul Praktikum")
                st.write("Berikut adalah jadwal praktikum Anda:")

                # Daftar kolom tanggal modul (15/09 SUDAH DIHAPUS dari daftar ini)
                # Sesuaikan nama kolom persis dengan di CSV (termasuk '11-Oct')
                date_cols = ["29/09", "13/10", "27/10", "11-Oct"]
                
                cols = st.columns(len(date_cols))
                
                for i, date_col in enumerate(date_cols):
                    with cols[i]:
                        # Tampilkan Tanggal sebagai Header Kecil
                        st.markdown(f"##### {date_col}")
                        
                        if date_col in student_data.columns:
                            kode_modul = student_data.iloc[0][date_col]
                            
                            # Cek validitas kode modul
                            if pd.notna(kode_modul):
                                st.write(f"Kode: **{kode_modul}**")
                                
                                try:
                                    # Ambil angka dari string (contoh: "M01" -> 1)
                                    nomor_modul_int = int(''.join(filter(str.isdigit, str(kode_modul))))
                                    
                                    # Tombol Buka Modul
                                    st.button(
                                        f"Buka {kode_modul}", 
                                        key=f"btn_{date_col}",
                                        on_click=lambda m=nomor_modul_int: pilih_modul(m)
                                    )
                                except ValueError:
                                    # Jika isinya bukan format modul (misal kosong atau text lain)
                                    st.caption("-") 
                            else:
                                st.caption("Libur / Kosong")
                        else:
                            st.caption("Jadwal Tdk Ada")
            else:
                st.error(f"NIM {nim_cari} tidak ditemukan dalam data.")
                st.write("Pastikan file CSV benar dan NIM sesuai.")

        except FileNotFoundError:
            st.error("File 'Sebaran_LFD_FTI.csv' tidak ditemukan. Harap unggah file tersebut.")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
        elif st.session_state.page.startswith("modul_"):
    # Mengambil nomor modul dari state (misal: "modul_1" -> "1")
            nomor_modul = st.session_state.page.split("_")[1]

    # Logika Tombol Kembali: 
    # Jika LFD -> Kembali ke Page 3 (Jadwal)
    # Jika LKD -> Kembali ke Page 2 (Menu LKD)
    if st.session_state.pilihan == "LKD":
        func_kembali = lambda: st.session_state.update(page="page2")
        label_kembali = "⬅️ Kembali ke Menu LKD"
    else:
        func_kembali = lambda: st.session_state.update(page="page3")
        label_kembali = "⬅️ Kembali ke Menu LFD"

    if nomor_modul == "1":
        # Cek apakah ini LFD?
        if st.session_state.pilihan == "LFD":
            st.title("Modul 01 – Fisika Dasar (LFD)")
            st.markdown("Silakan pelajari modul dan kerjakan Tugas Pendahuluan di bawah ini.")

            # Membuat Tab agar tampilan rapi
            tab_modul, tab_tp = st.tabs(["📄 File Modul", "📝 Tugas Pendahuluan"])

            # --- TAB 1: FILE MODUL ---
            with tab_modul:
                st.subheader("Modul Praktikum")
                # GANTI ID INI dengan ID File PDF Modul Fisika di Google Drive Anda
                ID_FILE_MODUL = "1f8bEu46KVdLVC_pZjucA7H-dtIyj09Us" 
                
                st.components.v1.html(
                    f'<iframe src="https://drive.google.com/file/d/{ID_FILE_MODUL}/preview" width="100%" height="600"></iframe>',
                    height=600,
                )

            # --- TAB 2: TUGAS PENDAHULUAN ---
            with tab_tp:
                st.subheader("Tugas Pendahuluan (TP)")
                st.warning("Wajib dikerjakan sebelum praktikum dimulai.")
                
                # GANTI ID INI dengan ID File PDF Soal TP di Google Drive Anda
                ID_FILE_TP = "1iOGIx1C-d9moDGba_KkjZ7v_h370ilWC" 
                
                # Jika TP berupa PDF soal:
                st.components.v1.html(
                f'<iframe src="https://drive.google.com/file/d/{ID_FILE_TP}/preview" width="100%" height="600"></iframe>',
                    height=600,
                )
                
                # ATAU Jika TP berupa Link Upload Folder:
                # st.write("Silakan lihat soal atau upload jawaban di link berikut:")
                # st.markdown(f"[Klik disini untuk akses Folder TP](https://drive.google.com/drive/folders/{ID_FILE_TP})")

        else:
            # --- BAGIAN LKD (Tidak diubah sesuai request) ---
            st.title("Modul 01 - Kimia Dasar (LKD)")
            st.write("Konten Modul 1 LKD...")
            # (Masukkan kode LKD lama di sini jika perlu)

    # ==========================================
    # KONTEN MODUL LAINNYA (Placeholder)
    # ==========================================
    elif nomor_modul == "2":
        st.title(f"Modul 02 - {st.session_state.pilihan}")
        st.write("Materi sedang disiapkan.")

    else:
        st.title(f"Modul {nomor_modul}")
        st.write("Halaman belum tersedia.")
            
    st.write("---")
    st.button("⬅️ Kembali ke halaman awal", on_click=lambda: st.session_state.update(page="page1"))
