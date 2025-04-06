from dbm.sqlite3 import BUILD_TABLE
from tkinter import *

# Window features.
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Get the user number.
miles_input = Entry()
miles_input.grid(column=1, row=0)

# Labels.
is_equal_to = Label(text="is equal to: ")
is_equal_to.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

# Shows the result.
result = Label(text=0)
result.grid(column=1, row=1)

def miles_to_km():
    '''Function responsible for getting the user answer and doing the conversion to Km.'''
    miles_to_km = float(miles_input.get()) * 1.60934
    result.config(text=round(miles_to_km, 2))

# Button.
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# Keep showing the window.
window.mainloop()