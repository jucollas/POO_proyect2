import streamlit as st

def board_flight_client(flights : list[tuple[str]]) -> None:
    print(flights)
    st.dataframe( flights, hide_index = True, column_config = {
        1 : "Codigo de vuelo", 2 : "Fecha", 3 : "Origen", 4 : "Llegada", 5: "Serie aeronave", 6 : "Asientos", 7 : "En el aire"
        } )