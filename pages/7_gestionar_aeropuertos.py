import streamlit as st
from controller.controlTower_controller import ControlTower_controller

controller = ControlTower_controller()

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "Aeropuerto",
    page_icon = ":toolbox:"
)
st.write( "Aeropuertos" )
st.dataframe( controller.get_airports(), use_container_width = True, hide_index = True, column_config = { 1 : "Ciudad del Aeropuerto ", 2 : "Cantidad de vuelos asociados", 3:"Puertas de abordaje libres" } )

seleccion = st.radio("¿Que quieres hacer?", [" - ", "Crear Aeropuerto", "Eliminar Aeropuerto"]);

if ( seleccion ==  "Crear Aeropuerto" ) :
    with st.form( "Crear Aeropuerto" ):
        name = st.text_input( "Ciudad: ", key ="cityName" );
        if ( st.form_submit_button("Crear") ):
            controller.create_airport( name );

elif ( seleccion == "Eliminar Aeropuerto"):
    elim = st.selectbox( "¿Cual quieres eliminar?", controller.get_deletable_airports() )
    if ( st.button( "Eliminar" ) ):
        controller.delete_airport( elim );