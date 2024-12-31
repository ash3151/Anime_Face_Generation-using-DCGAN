from tensorflow.keras.preprocessing.image import array_to_img
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import streamlit as st

generator = load_model('NEW_generator.h5')

def generate_face():
    plt.figure(figsize=(20, 20))
    index = 1
    for i in range(28):
        plt.subplot(7, 7, index)
        
        noise = tf.random.normal([1, 100])
        # fig = plt.figure(figsize=(3, 3))
        g_img = generator(noise)

        g_img = (g_img * 127.5) + 127.5
        g_img.numpy()
        img = array_to_img(g_img[0])
        plt.imshow(img)
        plt.axis('off')
        index += 1
    return plt

st.title("ANIME FACES GENERATION USING DCGAN")
st.subheader("Trained DCGAN model on Anime faces dataset available on Kaggle.")

if st.button("Generate Face"):
    face_image = generate_face()
    st.pyplot(face_image)


st.write(
    "This application uses two Neural Networks called Generator and Discriminator, both are trained simultaneously on batches for 50 epochs."
)