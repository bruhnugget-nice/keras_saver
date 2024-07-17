"""
This file implements some basic functions for saving and loading keras models, 
which should prove to be useful when building the custom-tkinter windows.
"""

#Importing the Libraries
import tensorflow as tf
import re
import os

def save_keras_model(model):
    """
    Args:
        model (tf.keras.Sequential):
    
    Desc:
    Uses the command line to ask the user to save a file in either a .h5 or .keras file.
    """

    #Setting Up the Regex, this will be referenced later.
    regex=".*.keras|h5"

    #Checking for model type
    if type(model)!=tf.keras.Sequential:
        raise TypeError("\nThis model is not a Keras Sequential Model, try again!")
    

    for i in range(3):
        model_path=input("\n\nWhere would you like to save this file?\n(to exit, type in 'exit', and if testing, save this as cnn.[h5 or keras]). ")
        regex_match=re.search(regex, model_path)
        path_does_not_exist=os.path.exists(model_path)==False

        if model_path=="exit":
            break
        elif regex_match and path_does_not_exist:
            model.save(model_path)
            print(f"\nYour model is saved to {model_path}, store this path in a variable.")
            break
        elif regex_match and path_does_not_exist==False:
            print(f"\nThis path({model_path}) is already taken up, choose a different path.")
        else:
            print("\nUh oh! Your file path should end in .h5 or .keras.")

def load_keras_model(model_path):
    """
    Args:
        model_path (str):

    Desc:
    Takes in a path to a .h5 or .keras model and returns the loaded model.
    """
    if os.path.exists(model_path):
        # Get User Input
        return tf.keras.models.load_model(model_path)
    else:
        print("\nYour model path does not exist, or your path does not lead to a model.")
        print("Make sure your path ends in .h5 or .keras.")