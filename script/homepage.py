# THIS IS THE FIRST / HOMEPAGE OF THE PROGRAM

import tkinter as tk

class WeatherApp:

    # App Initialization
    def __init__(self):
        self.window = tk.Tk()
        self.display_widgets()

    # Display Widgets
    def display_widgets(self):
        self.window.title("Weather Planner App")
        self.window.geometry("500x500")
        self.window.configure(bg="white")

        # Title/Header
        self.header = tk.Label(
            self.window, 
            text="Welcome to Weather Planner App",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="darkblue"
            )
        self.header.pack(pady=(10,10))

        # Creates The frame which the buttons will stay
        self.button_frame = tk.Frame(
            self.window,
            bg="white"
            )

        # All the buttons
        self.todays_plan = tk.Button(
            self.button_frame, 
            text="Todays Plan", 
            font=("Arial", 15, "bold"),
            width=20, 
            height=3,
            bg="lightblue"
            )
        self.todays_plan.grid(row=0, column=0, padx=10, pady=10)

        self.activity_advisor = tk.Button(
            self.button_frame, 
            text="Activity Advisor", 
            font=("Arial", 15, "bold"),
            width=20, 
            height=3,
            bg="lightblue"
            )
        self.activity_advisor.grid(row=1, column=0, padx=10, pady=10)

        self.hydration_safety = tk.Button(
            self.button_frame, 
            text="Hydration & Safety",
            font=("Arial", 15, "bold"),
            width=20, 
            height=3,
            bg="lightblue"
            )
        self.hydration_safety.grid(row=2, column=0, padx=10, pady=10)

        self.city_compare = tk.Button(
            self.button_frame, 
            text="City Compare", 
            font=("Arial", 15, "bold"),
            width=20,
            height=3,
            bg="lightblue"
            )
        self.city_compare.grid(row=3, column=0, padx=10, pady=10)

        self.exit = tk.Button(
            self.button_frame, 
            text="exit", 
            font=("Arial", 15, "bold"),
            width=20, 
            height=3,
            bg="lightblue"
            )
        self.exit.grid(row=4, column=0, padx=10, pady=10)

        # Packs all buttons 
        self.button_frame.pack()

    # Adds event listener to the buttons
    def on_click(self):
        ...

    # Runs the program when called
    def run(self):
        self.window.mainloop()     

if __name__ == "__main__":
    app = WeatherApp()
    app.run()