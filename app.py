from tkinter import *
from app_settings import *
from os import path
from PIL import Image, ImageTk

class App():
    def __init__(self):
        # Main Page
        self.window = Tk()
        self.window.geometry("430x932")
        self.window.title("SportsX")
        self.window.configure(background="black")
        self.window.resizable(width=False, height=False)

        # Frame
        self.top_frame = Frame(self.window, background="black", width=frame_width, height=topF_height)
        self.top_frame.pack_propagate(False)
        self.main_frame = Frame(self.window, background="black", width=frame_width, height=frame_height)

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

        # Load images
        dirname = path.dirname(__file__)
        logo_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\LogoSportsX.png')
        basketball_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Basketball.psd')

        # Load and resize logo image
        self.image = Image.open(logo_filename)
        self.image = self.image.resize((frameImg_width, frameImg_height), Image.LANCZOS)
        self.Logo = ImageTk.PhotoImage(self.image)

        # Load and resize basketball button image
        self.basketball_image = Image.open(basketball_filename)
        self.basketball_image = self.basketball_image.resize((button_width * 45, button_height * 140), Image.LANCZOS)  # Adjust size as needed
        self.basketball_photo = ImageTk.PhotoImage(self.basketball_image)

        # Background image label
        self.backgroundlogo = Label(self.top_frame, image=self.Logo)
        self.backgroundlogo.place(x=0, y=0, relwidth=1, relheight=1)

        # Buttons
        basketball_button = Button(self.main_frame, image=self.basketball_photo, command=open_basketball, bd=0, highlightthickness=0)
        basketball_button.image = self.basketball_photo  # Keep a reference to prevent garbage collection
        basketball_button.config(width=button_width * 40, height=button_height * 120)
        
        football_button = Button(self.main_frame, text="⚽", command=open_football, font=("Roboto", 38), width=button_width, height=button_height, compound="right")
        cricket_button = Button(self.main_frame, text="🏏", command=open_cricket, font=("Roboto", 38), width=button_width, height=button_height, compound="right")

        # Button packs
        basketball_button.grid(row=0, column=0, padx=18, pady=buttonY)
        football_button.grid(row=0, column=1, padx=30, pady=buttonY)
        cricket_button.grid(row=0, column=2, padx=20, pady=buttonY)

        # Run
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
