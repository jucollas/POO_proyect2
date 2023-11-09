import streamlit as st
from controller.passenger_controller import PassengerController
from view.forms import PassagerForm

controller = PassengerController()

st.set_page_config(
    page_title = "Cliente",
    page_icon = ":toolbox:"
)

seleccion = st.radio("¿Que quieres hacer?", [" - ", "Registrar pasajero", "Comprar Vuelo", "Informacion paises"] );
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

elif (seleccion == "Informacion paises"):
    st.title("Información de Países")
    # Crear una lista de países que el usuario puede seleccionar
    country_list = [
    "Colombia", "Argentina", "Brasil", "Perú", "Ecuador",
    "Canada", "Mexico", "Chile", "Venezuela",
    "España", "France", "Germany", "Italia", "United Kingdom",
    "Japan", "South Korea", "Australia",
    "South Africa", "Egypt", "Nigeria", "Russia",
    "Saudi Arabia", "United Arab Emirates", "Turkey", "Iran", "Iraq",
    "Greece", "Netherlands", "Belgium", "Switzerland", "Austria","Portugal"
    ]
    selected_country = st.selectbox("Selecciona un país:", country_list)

    if st.button("Obtener Información"):
        country_data = controller.get_country_data(selected_country)
        if country_data:
            st.subheader(country_data["name"]["common"])
            st.write(country_data['name']['official'])

            st.image(country_data["flags"]["svg"], use_column_width=True)
            st.write(country_data['flags']['alt'])

            # Crear una tabla para mostrar la información
            country_info = {
                "Capital": ', '.join(country_data['capital']),
                "Monedas": ', '.join([f"{cur['name']} ({cur['symbol']})" for cur in country_data['currencies'].values()]),
                "Idiomas nativos": ', '.join(country_data["languages"].values()),
                "Región": country_data['region'],
                "Subregión": country_data['subregion'],
                "Población": country_data['population'],
            }
            st.table(country_info)

            # Mostrar la bandera
            
        else:
            st.error("Error en la consulta de datos. Asegúrate de seleccionar un país válido.")



