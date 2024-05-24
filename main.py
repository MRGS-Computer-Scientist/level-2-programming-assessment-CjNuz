from tkinter import *
from app_settings import *
from os import * 
from PIL import Image, ImageTk 


class App():
    def __init__(self):
        # Main Page
        window = Tk()
        window.geometry("430x932")
        window.title("SportsX")
        window.configure(background="black")
        window.resizable(width=False, height=False)

        # Frame
        self.top_frame = Frame(window, background="black", width= frame_width, height= topF_height)
        self.top_frame.pack_propagate(False)
        self.main_frame = Frame(window, background="black", width= frame_width, height= frame_height)

        # Frame pack
        self.top_frame.pack(side=TOP, fill=BOTH)
        self.main_frame.pack(side=TOP, fill=BOTH)

        # Button functions
        # Basketball Page
        def basketball():
            print("You clicked the button!")

        # Football Page
        def football():
            print("Football")

        # Cricket Page
        def cricket():
            print("cricket")

        # Image
        dirname = path.dirname(__file__)
        filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\LogoSportsX.png')

        # Load image
        self.image = Image.open(filename)
        # Resize image to fit the top frame
        self.image = self.image.resize((frameImg_width, frameImg_height), Image.LANCZOS)
        self.Logo = ImageTk.PhotoImage(self.image)


        # Background image label
        self.backgroundlogo = Label(self.top_frame, image=self.Logo)
        self.backgroundlogo.place(x=0, y=0, relwidth=1, relheight=1)

        # Buttons
        basketball_button = Button(self.main_frame, text="🏀", command=basketball, font=("Roboto", 38), width=button_width, height=button_height, compound="left")
        football_button = Button(self.main_frame, text="⚽", command=football, font=("Roboto", 38), width=button_width, height=button_height, compound="right")
        cricket_button = Button(self.main_frame, text="🏏", command=cricket, font=("Roboto", 38), width=button_width, height=button_height, compound="right")

        # Button packs
        basketball_button.grid(row=0, column=0, padx=18, pady=buttonY)
        football_button.grid(row=0, column=1, padx=30, pady=buttonY)
        cricket_button.grid(row=0, column=2, padx=20, pady=buttonY)

        # Run
        window.mainloop()

# Instantiate the app
app = App()
