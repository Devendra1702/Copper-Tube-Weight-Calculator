import streamlit as st
import math

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Tube Weight Calculator", layout="centered")

# ---------------- HEADER WITH LOGO ----------------
# Place your logo image in the app folder as "microcoil_logo.png"
st.image("microcoil_logo.png", width=200)   # adjust width as needed

# Custom Title
st.markdown(
    """
    <h1 style='text-align: center; color: #003366;'>
        Tube Weight Calculator
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("Compute tube weight from OD, ID, length, and material density.")

# ---------------- INPUT FORM ----------------
with st.form("tube_inputs"):
    od_mm = st.number_input("Tube OD (mm)", min_value=0.0001, value=12.7, format="%.4f")
    id_mm = st.number_input("Tube ID (mm)", min_value=0.0, value=10.5, format="%.4f")
    length_m = st.number_input("Tube Length (m)", min_value=0.0, value=1.0, format="%.4f")
    density = st.number_input("Material Density (kg/m³)", min_value=0.0, value=8960.0, format="%.1f")
    calc_btn = st.form_submit_button("Calculate")

# ---------------- CALCULATION ----------------
if calc_btn:
    if id_mm >= od_mm:
        st.error("ID must be smaller than OD.")
    else:
        # mm → m
        od_m = od_mm / 1000.0
        id_m = id_mm / 1000.0

        # Cross-section area
        area_m2 = math.pi * (od_m**2 - id_m**2) / 4.0
        volume_m3 = area_m2 * length_m
        mass_kg = density * volume_m3
        mass_per_m = density * area_m2

        st.success("Calculation Complete")

        col1, col2 = st.columns(2)
        col1.metric("Total Weight (kg)", f"{mass_kg:.4f}")
        col2.metric("Weight per Meter (kg/m)", f"{mass_per_m:.4f}")

        with st.expander("Show Calculation Details"):
            st.write(f"OD (m): {od_m:.6f}")
            st.write(f"ID (m): {id_m:.6f}")
            st.write(f"Area (m²): {area_m2:.9f}")
            st.write(f"Volume (m³): {volume_m3:.9f}")
            st.write(f"Mass (kg): {mass_kg:.9f}")
