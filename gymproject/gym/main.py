from program import Program
import program
import tkinter
import tkinter.messagebox
import customtkinter
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
 
       self.topmenu.grid_columnconfigure(3, minsize=160)
       self.topmenu.grid_columnconfigure(1, minsize=160)
       self.topmenu.grid_columnconfigure(4, minsize=160)
 
       # Create logo
 
       self.logo = customtkinter.CTkLabel(master=self.topmenu,
                                             text="PAL",
                                             text_font=("Helvetica", -64))  # font name and size in px
       self.logo.grid(row=0, column=1, pady=10, padx=10)
 
       # Create menu options
 
       self.buildbutton = customtkinter.CTkButton(master=self.topmenu,
                                               text="Build",
                                               command=self.first_info_page)
       self.buildbutton.grid(row=0, column=2)
 
       self.darkmodeswitch = customtkinter.CTkSwitch(master=self.topmenu,
                                               text="Light Mode",
                                               command=self.change_mode)
       self.darkmodeswitch.grid(row=0, column=6, pady=10, padx=20, sticky="w")
 
       # Create bottom screen initial image
 
       self.bottom = customtkinter.CTkFrame(master = self)
       self.bottom.grid(row = 1, column = 0, sticky = "nswe")
 
       # load image with PIL and convert to PhotoImage
       image = Image.open(PATH + "/barbellsimple.jpeg").resize((self.WIDTH, self.HEIGHT))
       self.bg_image = ImageTk.PhotoImage(image)
 
       self.image_label = tkinter.Label(master=self.bottom, image=self.bg_image)
       self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
 
   def first_info_page(self):
       self.bottom.grid_forget()
       self.buildbutton.configure(state=tkinter.DISABLED)
 
       self.info = customtkinter.CTkFrame(master=self) # main information frame
       self.info.grid(row=1, column=0, columnspan=4, rowspan=4, pady=20, padx=20, sticky="nswe")
 
       # Instruction frame + label
       self.instructions = customtkinter.CTkFrame(master = self.info)
       self.instructions.grid(row=1, column=0, columnspan=7, pady=20, padx=20, sticky="nswe")
       self.instruction = customtkinter.CTkLabel(master = self.instructions,
                                                   text = "                                                Please fill this out to tailor your plan for your lifestyle:")
       self.instruction.grid(row = 0, column = 4, columnspan = 7, padx = 10, pady = 10, sticky = "nswe")
 
       # Days Available Frame + Day checkboxes
       self.days = customtkinter.CTkLabel(master = self.info,
                                           text = "Days You Can Lift")
       self.days.grid(row = 2, column = 4, sticky = "nswe", pady = 10)
 
       self.monday = customtkinter.CTkCheckBox(master = self.info, text = "Monday")
       self.monday.grid(row = 2, column = 0, sticky = "nswe", pady = 10, padx = 20)
       self.tuesday = customtkinter.CTkCheckBox(master = self.info, text = "Tuesday")
       self.tuesday.grid(row = 2, column = 1, sticky = "nswe", pady = 10)
       self.wednesday = customtkinter.CTkCheckBox(master = self.info, text = "Wednesday")
       self.wednesday.grid(row = 2, column = 2, sticky = "nswe", pady = 10)
       self.thursday = customtkinter.CTkCheckBox(master = self.info, text = "Thursday")
       self.thursday.grid(row = 2, column = 3, sticky = "nswe", pady = 10)
       self.friday = customtkinter.CTkCheckBox(master = self.info, text = "Friday")
       self.friday.grid(row = 3, column = 0, sticky = "nswe", pady = 10, padx = 20)
       self.saturday = customtkinter.CTkCheckBox(master = self.info, text = "Saturday")
       self.saturday.grid(row = 3, column = 1, sticky = "nswe", pady = 10)
       self.sunday = customtkinter.CTkCheckBox(master = self.info, text = "Sunday")
       self.sunday.grid(row = 3, column = 2, sticky = "nswe", pady = 10)
 
       # Time available slider + label + markings
       self.timeslider = customtkinter.CTkSlider(master=self.info,
                                               from_=1,
                                               to=4,
                                               number_of_steps=8)
       self.timeslider.grid(row=4, column=0, columnspan=4, pady=10, padx=20, sticky="nswe")
       self.timelabel = customtkinter.CTkLabel(master = self.info,
                                               text = "Hours Available")
       self.timelabel.grid(row = 4, column = 4, pady = 10, sticky = "nswe", columnspan = 1)
       for i in range(4):
           self.time = customtkinter.CTkLabel(master = self.info, text = str(i + 1))
           self.time.grid(row = 5, column = i)
 
       # Bodytype assessment frame + label
       self.instructions2 = customtkinter.CTkFrame(master = self.info)
       self.instructions2.grid(row=6, column=0, columnspan=7, padx = 10, pady = 10, sticky = "nswe")
       self.instruction2 = customtkinter.CTkLabel(master = self.instructions2, text = "                     Please assess your bodytype. Describe based off your size and body composition:")
       self.instruction2.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = "nswe")
      
       # Bodytype radiobuttons + variable
       self.radio_var = tkinter.IntVar(value=0)
       self.radio_button_1 = customtkinter.CTkRadioButton(master=self.info,
                                                          variable=self.radio_var,
                                                          value=1,
                                                          text = "Skinny/Lean")
       self.radio_button_1.grid(row=7, column=2, pady=10, padx = 10, sticky="nswe")
       self.radio_button_2 = customtkinter.CTkRadioButton(master=self.info,
                                                          variable=self.radio_var,
                                                          value=2,
                                                          text = "Skinny/Fat")
       self.radio_button_2.grid(row=7, column=1, pady=10, sticky="nswe")
       self.radio_button_3 = customtkinter.CTkRadioButton(master=self.info,
                                                          variable=self.radio_var,
                                                          value=3,
                                                          text = "Overweight")
       self.radio_button_3.grid(row=7, column=3, pady=10, sticky="nswe")
       self.radio_button_4 = customtkinter.CTkRadioButton(master=self.info,
                                                          variable=self.radio_var,
                                                          value=4,
                                                          text = "Semi-Muscular")
       self.radio_button_4.grid(row=7, column=0, pady=10, sticky="nswe", padx = 20)
 
       # submit button to next page
       self.submitbutton = customtkinter.CTkButton(master = self.info, text = "Next", command = self.second_info_page) # write command
       self.submitbutton.grid(row = 7, column = 4, pady = 10, sticky = "nswe", columnspan = 1)
 
       # Set pre-existing conditions
       self.timeslider.set(2)
       self.monday.select()
       self.tuesday.select()
       self.wednesday.select()
       self.thursday.select()
       self.friday.select()
       self.saturday.select()
       self.radio_button_4.select()
  
   def second_info_page(self):
       self.info.forget() # forget previous page
 
 
       self.info2 = customtkinter.CTkFrame(master = self) # new info page
       self.info2.grid(row=1, column=0, columnspan=7, rowspan=4, pady=20, padx=20, sticky="nswe")
 
       # instructions frame + label
       self.instructions2 = customtkinter.CTkFrame(master = self.info2)
       self.instructions2.grid(row=1, column=0, columnspan=7, pady=20, padx=20, sticky="nswe")
       self.instruction2 = customtkinter.CTkLabel(master = self.instructions2,
       text = " Please fill this out to tailor your plan to your specific person. This information will not be stored or distributed.")
       self.instruction2.grid(row = 0, column = 0, columnspan = 7, padx = 10, pady = 10, sticky = "nswe")
 
       # new radiobutton for gender + variable + label
       self.gender = tkinter.IntVar(value=0)
       self.gender_male = customtkinter.CTkRadioButton(master = self.info2, text = "Male", value = 0, variable = self.gender)
       self.gender_male.grid(row = 2, column = 1, padx = 20, sticky = "nswe")
       self.gender_female = customtkinter.CTkRadioButton(master = self.info2, text = "Female", value = 1, variable=self.gender)
       self.gender_female.grid(row = 2, column = 3, sticky = "nswe")
       self.ask_gender = customtkinter.CTkLabel(master = self.info2, text = "Select your Gender")
       self.ask_gender.grid(row = 2, column = 5, padx = 20, sticky = "nswe")
 
       # entry bar for age + label (can add input checking later)
       self.age_entry = customtkinter.CTkEntry(master=self.info2, corner_radius=6, placeholder_text="21, 16, 45, etc.")
       self.age_entry.grid(row = 3, column = 1, columnspan = 3, padx = 20, pady = 20, sticky = "nswe")
       self.ask_age = customtkinter.CTkLabel(master = self.info2, text = "Enter your Age")
       self.ask_age.grid(row = 3, column = 5, padx = 20, sticky = "nswe")
 
       # Target area instruction frame + label
       self.instructions3 = customtkinter.CTkFrame(master = self.info2)
       self.instructions3.grid(row = 4, column = 0, columnspan = 7, padx = 20, sticky = "nswe")
       self.instruction3 = customtkinter.CTkLabel(master = self.instructions3,
       text = "What specific target areas do you want to emphasize? Leave blank for a general emphasis on everything.")
       self.instruction3.grid(row = 5, column = 0, columnspan = 7, padx = 10, pady = 10, sticky = "nswe")
 
       # Target area checkbox options
       self.arms = customtkinter.CTkCheckBox(master = self.info2, text = "Arms", onvalue=1)
       self.arms.grid(row = 6, column = 0, padx = 20, pady = 20, sticky = "nswe")
       self.chest = customtkinter.CTkCheckBox(master = self.info2, text = "Chest", onvalue=1)
       self.chest.grid(row = 6, column = 1, padx = 10, pady = 20, sticky = "nswe")
       self.shoulders = customtkinter.CTkCheckBox(master = self.info2, text = "Shoulders", onvalue=1)
       self.shoulders.grid(row = 6, column = 2, padx = 10, pady = 20, sticky = "nswe")
       self.back = customtkinter.CTkCheckBox(master = self.info2, text = "Back", onvalue=1)
       self.back.grid(row = 6, column = 3, padx = 10, pady = 20, sticky = "nswe")
       self.glutes = customtkinter.CTkCheckBox(master = self.info2, text = "Glutes", onvalue=1)
       self.glutes.grid(row = 6, column = 4, padx = 10, pady = 20, sticky = "nswe")
       self.legs = customtkinter.CTkCheckBox(master = self.info2, text = "Legs", onvalue=1)
       self.legs.grid(row = 6, column = 5, padx = 20, pady = 20, sticky = "nswe")
 
       # Ending frame + label
       self.ending = customtkinter.CTkFrame(master = self.info2)
       self.ending.grid(row = 7, column = 0, columnspan = 7, padx = 20, sticky = "nswe")
       self.endingmessage = customtkinter.CTkLabel(master = self.ending, text = "If all this information is correct, select 'Continue'. Enjoy your new routine!")
       self.endingmessage.grid(column = 0, row = 7, padx = 10, pady = 10, sticky = "nswe")
 
       # submit option
       self.submit = customtkinter.CTkButton(master = self.ending, text = "Continue", command = self.create_workout) # create command
       self.submit.grid(row = 7, column = 7, padx = 10, pady = 10, sticky = "nswe")
 
   def create_workout(self):
       self.success_screen() # create success screen -> method
 
       # create program input
       days = self.monday.get() + self.tuesday.get() + self.wednesday.get() + self.thursday.get() + self.friday.get() + self.saturday.get() + self.sunday.get()
       time = self.timeslider.get()
       targets = [self.arms.get(), self.chest.get(), self.shoulders.get(), self.back.get(), self.glutes.get(), self.legs.get()]
      
       # Create workout routine file
       try:
        workout = Program(int(self.age_entry.get()), self.gender.get(), days, time, targets, self.radio_var.get())
       except(ValueError):
        workout = Program(20, self.gender.get(), days, time, targets, self.radio_var.get())
 
   def success_screen(self):
       self.info2.forget() # forget previous screen
      
       # create success frame + info
       self.success = customtkinter.CTkFrame(master = self)
       self.success.grid(row=1, column=0, columnspan=4, rowspan=4, pady=20, padx=20, sticky="nswe")
       self.instructions = customtkinter.CTkFrame(master = self.success)
       self.instructions.grid(row=1, column=0, columnspan=7, pady=20, padx=20, sticky="nswe")
       self.instruction = customtkinter.CTkLabel(master = self.instructions,
                                                   text = "Success! Look for a file called 'program.txt' where you will find your new routine. Enjoy your newfound progress!")
       self.instruction.grid(row = 0, column = 4, columnspan = 7, pady = 10, sticky = "nswe")
 
   def change_mode(self): # basic dark mode function (doesn't really look good)
       if self.darkmodeswitch.get() == 1:
           customtkinter.set_appearance_mode("light")
       else:
           customtkinter.set_appearance_mode("dark")
 
   def on_closing(self, event=0):
       self.destroy()
 
 
if __name__ == "__main__":
   app = App()
   app.mainloop()
