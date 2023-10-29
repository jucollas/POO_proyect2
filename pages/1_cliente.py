import streamlit as st
from controller.airport_controller import Airport_Controller
from view.view_admin import create_person

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "aeropuerto",
    page_icon = ":airplane_departure:"
)

controller = Airport_Controller()

cliente = create_person( controller );

