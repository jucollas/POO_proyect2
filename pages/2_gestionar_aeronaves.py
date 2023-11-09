import streamlit as st
from controller.aircraft_controller import AircraftController

controller = AircraftController()

#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "Aeronaves",
    page_icon = ":toolbox:"
)

st.write( "Aeronaves" );

st.dataframe( controller.get_aircrafts(), use_container_width = True, hide_index = True, column_config = {
    1:"Numero de serie", 2:"Marca",3:"Modelo",4:"Año produccion",5:"Capacidad pasajeros",6:"Velocidad Maxima",7:"Autonomia",8:"Vuelos Asociados", 9:"En Vuelo", 10:"En Mantenimiento", 11 :"¿se puede asignar vuelos?"
    } );

seleccion = st.radio("¿Que quieres hacer?", [" - ", "Crear Aeronave", "Eliminar Aeronave", "Mantenimiento"]);


if ( seleccion ==  "Crear Aeronave" ) :
    nRotors, liftingCapacity, specificUse, heightMax, nEngines, category, cedula, name, surname, birthDate, genre, address, phoneNumber, email = None, None, None, None, None, None, None, None, None, None, None, None, None, None
    st.write( "Crear Aeronave" )
    aircraftType = st.selectbox( "Elige el tipo de aeronave que deseas", ["Helicoptero", "Avion", "Jet"] );
    n_number = st.text_input( "Numero de serie: ", key ="serie" );
    brand = st.text_input( "Marca: ", key ="marca")
    model = st.text_input( "Modelo: ", key ="modelo" );
    yearProduction = str(st.number_input( "Año de producion: ", key = "añoProduccion", min_value=1970, max_value=2023, step=1 )) # modificar con el año actual
    abilityPass = st.number_input( "Capacidad de pasajeros: ",key = "abilityPass", min_value=0, step=1 )
    speedMax = st.number_input( "Velocidad Maxima (km/h): ", key = "speedMax", min_value=0, step=1 )
    autonomy = st.number_input( "Autonomia (km): ", key = "autonomy", min_value=0, step=1 )
    if ( aircraftType == "Helicoptero" ):
        nRotors = st.number_input( "Cantidad de rotores: ", key = "nRotors", min_value=0, step=1 )
        liftingCapacity = st.number_input( "Capacidad de levantar (ton): ", key = "liftingCapacity", min_value=0, step=1 )
        specificUse = st.selectbox( "Uso: ", ["Comercial", "Privado", "Rescate"] )#no me acuerdo
    elif ( aircraftType == "Avion" ):
        heightMax = st.number_input( "Altura Maxima (pies): ", key = "heightMax", min_value=0, step=1 )
        nEngines = st.number_input( "Cantidad de motores: ", key ="nEngines", min_value=0, step=1  )
        category = st.selectbox( "Categoria: ", ["comercial", "carga", "bombardeo"] )
    elif ( aircraftType == "Jet" ):
        st.write( "Escribe la informacion del propietario del jet:" );
        cedula = st.text_input( "Cedula: ", key = "cedula" )
        name = st.text_input( "Nombre: ", key = "name" )
        surname = st.text_input( "Apellido: ", key = "surname" )
        birthDate = st.date_input( "Fecha de Nacimiento: " );
        genre = st.selectbox( "Genero: ", ["Masculino", "Femenino", "Otro"] )
        address = st.text_input( "Direccion: ", key = "address" )
        phoneNumber = st.text_input( "Numero de telefono: ", key = "phoneNumber" )
        email = st.text_input( "Correo: ", key = "Correo" )

    if ( st.button("Crear") ):
        controller.create_aircraft( aircraftType, n_number, brand, model, yearProduction, abilityPass, speedMax, autonomy, nRotors, liftingCapacity, specificUse, cedula, name, surname, birthDate, genre, address, phoneNumber, email, heightMax, nEngines, category );
elif ( seleccion == "Eliminar Aeronave" ):
    elim = st.selectbox( "¿Cual quieres eliminar?", controller.get_deletable_aircrafts() )
    if ( st.button( "Eliminar" ) ):
        controller.delete_aircraft( elim );
elif ( seleccion == "Mantenimiento" ):
    craft = st.selectbox( "¿Cual quieres poner/quitar de mantenimiento?", controller.get_manteinable_aircrafts() );
    manteinance = st.toggle( "Mantenimiento", value = controller.get_aircraft_manteinanceInfo( craft ) );
    if ( st.button( "Realizar Cambio" ) ):
        controller.change_manteinance( craft, manteinance );
