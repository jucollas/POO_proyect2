import streamlit as st
from controller.airport_controller import Airport_Controller
import datetime

def create_person( controller : Airport_Controller ) -> None:
    st.subheader("Crear Cliente")
    
    # Recopilar los datos del cliente
    cedula = st.text_input("Cédula:")
    nombre = st.text_input("Nombre:")
    apellido = st.text_input("Apellido:")
    fecha_nacimiento = st.date_input("Fecha de Nacimiento:")
    genero = st.selectbox("Género:", ["Masculino", "Femenino", "Otro"])
    direccion = st.text_area("Dirección:")
    telefono = st.text_input("Número de Teléfono:")
    correo = st.text_input("Correo Electrónico:")
    
    # Validar y guardar los datos cuando se presiona un botón
    if st.button("Guardar Cliente", key = "Guardar cliente"):
        if cedula and nombre and apellido and fecha_nacimiento and genero and direccion and telefono and correo:
            # Aquí puedes agregar la lógica para guardar los datos del cliente en una base de datos o donde desees.
            controller.create_person(cedula, nombre, apellido, fecha_nacimiento, genero, direccion, telefono, correo)
            st.success("Cliente guardado exitosamente.")

        else:
            st.error("Por favor, completa todos los campos obligatorios.")