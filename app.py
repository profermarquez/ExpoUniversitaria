import streamlit as st
import csv

# Título del formulario
st.title("Encuesta de Interés en Programación")

# Pregunta de interés
interes = st.selectbox(
    "¿Cuánto interés tenés para aprender a programar?",
    ["Mucho", "Poco", "Algo", "Ninguno"]
)

# Botón para enviar la respuesta
if st.button("Enviar"):
    # Guardar la respuesta en un archivo CSV
    with open('respuestas.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([interes])
    st.success("¡Gracias por tu respuesta!")

# Mostrar respuestas anteriores
if st.checkbox("Mostrar respuestas anteriores"):
    with open('respuestas.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            st.write(f"Interés: {row[0]}")
