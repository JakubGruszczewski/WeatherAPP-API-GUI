import tkinter as tk


def display_error(message):

    def exit_function():
        exit()

    error_widget = tk.Tk()
    error_widget.geometry("350x80")
    error_widget.resizable(False, False)

    error_info = tk.Label(error_widget, text=message, font=("Arial Bold", 15), fg="#881919", width=28, anchor="center")
    error_info.grid(column=0, row=0, padx=4)

    exit_button = tk.Button(error_widget, text="Exit", font=("Calibri", 11), bg="#C34343", command=exit_function)
    exit_button.grid(column=0, row=1, pady=10)

    error_widget.mainloop()
