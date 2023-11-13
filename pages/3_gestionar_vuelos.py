from controller.flight_controller import FlightController
from view.flightFrom import flightFrom

import streamlit as st

controller = FlightController()

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "Vuelo",
    page_icon = ":toolbox:"
)
st.write( "Bienvenido a los vuelos" )
modo = st.radio( "Elegir visualizar", ["-", "Aerolineas", "Torre de control"] );

if modo == "Aerolineas":
    airline = st.selectbox( "Elegir la aerolinea", controller.get_airlines() );
    st.dataframe( controller.get_airline_flights( airline ), hide_index = True, column_config = {
        1 : "codigo de vuelo", 2 : "Fecha", 3 : "origen", 4 : "llegada", 5: "serie aeronave", 6 : "tripulacion", 7 : "Asientos Disponibles", 8 : "En el aire"
        } );

    comand = st.selectbox( "¿Que accion deseas hacer?", ["-", "Iniciar Vuelo", "Cancelar Vuelo", "Crear vuelo"] );

    if comand == "Iniciar Vuelo":
        flight = st.selectbox( "Elegir Vuelo", controller.get_startable_flights( airline ) );
        if ( st.button( "Iniciar" ) ):
            controller.start_flight( airline, flight )
    elif comand == "Cancelar Vuelo":
        flight = st.selectbox( "Elegir Vuelo", controller.get_airline_flight_id( airline ) );
        if ( st.button( "Cancelar" ) ):
            controller.cancel_flight( airline, flight )
    elif comand == "Crear vuelo":
        flightFrom(controller, 'Vuelo')

elif modo == "Torre de control":
    airport = st.selectbox( "Elegir el aeropuerto", controller.get_airports() );
    st.dataframe( controller.get_airport_flights( airport ), hide_index = True, column_config = {
        1 : "codigo de vuelo", 2 : "Fecha", 3 : "origen", 4 : "llegada", 5: "serie aeronave", 6 : "tripulacion", 7 : "Asientos Disponibles", 8 : "En el aire"
        } );

    comand = st.selectbox( "¿Que accion deseas hacer?", ["-", "Despegar", "Aterrizar", "Terminar Vuelo", "Continuar Vuelo", "Visualzar mensajes", "Solicitar reporte"] );

    if comand == "Despegar":
        flight = st.selectbox( "Elegir Vuelo", controller.get_takeOff_flights( airport ) );
        if ( st.button( "Despegar" ) ):
            controller.takeOff_flight( airport, flight )
    elif comand == "Aterrizar":
        flight = st.selectbox( "Elegir Vuelo", controller.get_landing_flights( airport ) );
        if ( st.button( "Aterrizar" ) ):
            controller.land_flight( airport, flight )

    elif comand == "Terminar Vuelo":
        flight = st.selectbox( "Elegir Vuelo", controller.get_finishing_flights( airport ) );
        if ( st.button( "Terminar" ) ):
            controller.end_flight( airport, flight )

    elif comand == "Continuar Vuelo":
        flight = st.selectbox( "Elegir Vuelo", controller.get_continue_flights( airport ) );
        if ( st.button( "Continuar" ) ):
            controller.continue_flight( airport, flight )

    elif comand == "Solicitar reporte":
        flight = st.selectbox( "Elegir Vuelo", controller.get_continue_flights( airport )  )

        st.write( "Historial" )
        st.dataframe( controller.get_messages_flight(flight), hide_index = True, column_config = {
        1 : "codigo de vuelo", 2 : "Fecha", 3 : "origen", 4 : "llegada", 5: "serie aeronave", 6 : "tripulacion", 7 : "Asientos Disponibles", 8 : "En el aire"
        } );
        if ( st.button( "Solicitar informacion a %s" %(flight) ) ):
            message = controller.notifyFlights(flight, airport)
            st.write("Mesaje recibido:")
            st.write(message)

        


