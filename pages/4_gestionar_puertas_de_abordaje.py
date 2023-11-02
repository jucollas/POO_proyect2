import streamlit as st
from controller.boardingGate_controller import BoardingGate_Controller

controller = BoardingGate_Controller()

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "abordaje",
    page_icon = ":toolbox:"
)

city = st.selectbox( "¿Cual aeropuerto quieres visualizar?", controller.get_cities() )

st.write( "\nPuertas de abordaje" );

st.dataframe( controller.get_boardingGates( city ), use_container_width = True, column_config = { 1:"Identificacion", 2:"Ubicacion", 3:"Vuelo asignado", 4:"Historial" }, hide_index = True );

#nota, no se si lo del historial esta bien manejado

seleccion = st.radio("¿Que quieres hacer?", [" - ", "Crear Puerta de Abordaje", "Eliminar Puerta de Abordaje"]);


if ( seleccion ==  "Crear Puerta de Abordaje" and city is not None ) :
    with st.form( "Crear Puerta de Abordaje" ):
        identification = st.text_input( "Identificacion: ", key ="idName" );
        location = st.text_input( "Location: ", key ="locationName" );
        if ( st.form_submit_button("Crear") ):
            controller.create_boardingGate( city, identification, location );
elif ( seleccion == "Eliminar Puerta de Abordaje" and city is not None ):
    elim = st.selectbox( "¿Cual quieres eliminar?", controller.get_deletable_gates( city ) )
    if ( st.button( "Eliminar" ) ):
        controller.delete_boardingGate( city, elim );
