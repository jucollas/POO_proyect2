import streamlit as st
from controller.passenger_controller import PassengerController
#from controller.flight_controller import FlightController
from view.forms import PassagerForm

controller = PassengerController()
#controllerFlight = FlightController()


#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "cliente",
    page_icon = ":toolbox:"
)

seleccion = st.radio("¿Que quieres hacer?", [" - ", "Registrar Nuevo Cliente", "Comprar Vuelo"] );
if ( seleccion == "Registrar Nuevo Cliente" ):
    PassagerForm( controller, "Registrar Nuevo Cliente" )

elif ( seleccion == "Comprar Vuelo" ):
    
    origin = st.selectbox("Origen: ", controller.get_airports())
    destiny = st.selectbox("Destino: ", controller.get_airports())
    date = st.date_input("Fecha:", min_value='today')

    flights = controller.get_flight_filter(origin, destiny, date )

    st.dataframe( flights, hide_index = True, column_config = {
        1 : "codigo de vuelo", 2 : "Fecha", 3 : "origen", 4 : "llegada", 5: "serie aeronave", 6 : "pasajeros", 7 : "tripulacion", 8 : "En el aire"
        } )
    client = st.text_input("Cedula:")
    flight = st.selectbox("Identificador de Vuelo", [f[0] for f in flights] )
    if ( st.button( "Comprar" ) ):
        controller.assing_passenger_to_flight( client, flight )



