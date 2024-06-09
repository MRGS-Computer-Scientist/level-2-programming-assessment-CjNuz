from tkinter import *
from app_settings import *
from os import * 
from PIL import Image, ImageTk 
from app import App

class Cricket(Tk):
    def __init__(self, master ):
    # Main Page
        self.window = Toplevel(master)
        self.window.geometry("430x932")
        self.window.title("Cricket")
        self.window.configure(background="black")
        self.window.resizable(width=False, height=False)
        # Frame
        self.top_frame = Frame(self.window, background="black", width= frame_width, height= topF_height)
        self.top_frame.pack_propagate(False)
        self.main_frame = Frame(self.window, background="black", width= frame_width, height= frame_height)

        # Frame pack
        self.top_frame.pack(side=TOP, fill=BOTH)
        self.main_frame.pack(side=TOP, fill=BOTH)

        # Button functions
        # Basketball Page
        def open_basketball():
            from basketball import Basketball
            self.window.withdraw()  # Close the current window
            Basketball(self.window)  # Open the basketball window
            

        # Football Page
        def open_football():
            from football import Football
            self.window.withdraw()  # Close the current window
            Football(self.window)  # Open the football window

            

        # Cricket Page
        def open_cricket():
            from cricket import Cricket
            self.window.withdraw()  # Close the current window
            Cricket(self.window)  # Open the cricket window

        # Logo Button Click
        def logo_click():
            self.window.destroy()  # Close the current window
            App()  # Open the main app window

        dirname = path.dirname(__file__)
        logo_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\LogoSportsX.png')
        basketball_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Basketball_grey.png')
        football_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Football_grey.png')
        cricket_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Cricket_green.png')

        # Load and resize logo image
        self.image = Image.open(logo_filename)
        self.image = self.image.resize((frameImg_width, frameImg_height), Image.LANCZOS)
        self.Logo = ImageTk.PhotoImage(self.image)

        # Load and resize basketball button image
        self.basketball_image = Image.open(basketball_filename)
        self.basketball_image = self.basketball_image.resize((button_width * 50, button_height * 110), Image.LANCZOS)  # Adjust size as needed
        self.basketball_photo = ImageTk.PhotoImage(self.basketball_image)

        # Load and resize football button image
        self.football_image = Image.open(football_filename)
        self.football_image = self.football_image.resize((button_width * 50, button_height * 110), Image.LANCZOS)  # Adjust size as needed
        self.football_photo = ImageTk.PhotoImage(self.football_image)

        # Load and resize cricket button image
        self.cricket_image = Image.open(cricket_filename)
        self.cricket_image = self.cricket_image.resize((button_width * 50, button_height * 110), Image.LANCZOS)  # Adjust size as needed
        self.cricket_photo = ImageTk.PhotoImage(self.cricket_image)


        # Background image label
        self.backgroundlogo = Label(self.top_frame, image=self.Logo)
        self.backgroundlogo.place(x=0, y=0, relwidth=1, relheight=1)

        # Buttons
        basketball_button = Button(self.main_frame, image=self.basketball_photo, command=open_basketball, bd=0, highlightthickness=0)
        basketball_button.image = self.basketball_photo  # Keep a reference to prevent garbage collection
        basketball_button.config(width=button_width * 50, height=button_height * 110)

        self.logo_button = Button(self.top_frame, image=self.Logo, command=logo_click, bd=0, highlightthickness=0)
        self.logo_button.image = self.Logo  # Keep a reference to prevent garbage collection
        self.logo_button.place(x=0, y=0, relwidth=1, relheight=1)

        
        football_button = Button(self.main_frame, image=self.football_photo, command=open_football, bd=0, highlightthickness=0)
        football_button.image = self.football_photo  # Keep a reference to prevent garbage collection
        football_button.config(width=button_width * 50, height=button_height * 110)

        cricket_button = Button(self.main_frame, image=self.cricket_photo, command=open_cricket, bd=0, highlightthickness=0)
        cricket_button.image = self.cricket_photo  # Keep a reference to prevent garbage collection
        cricket_button.config(width=button_width * 50, height=button_height * 110)

        # Button packs
        basketball_button.grid(row=0, column=0, padx=18, pady=buttonY)
        football_button.grid(row=0, column=1, padx=30, pady=buttonY)
        cricket_button.grid(row=0, column=2, padx=20, pady=buttonY)

        # Run
        self.window.mainloop()
