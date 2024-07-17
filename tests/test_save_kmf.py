#Import Dependencies
import unittest
import sys
import os
#IMPORTANT
sys.path.append('../keras_saver')  # Add keras_saver to the system path

from keras_model_functions import * # type: ignore
#END
import tensorflow as tf

class test_keras_save_model(unittest.TestCase):
    def test_save_model(self):
        print("\nCURRENTLY TESTING SAVING THE MODEL")
        example_model=tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(28,28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        #Save the model in the same folder, and call it 'cnn.[h5 or keras]'
        save_keras_model(example_model)
        does_model_exist=os.path.exists("cnn.h5") or os.path.exists("cnn.keras")
        self.assertEqual(does_model_exist, True)

    def can_load_model(self):
        self.assertEqual(os.path.exists("cnn.keras") or os.path.exists("cnn.h5"), True)

if __name__=="__main__":
    unittest.main()
