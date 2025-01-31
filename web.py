import streamlit as st
import pandas as pd

def calculate_risk_score(data):
    # Menentukan bobot untuk setiap parameter
    scoring = {
        "Pekerjaan": {"buruh": 3, "IRT": 2, "guru": 1, "mahasiswa": 1, "freelancer": 2, "PNS": 1, "tidak bekerja": 3},
        "Pendidikan Terakhir": {"SD": 3, "SMP": 2, "SMA": 1, "Perguruan Tinggi": 1, "Tidak Sekolah": 4},
        "Aktivitas Fisik": {"Ringan": 3, "Sedang": 2, "Berat": 1},
        "Status Gizi": {"UnderWeight": 4, "Normal": 1, "OverWeight": 2, "Obesitas": 3},
        "Konsumsi Obat Tambah Darah": {"Sering": 1, "Jarang": 2, "Tidak Pernah": 3},
        "Konsumsi Suplemen Tambahan": {"Sering": 1, "Jarang": 2, "Tidak Pernah": 3},
        "Konsumsi Nasi per Sajian": {"½ Centong": 3, "1 Centong": 2, ">2 Centong": 1},
        "Riwayat Anemia": {"Pernah": 3, "Tidak Pernah": 1},
        "KEK": {"Beresiko KEK": 4, "Tidak Beresiko KEK": 1},
        "Konsumsi Tinggi Protein": {"Jarang": 3, "Cukup Sering": 2, "Sering": 1},
        "Konsumsi Buah dan Sayur": {"Jarang": 3, "Cukup Sering": 2, "Sering": 1},
        "Kebiasaan Makan": {"1 kali sehari": 4, "2 kali sehari": 3, "3 kali sehari": 2, ">3 kali sehari": 1}
    }
    
    total_score = 0
    for key, value in data.items():
        if key in scoring and value in scoring[key]:
            total_score += scoring[key][value]
    
    return total_score

def classify_risk(score):
    if score <= 10:
        return "Risiko Rendah"
    elif score <= 20:
        return "Risiko Sedang"
    else:
        return "Risiko Tinggi"

# Streamlit UI
st.title("Sistem Pencegahan Risiko Stunting")

# Input Form
st.header("Masukkan Data")
data = {}
data["Pekerjaan"] = st.selectbox("Pekerjaan", ["buruh", "IRT", "guru", "mahasiswa", "freelancer", "PNS", "tidak bekerja"])
data["Pendidikan Terakhir"] = st.selectbox("Pendidikan Terakhir", ["SD", "SMP", "SMA", "Perguruan Tinggi", "Tidak Sekolah"])
data["Aktivitas Fisik"] = st.selectbox("Aktivitas Fisik", ["Ringan", "Sedang", "Berat"])
data["Status Gizi"] = st.selectbox("Status Gizi", ["UnderWeight", "Normal", "OverWeight", "Obesitas"])
data["Konsumsi Obat Tambah Darah"] = st.selectbox("Konsumsi Obat Tambah Darah", ["Sering", "Jarang", "Tidak Pernah"])
data["Konsumsi Suplemen Tambahan"] = st.selectbox("Konsumsi Suplemen Tambahan", ["Sering", "Jarang", "Tidak Pernah"])
data["Konsumsi Nasi per Sajian"] = st.selectbox("Konsumsi Nasi per Sajian", ["½ Centong", "1 Centong", ">2 Centong"])
data["Riwayat Anemia"] = st.selectbox("Riwayat Anemia", ["Pernah", "Tidak Pernah"])
data["KEK"] = st.selectbox("KEK", ["Beresiko KEK", "Tidak Beresiko KEK"])
data["Konsumsi Tinggi Protein"] = st.selectbox("Konsumsi Tinggi Protein", ["Jarang", "Cukup Sering", "Sering"])
data["Konsumsi Buah dan Sayur"] = st.selectbox("Konsumsi Buah dan Sayur", ["Jarang", "Cukup Sering", "Sering"])
data["Kebiasaan Makan"] = st.selectbox("Kebiasaan Makan", ["1 kali sehari", "2 kali sehari", "3 kali sehari", ">3 kali sehari"])

if st.button("Hitung Risiko"):
    score = calculate_risk_score(data)
    risk_level = classify_risk(score)
    st.subheader(f"Total Skor: {score}")
    st.subheader(f"Tingkat Risiko: {risk_level}")
