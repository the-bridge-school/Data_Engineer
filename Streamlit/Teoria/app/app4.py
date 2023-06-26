import streamlit as st
from PIL import Image

#Insert a picture
# First, read it with PIL
image = Image.open(r'Streamlit\Teoria\img\591e3af95df3c.jpeg')
image2 = Image.open(r'Streamlit\Teoria\img\images.jpg')
# Load Image in the App
st.image(image)
st.image(image2)