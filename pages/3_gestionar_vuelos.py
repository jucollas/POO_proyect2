import streamlit as st
import controller.flight_controller as controller

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "vuelo",
    page_icon = ":toolbox:"
)
st.write( "Bienvenido a los vuelos" )
modo = st.radio( "Elegir visualizar", ["-", "Aerolineas", "Aeropuertos"] );

if modo == "Aerolineas":
    airline = st.selectbox( "Elegir la aerolinea", controller.get_airlines() );
    st.dataframe( controller.get_airline_flights( airline ), hide_index = True, column_config = {
        1 : "codigo de vuelo", 2 : "Fecha", 3 : "origen", 4 : "llegada", 5: "serie aeronave", 6 : "pasajeros", 7 : "tripulacion", 8 : "En el aire"
        } );

    comand = st.selectbox( "¿Que accion deseas hacer?", ["-", "Iniciar Vuelo", "Cancelar Vuelo", "Crear vuelo"] );

    if comand == "Iniciar Vuelo":
        flight = st.selectbox( "Elegir Vuelo", controller.get_airline_flight_id( airline ) );
        if ( st.button( "Iniciar" ) ):
            controller.start_flight( airline, flight )
    elif comand == "Cancelar Vuelo":
        flight = st.selectbox( "Elegir Vuelo", controller.get_airline_flight_id( airline ) );
        if ( st.button( "Cancelar" ) ):
            controller.cancel_flight( airline, flight )
    elif comand == "Crear vuelo":
        with st.form( "Vuelo" ):
            flightCode = st.text_input( "Codigo de Vuelo: ", key = "flightCode" );
            selectedAirline = st.selectbox( "Aerolinea: ", controller.get_airlines() );
            date = st.date_input( "Fecha del vuelo: ", key = "date" );
            origin = st.selectbox( "Aeropuerto de salida", controller.get_airports() )
            destiny = st.selectbox( "Aeropuerto de llegada",controller.get_airports() );
            st.write( "Aeronave" );
            aircraft = st.selectbox( "<numero serie>|<marca> - <modelo> - <pasajeros> - <velocidad maxima> - <autonomia>", controller.get_posible_aircraft() );
            st.write( "tripulantes" )
            crew = st.multiselect( "<cedula>|<nombre> - <apellido> - <trabajo> - <horas diarias de trabajo> - <experiencia>", controller.get_crew() );
            if ( st.form_submit_button( "Guardar" ) ):
                controller.create_flight( selectedAirline, (aircraft.split("|"))[0], flightCode, date, origin, destiny, [ (el.split("|"))[0] for el in crew ] );

elif modo == "Aeropuertos":
    airport = st.selectbox( "Elegir el aeropuerto", controller.get_airports() );
    st.dataframe( controller.get_airport_flights( airport ), hide_index = True, column_config = {
        1 : "codigo de vuelo", 2 : "Fecha", 3 : "origen", 4 : "llegada", 5: "serie aeronave", 6 : "pasajeros", 7 : "tripulacion", 8 : "En el aire"
        } );

    comand = st.selectbox( "¿Que accion deseas hacer?", ["-", "Despegar", "Aterrizar", "Terminar Vuelo", "Continuar Vuelo", "Dar informacion"] );

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
    elif comand == "Dar informacion":
        pass#nota hacer esto


