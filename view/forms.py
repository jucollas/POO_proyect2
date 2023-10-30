import datetime
import streamlit as st
from model.person import Person


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

if __name__ == "__main__":
	st.write( str(personForm( "hola" )))
