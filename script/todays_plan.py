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
        self.hello_world = tk.Label(
            self,
            text="Hello World"
        )
        self.hello_world.pack(pady=(10,10))

