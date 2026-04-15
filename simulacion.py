#mian
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k

st.set_page_config(page_title="Catástrofe UV", layout="wide")

st.title("🌡️ Simulación: Física Clásica vs Cuántica")
st.subheader("El problema del Cuerpo Negro")

# Slider de temperatura
T = st.slider("Temperatura (K)", 500, 10000, 5000, step=100)

# Rango de longitudes de onda (nm)
lambda_nm = np.linspace(10, 3000, 1000)  # 10 nm a 3000 nm
lambda_m = lambda_nm * 1e-9

# Ley de Planck (cuántica)
def planck(lambda_m, T):
    return (2 * h * c**2) / (lambda_m**5) * 1/(np.exp((h*c)/(lambda_m*k*T)) - 1)

# Ley de Rayleigh-Jeans (clásica)
def rayleigh_jeans(lambda_m, T):
    return (2 * c * k * T) / (lambda_m**4)

# Calcular
I_planck = planck(lambda_m, T)
I_rj = rayleigh_jeans(lambda_m, T)

# Gráfica
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(lambda_nm, I_rj, 'r--', label="Rayleigh-Jeans (Clásica)", linewidth=2)
ax.plot(lambda_nm, I_planck, 'b-', label="Planck (Cuántica)", linewidth=2)

# Sombrear región UV problemática
ax.axvspan(10, 400, alpha=0.2, color='red', label="Región UV (Catástrofe)")

ax.set_xlabel("Longitud de onda (nm)")
ax.set_ylabel("Intensidad espectral (W/m³)")
ax.set_title(f"Radiación de Cuerpo Negro - T = {T} K")
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_xlim(10, 3000)
ax.set_ylim(0, max(I_planck)*1.2)

# Mostrar en Streamlit
st.pyplot(fig)

# Explicación
col1, col2 = st.columns(2)

with col1:
    st.info("🔴 **Falla clásica**")
    st.latex(r"I(\lambda, T) = \frac{2ck_B T}{\lambda^4}")
    st.write("Para λ → 0, I → ∞ (¡absurdo!)")

with col2:
    st.success("✅ **Solución cuántica**")
    st.latex(r"I(\lambda, T) = \frac{2hc^2}{\lambda^5} \cdot \frac{1}{e^{\frac{hc}{\lambda k_B T}} - 1}")
    st.write("Planck: energía cuantizada $E = h\\nu$")

# Mostrar valores
st.caption(f"Constante de Planck h = {h:.3e} J·s")