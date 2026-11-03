# Todays Plan Page

import tkinter as tk
import json
import os
from datetime import datetime


class TodaysPlanPage(tk.Frame):

    # Page Initialization
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

        # The state names (Johor, Kedah, ...) are the keys of the JSON.
        self.states = list(self.data.keys())

    def display_widgets(self):
        # Back button
        self.back_button = tk.Button(
            self,
            text="Back to home page",
            font=("Arial", 15, "bold"),
            width=15,
            height=2,
            bg="white",
            command=self.go_back
            )
        self.back_button.pack(padx=10, pady=10)

        # Title/Header
        self.header = tk.Label(
            self,
            text="Today's Plan",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="darkblue"
            )
        self.header.pack(pady=(10, 10))

        # Creates the frame which the dropdown and button will use.
        self.button_frame = tk.Frame(
            self,
            bg="white"
            )

        self.state_label = tk.Label(
            self.button_frame,
            text="Choose your state:",
            font=("Arial", 12),
            bg="white"
            )
        self.state_label.grid(row=0, column=0, padx=10, pady=(0, 5))

        self.selected_state = tk.StringVar(value=self.states[0])
        self.state_menu = tk.OptionMenu(
            self.button_frame,
            self.selected_state,
            *self.states
            )
        self.state_menu.config(
            font=("Arial", 15, "bold"),
            width=20,
            bg="lightblue"
            )
        self.state_menu.grid(row=1, column=0, padx=10, pady=10)

        self.plan_button = tk.Button(
            self.button_frame,
            text="Create Today's Plan",
            font=("Arial", 15, "bold"),
            width=20,
            height=3,
            bg="lightblue",
            command=self.on_click
            )
        self.plan_button.grid(row=2, column=0, padx=10, pady=10)

        self.button_frame.pack()

        self.result_label = tk.Label(
            self,
            text="Choose a state and press Create Today's Plan",
            font=("Arial", 12),
            bg="white",
            justify="left",
            wraplength=420
            )
        self.result_label.pack(pady=10)

        self.hourly_frame = tk.Frame(self, bg="white")
        self.hourly_frame.pack(fill="x", padx=20)

    # Gets the weather of one place for the current hour
    def get_city_data(self, state):
        place = self.data[state]

        # The JSON only has hours 6 to 20, so keep the hour inside that range.
        hour = datetime.now().hour
        if hour < 6:
            hour = 6
        if hour > 20:
            hour = 20

        for entry in place["hours"]:
            if entry["hour"] == hour:
                return {
                    "name": place["city"],
                    "temperature": entry["temp_c"],
                    "humidity": entry["humidity_pct"],
                    "uv_index": entry["uv_index"],
                    "rain_chance": entry["rain_chance_pct"],
                }

    # Calculates how suitable an hour is for outdoor activities.
    def calculate_score(self, entry):
        score = 100
        temperature = entry["temp_c"]

        if temperature < 12:
            score -= (12 - temperature) * 3
        elif temperature > 26:
            score -= (temperature - 26) * 3.5

        score -= entry["rain_chance_pct"] * 0.4
        score -= max(0, entry["uv_index"] - 6) * 2
        return max(0, min(100, int(score)))

    def get_score_color(self, score):
        if score >= 70:
            return "lightgreen"
        if score >= 40:
            return "khaki"
        return "lightcoral"

    # Builds a plan from the best forecast hours.
    def create_plan(self, state):
        place = self.data[state]
        scored_hours = self.score_hours(state)
        scored_hours.sort(key=lambda item: item[1], reverse=True)

        best_entry, best_score = scored_hours[0]
        best_hour = best_entry["hour"]
        plan = (
            f"{place['city']} today's plan\n"
            f"Best time for outdoor activities: {best_hour:02d}:00 "
            f"(Score: {best_score}/100)"
        )

        return plan

    def score_hours(self, state):
        return [
            (entry, self.calculate_score(entry))
            for entry in self.data[state]["hours"]
        ]

    def display_hourly_scores(self, state):
        for widget in self.hourly_frame.winfo_children():
            widget.destroy()

        legend = tk.Label(
            self.hourly_frame,
            text="Green: good   Yellow: moderate   Red: poor",
            font=("Arial", 10),
            bg="white"
            )
        legend.pack(pady=(0, 5))

        for entry, score in self.score_hours(state):
            row = tk.Label(
                self.hourly_frame,
                text=(
                    f"{entry['hour']:02d}:00   "
                    f"{entry['temp_c']}°C   "
                    f"Rain {entry['rain_chance_pct']}%   "
                    f"Score {score}/100"
                ),
                font=("Arial", 11, "bold"),
                bg=self.get_score_color(score),
                anchor="w",
                padx=8,
                pady=3
                )
            row.pack(fill="x", pady=1)

    def on_click(self):
        state = self.selected_state.get()
        self.result_label.config(text=self.create_plan(state))
        self.display_hourly_scores(state)

    # Goes back to home page
    def go_back(self):
        self.app.show_page("home")
