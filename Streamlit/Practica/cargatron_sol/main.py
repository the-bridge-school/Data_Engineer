# pip install streamlit
# pip install Pillow

# importar librerias
import streamlit as st
import function as ft

# configurar la pagina
ft.config_page()
# cargar los datos
path = 'red_recarga_2021.csv'
df = ft.cargar_datos(path)

st.title('CARGATRON')

# menu
menu = st.sidebar.selectbox('Selecciona menu', ['Home','Datos','Filtro'])

if menu == 'Home':
    ft.home(df)
elif menu == 'Datos':
    ft.datos(df)
else:
    ft.filtros(df)