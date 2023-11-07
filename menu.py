from controller.loandig_data import loandigData
import streamlit as st

loandig_data = loandigData()
loandig_data.data_default()

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "aeropuerto",
    page_icon = ":airplane_departure:"
)

# Configurar el título de la aplicación
st.title('Buenas')
st.write( "Este es una cosa que no esta terminada" )
st.write( "Se escribe esto para algo como par que se entienda algo")