import streamlit as st
import controller.aircraft_controller as controller

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "aeronaves",
    page_icon = ":toolbox:"
)

st.write( "Aeronaves" );

st.dataframe( controller.get_aircrafts(), use_container_width = True, hide_index = True, column_config = {
    1:"Numero de serie", 2:"Marca",3:"Modelo",4:"Año de produccion",5:"Capacidad de pasajeros",6:"Velocidad Maxima",7:"Autonomia",8:"Vuelos Asociados", 9:"En Vuelo", 10:"En Mantenimiento"
    } );

seleccion = st.radio("¿Que quieres hacer?", [" - ", "Crear Aeronave", "Eliminar Aeronave", "Mantenimiento"]);


if ( seleccion ==  "Crear Aeronave" ) :
    nRotors, liftingCapacity, specificUse, heightMax, nEngines, category, owner = None, None, None, None, None, None, None
    st.write( "Crear Aeronave" )
    aircaftType = st.selectbox( "Elige el tipo de aeronave que deseas", ["Helicoptero", "Avion", "Jet"] );
    n_number = st.text_input( "Numero de serie: ", key ="serie" );
    brand = st.text_input( "Marca: ", key ="marca")
    model = st.text_input( "Modelo: ", key ="modelo" );
    yearProduction = str(st.number_input( "Año de producion: ", key = "añoProduccion" ))
    abilityPass = st.number_input( "Capacidad de pasajeros: ",key = "abilityPass" );
    speedMax = st.number_input( "Velocidad Maxima: ", key = "speedMax" );
    autonomy = st.number_input( "Autonomia: ", key = "autonomy" );
    if ( aircaftType == "Helicoptero" ):
        nRotors = st.number_input( "Cantidad de rotores: ", key = "nRotors" )
        liftingCapacity = st.number_input( "Capacidad de levantar: ", key = "liftingCapacity" )
        specificUse = st.selectbox( "Uso: ", ["Comercial", "Privado", "Salvar vidas"] )#no me acuerdo
    elif ( aircaftType == "Avion" ):
        heightMax = st.number_input( "Altura Maxima: ", key = "heightMax" )
        nEngines = st.number_input( "Cantidad de motores: ", key ="nEngines" )
        category = st.selectbox( "Categoria: ", ["comercial", "carga", "bombardeo"] )
    elif ( aircraftType == "Jet" ):
        owner = None
    if ( st.button("Crear") ):
        controller.create_aircraft( aircaftType, n_number, brand, model, yearProduction, abilityPass, speedMax, autonomy, nRotors, liftingCapacity, specificUse, owner, heightMax, nEngines, category );
elif ( seleccion == "Eliminar Aeronave_" ):
    elim = st.selectbox( "¿Cual quieres eliminar?", controller.get_deletable_gates( city ) )
    if ( st.button( "Eliminar" ) ):
        controller.delete_boardingGate( city, elim );
elif ( seleccion == "Mantenimiento_" ):
    pass