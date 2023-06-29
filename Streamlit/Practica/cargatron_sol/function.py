# importar librerias
import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components

# configuracion de la pagina
def config_page():
    st.set_page_config(
        page_title = 'Cargatron',
        page_icon = ':electric_plug:',
        layout = 'wide'
    )

# cache
st.cache(suppress_st_warning=True)
# cargar los datos

def cargar_datos(path):
    df = pd.read_csv(path)
    return df

# HOME
def home(df):
    img = Image.open('puntos-recarga-madrid.jpg')
    st.image(img, use_column_width ='auto')
    with st.expander('¿Quieres saber más?'):
        st.write('Es una solución factible para el aumento del cambio climático')
        
# DATOS
def datos(df):
    st.write(df)
    st.table(df)
    st.map(df) # latitude, longitude, LAT, LON
    filehtml = open('mapa.html','r')
    sc= filehtml.read()
    components.html(sc, height = 700)

    nc_distrito = df.groupby('DISTRITO')['Nº CARGADORES'].sum()
    st.write(nc_distrito)
    st.bar_chart(nc_distrito)

    nc_op = df.groupby('OPERADOR')['Nº CARGADORES'].sum()
    st.write(nc_op)
    st.line_chart(nc_op)
# FILTROS
def filtros(df):
    st.write(df)
    lista_dis = list(df['DISTRITO'].unique())
    filtro_dis = st.sidebar.selectbox('Selecciona un distrito', lista_dis)
    df = df[df['DISTRITO'] == filtro_dis]
    st.write(df)
    st.sidebar.write('Selecciona por operador o por nº de cargadores')
    check_op = st.sidebar.checkbox('Filtrar por operador')
    check_nc = st.sidebar.checkbox('Filtrar por nº de cargadores')

    if check_op & check_nc:
        st.error('Solo puedes filtrar por una de las dos opciones')
    elif check_op:
        lista_op = list(df['OPERADOR'].unique())
        filtro_op = st.sidebar.selectbox('Selecciona un operador', lista_op)
        df = df[df['OPERADOR'] == filtro_op]
        st.write(df)
    elif check_nc:
         c_min = df['Nº CARGADORES'].min()
         c_max = df['Nº CARGADORES'].max()

         if c_min != c_max:
             intervalo = range(c_min, c_max+1)
             filtro_nc = st.sidebar.select_slider('Selecciona el intervalo de nº de cargadores', 
             intervalo,value = (c_min,c_max))
             mask1 = df['Nº CARGADORES']>= filtro_nc[0]
             mask2 = df['Nº CARGADORES'] <= filtro_nc[1]
             df = df[mask1&mask2]
             st.write(df)
             st.sidebar.radio('selecciona una opcion', ('1','2'))

    else: 
        pass

    col1, col2 = st.columns(2)

    with col1:
        zoom = 13
        st.map(df, zoom)

    with col2:
        st.table(df[['DIRECCION','EMPLAZAMIENTO','Nº CARGADORES']])