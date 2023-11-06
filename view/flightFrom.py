from controller.flight_controller import FlightController

import streamlit as st


def flightFrom(controller : FlightController, name : str ):
    with st.form( name ):
        flightCode = st.text_input( "Codigo de Vuelo: ", key = "flightCode" );
        selectedAirline = st.selectbox( "Aerolinea: ", controller.get_airlines() );
        date = st.date_input( "Fecha del vuelo: ", key = "date")
        origin = st.selectbox( "Aeropuerto de salida", controller.get_airports() )
        destiny = st.selectbox( "Aeropuerto de llegada",controller.get_airports() );
        st.write( "Aeronave" )
        aircraft = st.selectbox( "<numero serie>|<marca> - <modelo> - <pasajeros> - <velocidad maxima> - <autonomia>", controller.get_posible_aircraft() )
        st.write( "tripulantes" )
        crew = st.multiselect( "<cedula> | <nombre> - <apellido> - <trabajo> - <horas diarias de trabajo> - <experiencia>", controller.get_crew() )
        if ( st.form_submit_button( "Guardar" ) ):
            controller.create_flight( selectedAirline, None if aircraft is None else (aircraft.split("|"))[0], flightCode, date, origin, destiny, None if crew is None else  [ (el.split("|"))[0] for el in crew ] );
