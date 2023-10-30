import datetime
import streamlit as st
from model.person import Person
from model.crew import Crew

def personForm( name : str = "Formulario Persona" ) -> Person :
	with st.form( name ):
		st.write( name );
		cedula = st.text_input( "Cedula: ", key = "cedula" );
		name = st.text_input( "Nombre: ", key = "name" )
		surname = st.text_input( "Apellido: ", key = "surname" )
		birthDate = st.date_input( "Fecha de Nacimiento: " );
		genre = st.selectbox( "Genero: ", ["Masculino", "Femenino", "Otro"] )
		address = st.text_input( "Direccion: ", key = "address" )
		phoneNumber = st.text_input( "Numero de telefono: ", key = "phoneNumber" )
		email = st.text_input( "Correo: ", key = "Correo" );
		if ( st.form_submit_button( "Guardar" ) ):
			return Person( cedula, name, surname, birthDate, genre, address, phoneNumber, email )

def crewForm( name : str = "Formulario tripulante" ) -> Crew :
	with st.form( name ):
		st.write( name );
		cedula = st.text_input( "Cedula: ", key = "cedula" );
		name = st.text_input( "Nombre: ", key = "name" )
		surname = st.text_input( "Apellido: ", key = "surname" )
		birthDate = st.date_input( "Fecha de Nacimiento: " );
		genre = st.selectbox( "Genero: ", ["Masculino", "Femenino", "Otro"] )
		address = st.text_input( "Direccion: ", key = "address" )
		phoneNumber = st.text_input( "Numero de telefono: ", key = "phoneNumber" )
		email = st.text_input( "Correo: ", key = "Correo" );
		jobPosition = st.text_input( "Trabajo: ", key = "jobPosition" );
		dailyWorkingHours = st.number_input( "Horas diarias de Trabajo: ", key = "dailyWorkingHours" )
		yearsExperience = st.number_input( "Años de experiencia: ", key = "yearsExperience" )
		if ( st.form_submit_button( "Guardar" ) ):
			return Crew( cedula, name, surname, birthDate, genre, address, phoneNumber, email, jobPosition, dailyWorkingHours, yearsExperience )

if __name__ == "__main__":
	st.write( str(personForm( "hola" )))
