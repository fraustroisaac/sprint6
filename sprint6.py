import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.title("Comportamiento de los precios de marcas de automóviles")

hist_button = st.button('Construir histograma') # crear un botón
disp_button = st.button('Diagrama de dispersión odometer vs price')
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de dispersión de odometer vs price')
            
    # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig2) # crear gráfico de dispersión
