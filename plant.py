import streamlit as st
import tensorflow as tf
import pickle
import numpy as np 


# Load the model
model = tf.keras.models.load_model('model.keras')

#class name
class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
   
def prediction(images):
    #get the max index 
    prediction_idx = np.argmax(model.predict(images))
    #convet this array in batch
    print(prediction_idx)
    return class_name[prediction_idx]

st.title("Crop Disease Prediction")

uploaded_file = st.file_uploader("Choose an image...", type="jpg", key="image")



if uploaded_file is not None:
    # Convert the file to an image array
    image = tf.keras.preprocessing.image.load_img( uploaded_file , target_size =(256,256))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.array([image])
    predicted_class = prediction(image)
    st.write("Predicted class:", predicted_class)
else:
    st.write("Please upload an image file")