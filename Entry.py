import tkinter as tk


def chose_place():
    chosen_city = None

    def get_input():
        nonlocal chosen_city
        chosen_city = ((entry_var.get()).capitalize())
        place_widget.destroy()

    place_widget = tk.Tk()
    place_widget.geometry("300x150")
    place_widget.title("WeatherApp")
    place_widget.resizable(False, False)

    label_place = tk.Label(place_widget, text="Enter the city name", font=25, width=24, height=2, anchor='center')
    label_place.grid(column=0, row=0, sticky="nsew")

    entry_var = tk.StringVar(place_widget)
    entry_block = tk.Entry(place_widget, font=15, textvariable=entry_var)
    entry_block.grid()

    submit_button = tk.Button(place_widget, text="Submit", command=get_input)
    submit_button.grid(column=0, row=2, padx=10, pady=10)

    place_widget.mainloop()
    return chosen_city
