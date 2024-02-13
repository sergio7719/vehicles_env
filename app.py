import pandas as pd
import plotly.express as px
import streamlit as st
import time

st.title(":blue[Vehicles data view]  :car:  🛠️ ")


      
vehicles_data = pd.read_csv('notebooks\vehicles_us.csv') # importacon de los datos


with st.status("Loading data..."):
        time.sleep(2)



# Se crea un boton

vehicles_info = st.checkbox('information is displayed') 

if vehicles_info:
        st.write(vehicles_data.head(10))


st.button("Return")


st.subheader("Car performance information by mileage")


# Se crea un boton
hist_button = st.button('Show histogram') 

if hist_button: # al hacer clic en el botón
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
#crear un histograma
fig = px.histogram(vehicles_data, x="odometer", y = 'type')
        
#mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True) 


st.subheader("price per car model")

price_info = st.button('information is displayed') 

if price_info:
        st.warning('Price and model scatter plot is created')


fig = px.scatter(vehicles_data, x="model", y="price") # crear un gráfico de dispersión
fig.show() # crear gráfico de dispersión 
