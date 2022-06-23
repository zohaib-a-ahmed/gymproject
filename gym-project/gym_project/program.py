import tkinter
import tkinter.messagebox
from wave import WAVE_FORMAT_PCM
import customtkinter
from numpy import column_stack
import exercisedbdata
from PIL import Image, ImageTk
import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("dark")
PATH = os.path.dirname(os.path.realpath(__file__))


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Progress Pal")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        self.resizable(False, False)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Create top frame

        self.topmenu = customtkinter.CTkFrame(master = self, height = 70, corner_radius=0, width = 780)
        self.topmenu.grid(row = 0, column = 0, sticky = "nswe")

        self.topmenu.grid_columnconfigure(3, minsize=175)
        self.topmenu.grid_columnconfigure(1, minsize=175)
        self.topmenu.grid_columnconfigure(5, minsize=175)

        # Create logo

        self.logo = customtkinter.CTkLabel(master=self.topmenu,
                                              text="PAL",
                                              text_font=("Helvetica", -64))  # font name and size in px
        self.logo.grid(row=0, column=1, pady=10, padx=10)

        # Create menu options

        self.searchbutton = customtkinter.CTkButton(master=self.topmenu,
                                                text="Explore",
                                                command=self.searchpanel
                                        )
        self.searchbutton.grid(row=0, column=2)

        self.analyzebutton = customtkinter.CTkButton(master=self.topmenu,
                                                text="Analyze",
                                                command=self.button_event)
        self.analyzebutton.grid(row=0, column=3)

        self.buildbutton = customtkinter.CTkButton(master=self.topmenu,
                                                text="Build",
                                                command=self.button_event)
        self.buildbutton.grid(row=0, column=4)

        self.darkmodeswitch = customtkinter.CTkSwitch(master=self.topmenu,
                                                text="Light Mode",
                                                command=self.change_mode)
        self.darkmodeswitch.grid(row=0, column=5, pady=10, padx=20, sticky="w")

        # Create bottom screen initial image

        self.bottom = customtkinter.CTkFrame(master = self)
        self.bottom.grid(row = 1, column = 0, sticky = "nswe")

        # load image with PIL and convert to PhotoImage
        image = Image.open(PATH + "/barbellsimple.jpeg").resize((self.WIDTH, self.HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tkinter.Label(master=self.bottom, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def button_event(self):
        print("Button pressed")

    def searchpanel(self):
        self.bottom.grid_forget()
        # Remove previous frame

        # Create search panel

        self.searchframe = customtkinter.CTkFrame(master = self)
        self.searchframe.grid(rows = 1, columns = 10, sticky = "nswe", padx = 20, pady = 20)
        self.searchframe.grid_columnconfigure(1, minsize = 260)

        self.entry = customtkinter.CTkEntry(master=self.searchframe,
                                            placeholder_text=" exercise, weightlifting movement, stretch, e.g.",
                                            width = 500)
        self.entry.grid(row=0, column=0, pady=20, padx=20, sticky="nswe", columnspan = 8)
        
        # Assign search button to a results display
        self.searchquerybutton = customtkinter.CTkButton(master=self.searchframe,
                                                text="Search",
                                                command=self.searchresults)
        self.searchquerybutton.grid(row=0, column=9, padx = 20, pady = 20)

        #self.results = customtkinter.CTkFrame(master = self.searchframe, height = 300, width = 350)
        #self.results.grid(row = 1, column = 0, padx = 10, pady = 10)

        #self.display = customtkinter.CTkFrame(master = self.searchframe, height = 300, width = 350)
        #self.display.grid(row = 1, column = 1, padx = 10, pady = 10)

    def searchresults(self):
        results = exercisedbdata.getSimilarMovements(self.entry.get())
        
        for i in range(len(results)):
            print("button made")

            columncounter = int(i / 5)
            if(i > 4):
                rowcounter = i - 5
            else:
                rowcounter = i

            self.resultframe = customtkinter.CTkFrame(master = self.searchframe, width = 100)
            self.resultframe.grid(row = rowcounter + 1, column = columncounter, pady = 5, padx = 10, sticky = "nswe")

            #self.result = customtkinter.CTkLabel(master=self.resultframe,
              #                                text=results[i],
             #                                 text_font=("Helvetica", 16))  # font name and size in px
            #self.result.grid(row=rowcounter + 1, column=columncounter + 1, pady=5, padx=10)

            self.resultbutton = customtkinter.CTkButton(master=self.resultframe,
                                                  text=results[i],
                                                  command=self.testbuttontext(results[i]))
            self.resultbutton.grid(row = rowcounter + 1, column = columncounter + 1 , padx = 10, pady = 10)


        #self.movementdisplay = customtkinter.CTkFrame(master = self.searchframe, width = 240, height = 240)
        #self.movementdisplay.grid(column = 4, row = 4, padx = 20, pady = 20)

    def testbuttontext(name: str):
        print(name)


    def change_mode(self):
        if self.darkmodeswitch.get() == 1:
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("dark")

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()