import streamlit as st
from streamlit_option_menu import option_menu
import pickle as pkl
import numpy as np

# st.title('Crop Recommender')

# loading the saved models
crop_model = pkl.load(open('crop_model_nb.pkl', 'rb'))
crop_names = ['rice',
 'maize',
 'chickpea',
 'kidneybeans',
 'pigeonpeas',
 'mothbeans',
 'mungbean',
 'blackgram',
 'lentil',
 'pomegranate',
 'banana',
 'mango',
 'grapes',
 'watermelon',
 'muskmelon',
 'apple',
 'orange',
 'papaya',
 'coconut',
 'cotton',
 'jute',
 'coffee']

with st.sidebar:
    selected = option_menu('AgriGuide',
                           ['Home', 'Crop Recommender'],
                           icons = ['house-fill', 'tree-fill'],
                           menu_icon = 'bi bi-chevron-double-down',
                           default_index = 0)

# Home
if selected == 'Home':
    st.title('AgriGuide: Your Smart Agriculture Companion')
    app_intro = """
        ## About AgriGuide

        AgriGuide, born out of a passion for innovation in agriculture, is not just a college project — it's a 
        vision for the future of farming. Developed as part of a college endeavor, AgriGuide aims to address the 
        unique challenges faced by farmers using the power of machine learning.

        ## How AgriGuide Works

        This college project harnesses the potential of machine learning to analyze diverse data sets, including 
        soil health, climate conditions, and historical crop performance. AgriGuide offers a glimpse into the future 
        of precision farming, making informed decisions accessible to all.

        ## Key Features

        ### 1. Precision Recommendations:
        AgriGuide, crafted with dedication as a college project, provides precise and personalized crop recommendations, 
        tailoring suggestions to your unique farming conditions.

        ### 2. User-Friendly Interface:
        AgriGuide, a labor of love in the college realm, boasts an intuitive interface designed to make the power of 
        precision agriculture accessible to all farmers.
        """
    st.markdown(app_intro)

# Diabetes Prediction page
if selected == 'Crop Recommender':
    # page title
    st.title('Crop Recommender')
    # asking details for prediction
    col1, col2, col3 = st.columns(3)
    with col1:
        nitrogen = st.number_input('Enter the nitrogen content (%)')
    with col2:
        phosphorus = st.number_input('Enter the phosphorus content (%)')
    with col3:
        potassium = st.number_input('Enter the potassium content (%)')
    with col1:
        temp = st.number_input('Enter the temperature in celsius')
    with col2:
        humidity = st.number_input('Enter the humidity (%)')
    with col3:
        ph = st.number_input('Enter the ph')
    with col1:
        rain = st.number_input('Enter the rainfall (mm)')
    # processing the features
    features = [nitrogen, phosphorus, potassium, temp, humidity, ph, rain]
    features = np.array(features)
    # making the prediction
    crop = ''
    if st.button('Recommend'):
        crop_pred_ind = crop_model.predict([features])
        crop = 'We recommend ' + crop_names[crop_pred_ind[0]] + ' crop.'
    st.write(crop)