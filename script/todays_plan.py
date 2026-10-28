# Todays Plan Page

import tkinter as tk 
import json
import os
from datetime import datetime

class TodaysPlanPage(tk.Frame):

    # Initialization
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app
        self.load_data()
        self.display_widgets()
    
    # Loads weather database
    def load_data(self):
        folder = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(folder, "..", "database", "malaysia_weather.json")

        with open(path, "r", encoding="utf-8") as file:
            self.data = json.load(file)

        # The state names (Johor, Kedah, ...) are the keys of the json
        self.states = list(self.data.keys())
    
    def display_widgets(self):
        # Creates frame for back button
        self.back_button_frame = tk.Frame(
            self,
            bg="white"
            )

        # Back button (goes back to the home page)
        self.back_button = tk.Button(
            self.back_button_frame,
            text="Back to home page",
            font=("Arial", 15, "bold"),
            width=15,
            height=2,
            bg="white",
            command=self.go_back
            )
        self.back_button.grid(row=0, column=0, padx=10, pady=10)

        # Packs back button frame
        self.back_button_frame.pack()

        # Title/Header
        self.header = tk.Label(
            self,
            text="Today's Plan",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="darkblue"
            )
        self.header.pack(pady=(10,10))

        # Creates The frame which the dropdowns and buttons will stay
        self.button_frame = tk.Frame(
            self,
            bg="white"
            )

    def on_click(self):
        ...

    # Goes back to home page
    def go_back(self):
        self.app.show_page("home")
