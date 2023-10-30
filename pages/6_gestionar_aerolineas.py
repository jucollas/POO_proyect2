import streamlit as st
import controller.airline_controller as controller

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "aerolinea",
    page_icon = ":toolbox:"
)

st.write( "Aerolineas" )
st.dataframe( controller.get_airlines(), use_container_width = True, column_config = {"":"Nombre aerolinea","value":"vuelos asignados"} )

seleccion = st.radio("¿Que quieres hacer?", [" - ", "Crear Aerolinea", "Eliminar Aerolinea"]);

if ( seleccion ==  "Crear Aerolinea" ) :
    name = st.text_input( "Nombre: ", key ="aeroName" );
    if ( st.button( "Crear" ) ):
        controller.create_airline( name )

elif ( seleccion == "Eliminar Aerolinea"):
    elim = st.selectbox( "¿Cual quieres eliminar?", controller.get_airlines() )
    if ( st.button( "Eliminar" ) ):
        controller.delete_airline( elim );