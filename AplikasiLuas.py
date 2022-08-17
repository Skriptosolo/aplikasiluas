import streamlit as st

st.title("MyAplication")
st.write("# Choirul Anam Firman Thohari")
st.write("""
## Aplikasi Luas Segitiga
Ini adalah aplikasi menghitung luas Segitiga
""")

alas = st.number_input("Masukan Alas", 0)
tinggi = st.number_input("Masukan Tinggi", 0)
hitung = st.button("Hitung Luas")

if hitung:
    luas = 0.5 * alas * tinggi
    st.success(f"Luas Segitiganya adalah {luas}")

st.write("""
## Aplikasi Luas Persegi Panjang
Ini adalah aplikasi menghitung Luas Persegi Panjang
""")

panjang = st.number_input("Masukan Panjang", 0)
lebar = st.number_input("Masukan Lebar", 0)
A = st.button("Hitung Luas Persegi Panjang")

if A:
    A = panjang * lebar
    st.success(f"Luas Persegi Panjangnya adalah {A}")
    st.balloons()

