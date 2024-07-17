from keras_model_functions import *
from base_window import *
import customtkinter as ctk
import tensorflow as tf
from tkinter import filedialog
import numpy as np
import imageio
import sys

#Helper Functions
def term_process():
    sys.exit(0)

def model_predict(model: tf.keras.Sequential, pred_label: ctk.CTkLabel, class_names):
    #Read the file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;")])
    file_path.replace("\\", "/")
    print(f"Your file path is: {file_path}")
    img = imageio.imread(file_path)
    img=tf.stack([img]*3, axis=-1)
    img=tf.expand_dims(img, axis=0)
    pred_arr=model.predict(img)
    pred_argmax=np.argmax(pred_arr)
    pred_text=class_names[int(pred_argmax)]
    pred_label["text"]="My prediction is..." + str(pred_text)
    print("My prediction is..." + str(pred_text))




def create_keras_window(model_path, class_names_arr, title="Keras Saver", geo_size="420x420"):
    """
    Description of create_keras_window

    Args:
        model_path (str):
        *elements (args):

    Creates a customizable window for loading in and using keras models.
    """
    #Set up the model
    new_model=load_keras_model(model_path)


    #Set up window
    bw=base_window()
    bw.set_geometry(geo_size)
    bw.root.title(title)

    #Set up the elements
    top_label=ctk.CTkLabel(master=bw.root, text="Keras Saver", font=('Arial', 40, 'bold'))
    predict_label=ctk.CTkLabel(master=bw.root, text="") #REDUNANT, TBD
    input_button=ctk.CTkButton(master=bw.root, text="Browse For Input", command=lambda: model_predict(model=new_model, pred_label=predict_label, class_names=class_names_arr))
    bw.set_elements(top_label, input_button, predict_label)

    #Get Array for element placing
    geo_list=geo_size.split("x")
    geo_list=[int(i) for i in geo_list]

    #Place the Elements
    bw.place_elements([
        [geo_list[0]/3.75,geo_list[1]/10],
        [geo_list[0]/2.6,geo_list[1]/2], #1st label(real)
        [geo_list[0]/2.75,geo_list[1]/3],
    ])

    bw.root.protocol("WM_DELETE_WINDOW", lambda: term_process())
    #Start mainloop
    bw.start()

    