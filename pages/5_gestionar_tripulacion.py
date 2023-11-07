import streamlit as st
from controller.crew_controller import CrewController
from view.forms import crewForm

controller = CrewController()

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "Tripulacion",
    page_icon = ":toolbox:"
)

st.dataframe( controller.get_crewMembers(), use_container_width = True, hide_index = True, column_config = {
    1 : "Cedula", 2 : "Nombre", 3 : "Appellido", 4 : "Fecha de Nacimiento", 5 : "Genero", 6 : "Direccion", 
    7 : "telefono", 8 : "Correo", 9 : "Trabajo", 10 : "Horas diarias de Trabajo", 11 : "Años de experiencia"
    } )

seleccion = st.radio("¿Que quieres hacer?", [" - ", "Crear Miembro de la Tripulacion", "Eliminar Miembro de la Tripulacion"] );
if ( seleccion == "Crear Miembro de la Tripulacion" ):
    crewForm( controller, "Crear tripulante" )
elif ( seleccion == "Eliminar Miembro de la Tripulacion" ):
    elim = st.selectbox( "¿Cual quieres eliminar?", controller.get_crew_id() )
    if ( st.button( "Eliminar" ) ):
        controller.delete_crewMember( elim );
