import streamlit as st
from controller.airport_controller import Airport_Controller
import datetime

def create_person() -> dict:

    cedula = st.text_input("Cédula:")
    name = st.text_input("Nombre:")
    surname = st.text_input("Apellido:")
    birthDate = st.date_input("Fecha de Nacimiento:")
    genre = st.selectbox("Género:", ["Masculino", "Femenino", "Otro"])
    address = st.text_area("Dirección:")
    phone_number = st.text_input("Número de Teléfono:")
    email = st.text_input("Correo Electrónico:")

    person_data = {
        'cedula': cedula,
        'name': name,
        'surname': surname,
        'birthDate': birthDate,
        'genre': genre,
        'address': address,
        'phoneNumber': phone_number,
        'email': email
    }

    return person_data

def create_crew(controller: Airport_Controller) -> None:

    st.subheader("Crear Tripulante")
    
    crew_data = create_person()

    jobPosition = st.selectbox("Cargo:", [
        "Piloto al mando (Comandante o Capitán)", 
        "Primer Oficial (Co-piloto)", 
        "Tripulación de cabina", 
        "Ingeniero de vuelo (en algunos tipos de aeronaves)"
        ])
    
    dailyWorkingHours = st.number_input("Horas de Trabajo Diarias:", min_value=0, max_value=24, step=1)
    yearsExperience = st.number_input("Años de experiencia:", min_value=0, max_value=30, step=1)
    
    crew_data['jobPosition'] = jobPosition
    crew_data['dailyWorkingHours'] = dailyWorkingHours
    crew_data['yearsExperience'] = yearsExperience


    if st.button("Guardar Tripulante"):
        if all(value != None for value in crew_data.values()):
            controller.create_crew(**crew_data)
            st.success("Tripulante guardado exitosamente.")
        else:
            st.error("Por favor, completa todos los campos obligatorios.")
