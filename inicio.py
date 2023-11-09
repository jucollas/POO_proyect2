from controller.loandig_data import loandigData
import streamlit as st

loandig_data = loandigData()
loandig_data.data_default()

# Configura el título y el icono de la página
st.set_page_config(
    page_title="Aeropuerto Alfonso Bonilla Arango",
    page_icon="✈️"
)

# Título principal
st.title("¡Bienvenido al Aeropuerto Alfonso Bonilla Arango!")

# Subtítulo
st.subheader("Su puerta de entrada a emocionantes destinos")

# Información sobre el aeropuerto
st.write(
    "El Aeropuerto Alfonso Bonilla Arango es el aeropuerto internacional que sirve a la ciudad de Cali, Colombia."
)
st.write(
    "Nuestro objetivo es brindarle una experiencia agradable y segura durante su viaje."
)

# Imagen del aeropuerto
st.image("static/image/aerop_alfonso.jpg", caption="Aeropuerto Alfonso Bonilla Arango")

# Opciones de navegación

# Pie de página
st.write("Gracias por elegir el Aeropuerto Alfonso Bonilla Arango para su viaje.")

