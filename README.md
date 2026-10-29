# Weather App Planner 

### Pages:
1. Homepage
2. Activity Advisor
3. City Compare
4. Hydration Safety
5. Todays Plan

#

### Features:

1. **Todays Plan Page**: 
Input city -> Fetch forecast -> Score each hour ->
Score each hour -> Show Planner

2. **Activity Advisor**: 
Input city -> Fetch forecast
-> Apply limit -> Safe Window -> Show advice

3. **Hydration And Safety**:
Input city -> Fetch forecast -> Find peak heat ->
Set Advice -> Show water goal

4. **City Compare**:
Add city -> Fetch forecast -> Score each city ->
Rank cities -> Show comparison

#

### Weather Database:

(NOTE: the database is hardcoded instead of fetching actual up-to-date weather data)

The weather database is kept in a JSON file inside `./database`.

Since weather database will only display weather forecast from the 6th hour to 20th hour,
each program will import the datetime module to get the current hour and fetch the weather forecast based on that hour.

### How to run:

1. Open `./script/homepage.py` (Entry Point)
2. Run `python homepage.py` in the terminal 