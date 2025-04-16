# Mile to Km Converter

## Description

This is a simple graphical user interface (GUI) application built with Python's Tkinter library that allows users to convert distances from miles to kilometers. Users can input a value in miles, and by clicking a button, the application will display the equivalent distance in kilometers.

## How to Use

1.  **Run the script:** Execute the Python script. A window titled "Mile to Km Converter" will appear.
2.  **Enter miles:** In the entry field next to the "Miles" label, type the distance you want to convert from miles to kilometers.
3.  **Click "Calculate":** Click the "Calculate" button below the input field.
4.  **View the result:** The converted distance in kilometers will be displayed next to the "is equal to:" label and the "Km" label. The result is rounded to two decimal places.
5.  **Close the window:** You can close the application window when you are finished.

## Functionality

* **User Input:** Provides an entry field for the user to input the distance in miles.
* **Conversion:** When the "Calculate" button is clicked, the application retrieves the value entered by the user, multiplies it by the conversion factor (1 mile = 1.60934 kilometers), and calculates the equivalent distance in kilometers.
* **Result Display:** Shows the calculated distance in kilometers in a label within the application window.
* **GUI Interface:** Utilizes Tkinter to create a user-friendly window with labels, an entry field, and a button.

## Requirements

* Python 3.x (The `tkinter` module is typically included with standard Python installations.)

## Installation

No specific installation is required. Save the provided code as a `.py` file (e.g., `miles_to_km_converter.py`) and run it using a Python interpreter.

## Code Explanation

* **`from dbm.sqlite3 import BUILD_TABLE`:** This import statement seems unnecessary for this particular application and can likely be removed. The `dbm.sqlite3` module is for working with database files and is not used in the provided code.
* **`from tkinter import *`:** Imports all modules and classes from the Tkinter library, which is used for creating the GUI.
* **`window = Tk()`:** Creates the main window object for the application.
* **`window.title("Mile to Km Converter")`:** Sets the title that appears in the title bar of the window.
* **`window.config(padx=20, pady=20)`:** Adds padding around the content of the window in the x and y directions (20 pixels each).
* **`miles_input = Entry()`:** Creates an entry field widget where the user can type in the miles value.
* **`miles_input.grid(column=1, row=0)`:** Places the entry field in the grid layout of the window at column 1, row 0.
* **`is_equal_to = Label(text="is equal to: ")`:** Creates a label displaying the text "is equal to: ".
* **`is_equal_to.grid(column=0, row=1)`:** Places this label at column 0, row 1 in the grid.
* **`miles = Label(text="Miles")`:** Creates a label displaying the text "Miles".
* **`miles.grid(column=2, row=0)`:** Places this label at column 2, row 0 in the grid, next to the input field.
* **`km = Label(text="Km")`:** Creates a label displaying the text "Km".
* **`km.grid(column=2, row=1)`:** Places this label at column 2, row 1 in the grid, next to the result display.
* **`result = Label(text=0)`:** Creates a label to display the conversion result, initialized with the value 0.
* **`result.grid(column=1, row=1)`:** Places this label at column 1, row 1 in the grid.
* **`def miles_to_km():`:** Defines a function that is called when the "Calculate" button is clicked.
    * **`miles_to_km = float(miles_input.get()) * 1.60934`:** Retrieves the text entered in the `miles_input` field using `.get()`, converts it to a floating-point number, and multiplies it by the conversion factor 1.60934.
    * **`result.config(text=round(miles_to_km, 2))`:** Updates the text of the `result` label to display the calculated value, rounded to two decimal places using `round()`.
* **`button = Button(text="Calculate", command=miles_to_km)`:** Creates a button with the text "Calculate". The `command=miles_to_km` argument specifies that the `miles_to_km` function should be called when the button is clicked.
* **`button.grid(column=1, row=2)`:** Places the button at column 1, row 2 in the grid.
* **`window.mainloop()`:** Starts the Tkinter event loop, which is necessary for the GUI to be displayed and interactive. It listens for events (like button clicks) and handles them accordingly.
