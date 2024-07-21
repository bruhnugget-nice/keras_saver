import customtkinter as ctk
import tkinter as tk

class base_window():
    root=ctk.CTk()
    def __init__(self):
        """
        Sets the window up.
        """
        print(f"You have created a window from class {__name__}")

    def set_geometry(self, geo_str):
        """
        Description of set_geometry

        Args:
            self (customtkinter.CTk):
            geo_str (str):
        Sets the customtkinter window size.
        """
        self.root.geometry(geo_str)

    def set_icon(self, icon_path):
        """
        Description of set_icon

        Args:
            self (customtkinter.CTk):
            icon_path (str):

        Takes in an image path and sets the tkinter window as it.
        """
        icon=tk.PhotoImage(icon_path)
        self.root.iconphoto(True, icon)

    def set_elements(self, *elements):
        """
        Description of setElements

        Args:
            self (customtkinter.CTk):
            *elements (args):

        Given customtkinter widgets, this will set the widgets onto the window before placing them with place_elements.      
        """
        self.elements=elements
        print(elements)
        return self
    def place_elements(self, coordsList):
        """
        Description of placeElements

        Args:
            self (customtkinter.CTk):
            coordsList (2D list):

        Takes in a 2D array to place elements set on the base window.
        """
        #Check for list type
        if type(self.elements)==tuple and type(coordsList)==list:
            for pairIndice in range(len(coordsList)):
                self.elements[pairIndice].place(x=coordsList[pairIndice][0], y=coordsList[pairIndice][1])
        else:
            raise TypeError("You need to pass in a 2D list for this function to work.")
            
        return self
    
    def start(self):
        """
        Description of start

        Args:
            self (customtkinter.CTk):

        Starts the window displaying on the screen.
        """
        self.root.mainloop()