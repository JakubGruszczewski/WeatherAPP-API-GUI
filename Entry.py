import tkinter as tk


def chose_place():
    chosen_city = None
    chosen_unit = "metric"

    def get_input():
        nonlocal chosen_city
        chosen_city = ((entry_var.get()).capitalize())
        place_widget.destroy()

    def setting_widget():
        def get_unit():
            nonlocal chosen_unit
            chosen_unit = dropdown_menu_info.get()
            settings_widget.destroy()

        settings_widget = tk.Tk()
        settings_widget.geometry("250x150")
        settings_widget.title("WeatherApp - Settings")
        settings_widget.resizable(False, False)

        settings_info_label = tk.Label(settings_widget, text="Choose units of measurements", font=("Arial Bold", 12),
                                       anchor="center")
        settings_info_label.grid(column=0, row=0, pady=12, padx=3, sticky="nsew")

        dropdown_menu_info = tk.StringVar(settings_widget)
        dropdown_menu_info.set("Units")

        dropdown_menu_units = ["Metric", "Imperial"]

        dropdown_menu = tk.OptionMenu(settings_widget, dropdown_menu_info, *dropdown_menu_units)
        dropdown_menu.config(width=8, height=1, font=("Calibri", 12), bg="#E2E2E2")
        dropdown_menu.grid(column=0, row=1, pady=10)

        accept_button = tk.Button(settings_widget, text="Accept", font="Arial, 10", bg="#A4C7A4", command=get_unit)
        accept_button.grid(column=0, row=2, pady=7)

    place_widget = tk.Tk()
    place_widget.geometry("350x140")
    place_widget.title("WeatherApp")
    place_widget.resizable(False, False)

    enter_label = tk.Label(place_widget, text="Enter the city name", font=("Arial Bold", 17), width=25,
                           anchor='center')
    enter_label.place(x=0, y=17)

    settings_button = tk.Button(place_widget, font=("Arial", 12), text="\U0001F527", bg="#E2E2E2",
                                command=setting_widget)
    settings_button.place(x=315, y=5)

    entry_var = tk.StringVar(place_widget)
    entry_block = tk.Entry(place_widget, font=5, textvariable=entry_var, width=30)
    entry_block.place(x=8, y=65)

    submit_button = tk.Button(place_widget, text="Submit", font="Calibri, 10", command=get_input,
                              bg="#A4C7A4", height=1, width=10)
    submit_button.place(x=175, y=115, anchor="center")

    place_widget.mainloop()

    result = (chosen_city, chosen_unit)
    return result
