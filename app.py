import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Vehicles data view")
        
vehicles_data = pd.read_csv('vehicles_us.csv') # importacon de los datos


@st.cache_data

def load_data(nrows):
    data = pd.read_csv(vehicles_data, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Se crea una etiqueta de cargando info
data_load_state = st.text('Loading data...')


#Aqui se cargan solo 10000 registros de todo el archivo

data = load_data(100)

#Se crea una etiqueta en donde indique que la carga del archivo fue correcta

data_load_state.text("Done! (using st.cache_data)")


hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(vehicles_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)