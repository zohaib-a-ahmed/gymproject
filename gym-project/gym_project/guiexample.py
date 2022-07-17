import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))


class App(customtkinter.CTk):

    APP_NAME = "CustomTkinter example_background_image.py"
    WIDTH = 900
    HEIGHT = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(App.WIDTH, App.HEIGHT)
        self.maxsize(App.WIDTH, App.HEIGHT)
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        radio_var = tkinter.IntVar(0)

        def radiobutton_event():
            print("radiobutton toggled, current value:", radio_var.get())

        radiobutton_1 = customtkinter.CTkRadioButton(master=self, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
        radiobutton_2 = customtkinter.CTkRadioButton(master=self, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=1)

        radiobutton_1.pack(padx=20, pady=10)
        radiobutton_2.pack(padx=20, pady=10)

    def button_event(self):
        print("Login pressed - username:", self.entry_1.get(), "password:", self.entry_2.get())

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()