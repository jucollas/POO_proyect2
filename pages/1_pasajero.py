import streamlit as st
from controller.passenger_controller import PassengerController
from view.forms import PassagerForm

controller = PassengerController()

st.set_page_config(
    page_title = "Cliente",
    page_icon = ":toolbox:"
)

seleccion = st.radio("¿Que quieres hacer?", [" - ", "Registrar pasajero", "Comprar Vuelo"] );
if ( seleccion == "Registrar pasajero" ):
    PassagerForm( controller, "Registrar pasajero" )

elif ( seleccion == "Comprar Vuelo" ):
    
    origin = st.selectbox("Origen: ", controller.get_airports())
    destiny = st.selectbox("Destino: ", controller.get_airports())
    date = st.date_input("Fecha:")

    flights = controller.get_flight_filter(origin, destiny, date )
    print(flights)

    st.dataframe( flights, hide_index = True, column_config = {
        1 : "codigo de vuelo", 2 : "Fecha", 3 : "origen", 4 : "llegada", 5: "serie aeronave", 6 : "tripulacion", 7 : "En el aire"
        } )
    client = st.text_input("Cedula:")
    flight = st.selectbox("Identificador de Vuelo", [f[0] for f in flights] )
    if ( st.button( "Comprar" ) ):
        controller.assing_passenger_to_flight( client, flight )