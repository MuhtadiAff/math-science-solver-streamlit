import streamlit as st
from formulas import math, physics, chemistry
from solvers import math_solver, physics_solver, chemistry_solver

# Judul aplikasi
st.set_page_config(page_title="Solver Ilmu Eksakta", layout="wide")
st.title("📘 Aplikasi Rumus & Penyelesaian Soal")

# Sidebar untuk navigasi
st.sidebar.header("📚 Pilih Kategori")
category = st.sidebar.selectbox("Kategori", ["Matematika", "Fisika", "Kimia"])

# Fungsi untuk menampilkan rumus
def show_formulas(category):
    st.subheader("📐 Daftar Rumus")
    if category == "Matematika":
        for name, formula in math.get_formulas().items():
            st.markdown(f"**{name}**: {formula}")
    elif category == "Fisika":
        for name, formula in physics.get_formulas().items():
            st.markdown(f"**{name}**: {formula}")
    elif category == "Kimia":
        for name, formula in chemistry.get_formulas().items():
            st.markdown(f"**{name}**: {formula}")

# Fungsi untuk menyelesaikan soal
def solve_problem(category, problem_text):
    st.subheader("🧮 Hasil Penyelesaian")
    if category == "Matematika":
        result = math_solver.solve(problem_text)
    elif category == "Fisika":
        result = physics_solver.solve(problem_text)
    elif category == "Kimia":
        result = chemistry_solver.solve(problem_text)
    st.code(result)

# Tampilkan rumus
show_formulas(category)

# Input soal
st.subheader("📝 Masukkan Soal")
problem_input = st.text_area("Tulis soal di sini (misalnya: hitung integral dari x^2)", height=150)

if st.button("Selesaikan Soal"):
    if problem_input.strip() != "":
        solve_problem(category, problem_input)
    else:
        st.warning("Silakan masukkan soal terlebih dahulu.")

# Footer
st.markdown("---")
st.markdown("Dikembangkan oleh Muhtadi Affandi • Streamlit + Python")

