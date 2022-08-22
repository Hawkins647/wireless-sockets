import tkinter
from energenie import switch_on, switch_off


def turn_on_plug():
    switch_on()
    
    
def turn_off_plug():
    switch_off()


root = tkinter.Tk()
root.geometry("300x200")
root.title("Wireless Fan")
root.resizable(0, 0)

title_label = tkinter.Label(root, text="aidans magic fan", font=("Rubrik", 25))
title_label.pack(padx=5, pady=5)

options_frame = tkinter.Frame(root, bg="grey")
options_frame.pack(padx=5, pady=5)

fan_on_button = tkinter.Button(options_frame, text="Turn On", font=("Rubrik", 15), width=10, command=turn_on_plug)
fan_on_button.grid(row=0, column=0, padx=10, pady=5)

fan_off_button = tkinter.Button(options_frame, text="Turn Off", font=("Rubrik", 15), width=10, command=turn_off_plug)
fan_off_button.grid(row=0, column=1, padx=10, pady=5)

title_label = tkinter.Label(root, text="aidans magic fan", font=("Rubrik", 25))
title_label.pack(padx=5, pady=5)


root.mainloop()
