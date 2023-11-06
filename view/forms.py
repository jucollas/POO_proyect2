from controller.passenger_controller import PassengerController
from controller.crew_controller import CrewController
import streamlit as st

def personForm() -> dict[str, str] :
	cedula = st.text_input( "Cedula: ", key = "cedula" )
	name = st.text_input( "Nombre: ", key = "name" )
	surname = st.text_input( "Apellido: ", key = "surname" )
	birthDate = st.date_input( "Fecha de Nacimiento: ")
	genre = st.selectbox( "Genero: ", ["Masculino", "Femenino", "Otro"] )
	address = st.text_input( "Direccion: ", key = "address" )
	phoneNumber = st.text_input( "Numero de telefono: ", key = "phoneNumber" )
	email = st.text_input( "Correo: ", key = "Correo" )
	person_data = {
		'cedula': cedula,
		'name': name,
		'surname': surname,
		'birthDate': birthDate,
		'genre': genre,
		'address': address,
		'phoneNumber': phoneNumber,
		'email': email
	}
	return person_data

def crewForm(controller : CrewController ,  name : str = "Formulario tripulante" ) -> None :
	with st.form( name ):
		st.write( name )
		crew_data = personForm()
		jobPosition = jobPosition = st.selectbox("Cargo:", [
        "Piloto al mando (Comandante o Capitán)", 
        "Primer Oficial (Co-piloto)", 
        "Tripulación de cabina", 
        "Ingeniero de vuelo (en algunos tipos de aeronaves)"
        ], key = 'jobPosition')
		dailyWorkingHours = st.number_input("Horas de Trabajo Diarias:", min_value=0, max_value=24, step=1, key = "dailyWorkingHours" )
		yearsExperience = st.number_input("Años de experiencia:", min_value=0, max_value=30, step=1, key = "yearsExperience" )
		crew_data['jobPosition'] = jobPosition
		crew_data['dailyWorkingHours'] = dailyWorkingHours
		crew_data['yearsExperience'] = yearsExperience
		if ( st.form_submit_button( "Guardar" ) ):
			controller.create_crewMember(**crew_data)

def PassagerForm(controller : PassengerController, name : str = "Formulario Pasajero"):
	with st.form ( name ):
		st.write( name )
		passager_data = personForm()
		nationality = st.text_input( "Nacionalidad: ", key = "Nacionalidad" )
		medicalInfo = st.text_area( "Informacion medica: ", key = "medicaInfo" )
		luggageAmount = st.selectbox( "Equipaje: ", ["Super liviano", "Liviano", "Mediano", "Grande"], key = "Equipaje" )
		passager_data['nationality'] = nationality
		passager_data['medicalInfo'] = medicalInfo
		passager_data['luggageAmount'] = luggageAmount
		if ( st.form_submit_button( "Guardar" ) ):
			controller.create_passager(**passager_data)

if __name__ == "__main__":
	st.write( str(personForm( "hola" )))
