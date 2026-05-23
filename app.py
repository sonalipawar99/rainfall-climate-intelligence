import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Rainfall Prediction & Climate Intelligence System")

# Load Dataset
df = pd.read_csv("rainfall_error_validation_1925_2025.csv")

# Show Dataset
st.subheader("Rainfall Dataset")
st.write(df.head())

# Rainfall Trend Graph
st.subheader("Observed vs Predicted Rainfall")

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(df['Year'],
        df['Observed_Rainfall_mm'],
        label='Observed Rainfall')

ax.plot(df['Year'],
        df['Predicted_Rainfall_mm'],
        label='Predicted Rainfall')

ax.set_xlabel("Year")
ax.set_ylabel("Rainfall")

ax.legend()

st.pyplot(fig)

# Error Graph
st.subheader("Prediction Error Percentage")

fig2, ax2 = plt.subplots(figsize=(10,5))

ax2.plot(df['Year'],
         df['Error_pct'])

ax2.set_xlabel("Year")
ax2.set_ylabel("Error Percentage")

st.pyplot(fig2)

# Conclusion
st.subheader("Project Conclusion")

st.write("""
This project analyzes historical rainfall data
to understand rainfall trends, prediction
accuracy, and climate intelligence possibilities.
""")