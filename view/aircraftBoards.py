from controller.aircraft_controller import AircraftController
import streamlit as st
import datetime

def allInfoAircraft(data : dict[str : any]) -> None:

    if "owner" in data:
        st.write("Datos del propietario:")
        owner = data["owner"]
        owner["birthDate"] = owner["birthDate"].strftime("%Y-%m-%d")
        st.json(owner)
        data.pop("owner")

    st.write("Datos de la Aeronave:")
    st.json(data)

    