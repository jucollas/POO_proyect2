import streamlit as st
from controller.airport_controller import Airport_Controller
from view.view_admin import create_crew

# Definir una función para el menú de administrador
def admin_menu():
    controller = Airport_Controller()
    st.subheader("Menú de Administrador")
    admin_option = st.selectbox("Selecciona una opción:", ["Administrar Aeronave", "Administrar Vuelos", "Administrar Tripulación", "Administrar Puertas de Abordaje"])
    if admin_option == "Administrar Aeronave":
        # Lógica para administrar aeronaves
        st.write("Aquí puedes administrar aeronaves.")
    elif admin_option == "Administrar Vuelos":
        # Lógica para administrar vuelos
        st.write("Aquí puedes administrar vuelos.")
    elif admin_option == "Administrar Tripulación":
        # Lógica para administrar tripulación
        create_crew(controller)
        st.write("Aquí puedes administrar la tripulación.")
    elif admin_option == "Administrar Puertas de Abordaje":
        # Lógica para administrar puertas de abordaje
        st.write("Aquí puedes administrar las puertas de abordaje.")

# Definir una función para el menú de cliente
def client_menu():
    controller = Airport_Controller()
    st.subheader("Menú de Cliente")
    client_option = st.selectbox("Selecciona una opción:", ["Administrar Cliente", "Comprar Vuelos", "Filtrar Vuelos"])
    if client_option == "Administrar Cliente":
        #create_person(controller)
        st.write("Aquí puedes administrar tus datos de cliente.")
    elif client_option == "Comprar Vuelos":
        # Lógica para comprar vuelos
        st.write("Aquí puedes comprar vuelos.")
    elif client_option == "Filtrar Vuelos":
        # Lógica para filtrar vuelos
        st.write("Aquí puedes filtrar vuelos disponibles.")



#configura el logo que aparece junto al boton de cerrar la camara
st.set_page_config(
    page_title = "aeropuerto",
    page_icon = ":airplane_departure:"
)

# Configurar el título de la aplicación
st.sidebar.title('Menú del Aeropuerto')

# Determinar si el usuario es administrador o cliente (simulado aquí por simplicidad)
user_type = st.sidebar.radio("¿Eres un administrador o un cliente?", ["Administrador", "Cliente"])

if user_type == "Administrador":
    admin_menu()
else:
    client_menu()
