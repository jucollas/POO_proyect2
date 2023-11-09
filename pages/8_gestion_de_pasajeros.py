from controller.humanResources_controller import HumanResourceController
from view.errorMessage import errorMessage            
import streamlit as st

controller = HumanResourceController()

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "Gestion de recursos humanos",
    page_icon = ":toolbox:"
)
st.write( "Bienvenido a gestion de recursos humanos (pasajeros)" )
modo = st.radio( "Elegir visualizar", ["-", "Todos", "Por vuelo"] );

if modo == "Todos":
    passengers= controller.get_all_passenger()

    st.dataframe( passengers, hide_index = True, column_config = {
        1 : "Cedula", 2 : "Nombre", 3 : "Apellido", 4 : "Fecha de nacimiento", 5: "Genero", 6 : "Direccion", 7 : "Telefono", 8 : "Email", 9 : "Nacionalidad", 10 : "info Medica", 11 : "Equipaje"
        } );

    comand = st.selectbox( "¿Que accion deseas hacer?", ["-", "Borrar pasajero"] );

    if comand == "Borrar pasajero":
        passenger = st.selectbox( "Selecciona el pasajero", [pas[0] for pas in passengers] )
        if ( st.button( "Borrar" ) ):
            controller.del_passenger(passenger)

elif modo == "Por vuelo":
    flights = controller.get_flights()
    st.dataframe( flights, hide_index = True, column_config = {
        1 : "codigo de vuelo", 2 : "Fecha", 3 : "origen", 4 : "llegada"
        } )
    
    flight = st.selectbox( "Selecciona el vuelo", [f[0] for f in flights])
    
    passengers= controller.get_flight_passenger(flight)

    st.dataframe( passengers, hide_index = True, column_config = {
        1 : "Cedula", 2 : "Nombre", 3 : "Apellido", 4 : "Fecha de nacimiento", 5: "Genero", 6 : "Direccion", 7 : "Telefono", 8 : "Email", 9 : "Nacionalidad", 10 : "info Medica", 11 : "Equipaje"
        } );
    
    comand = st.selectbox( "¿Que accion deseas hacer?", ["-", "Borrar pasajero"] );

    if comand == "Borrar pasajero":
        passenger = st.selectbox( "Selecciona el pasajero", [pas[0] for pas in passengers] )
        if ( st.button( "Borrar" ) ):
            controller.del_passenger(passenger, flight)



