import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
from geopy.geocoders import OpenCage
from geopy.exc import GeocoderUnavailable, GeocoderTimedOut

st.title("Healthcare Provider Locator")

# Initialize session state variables
if "grouped_data" not in st.session_state:
    st.session_state.grouped_data = None
if "npi_locations" not in st.session_state:
    st.session_state.npi_locations = None
if "map" not in st.session_state:
    st.session_state.map = folium.Map(location=[37.0902, -95.7129], zoom_start=5)  # Default US Map

# Replace with your OpenCage API key
OPENCAGE_API_KEY = "a5d4bef1afeb499292bbeaaf1a21eff0"

# Display Map
folium_static(st.session_state.map)

# Input for MSA Code
msa = st.text_input("Enter MSA Code:")

if st.button("Get Providers"):
    if msa:
        response = requests.get(f"http://127.0.0.1:8000/get_npi/{msa}")

        if response.status_code == 200:
            data = response.json()
            st.session_state.grouped_data = data.get("grouped_npi", {})
            st.session_state.npi_locations = data.get("npi_locations", {})

            st.write("### Grouped Data:")
            st.json(st.session_state.grouped_data)

            # Update Map with Providers
            st.session_state.map = folium.Map(location=[37.0902, -95.7129], zoom_start=5)
            geolocator = OpenCage(api_key=OPENCAGE_API_KEY, timeout=10)

            for address, providers in st.session_state.grouped_data.items():
                try:
                    location = geolocator.geocode(address)
                    if location:
                        for provider in providers:
                            name = provider["Name"]
                            city = provider["City"]
                            state = provider["State"]
                            popup_text = f"{name} ({city}, {state})"
                            folium.Marker([location.latitude, location.longitude], popup=popup_text).add_to(st.session_state.map)
                except (GeocoderUnavailable, GeocoderTimedOut):
                    st.warning(f"Geocoding failed for address: {address}")

            folium_static(st.session_state.map)  # Update Map
        else:
            st.error("Failed to fetch data!")
    else:
        st.warning("Please enter an MSA code!")

# # Input for NPI Number (This remains visible)
# npi = st.text_input("Enter NPI Number:")

# if st.button("Get NPI Locations"):
#     if npi:
#         response = requests.get(f"http://127.0.0.1:8000/get_npi_location/{npi}")

#         if response.status_code == 200:
#             locations = response.json().get("locations", [])

#             if locations:
#                 st.write("### Locations for NPI:")
#                 st.json(locations)

#                 # Update Map with NPI Locations
#                 st.session_state.map = folium.Map(location=[37.0902, -95.7129], zoom_start=5)
#                 geolocator = OpenCage(api_key=OPENCAGE_API_KEY, timeout=10)

#                 for address in locations:
#                     try:
#                         location = geolocator.geocode(address)
#                         if location:
#                             folium.Marker(
#                                 [location.latitude, location.longitude],
#                                 popup=f"NPI {npi} - {address}"
#                             ).add_to(st.session_state.map)
#                     except (GeocoderUnavailable, GeocoderTimedOut):
#                         st.warning(f"Geocoding failed for address: {address}")

#                 folium_static(st.session_state.map)  # Update Map
#             else:
#                 st.warning("No locations found for this NPI number!")
#         else:
#             st.error("Failed to fetch NPI data!")
#     else:
#         st.warning("Please enter an NPI number!")
