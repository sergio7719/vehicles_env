import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Vehicles data view")


      
vehicles_data = pd.read_csv('notebooks\\vehicles_us.csv') # importacon de los datos

data_state = st.text('Loading data...')

st.write(vehicles_data.head(10))

data_state.text("Done! ")

#Se crea boton 
if hist_button: 
    st.write("Histograma para la venta de autos")


#Se crea un histograma

fig = px.histogram(vehicles_data, x = 'odometer')

st.plotly_chart(fig, use_container_width= True)