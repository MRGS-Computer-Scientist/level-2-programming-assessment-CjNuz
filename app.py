from tkinter import *
from app_settings import *
from os import * 
from PIL import Image, ImageTk 
from basketball import Basketball
from cricket import Cricket
from football import Football

class App():
    def __init__(self):
        # Main Page
        self.window = Tk()
        self.window.geometry("430x932")
        self.window.title("SportsX")
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
            self.window.withdraw()  # Close the current window
            Basketball(self.window) # Open the baskeball window
            

        # Football Page
        def open_football():
            self.window.withdraw()  # Close the current window
            Football(self.window) # Open the football window
            

        # Cricket Page
        def open_cricket():
            self.window.withdraw()  # Close the current window
            Cricket(self.window)  # Open the cricket window



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

        #Button Image
        #Buttons
        basketball_button = Button(self.main_frame, text="🏀", command=open_basketball, font=("Roboto", 38), width=button_width, height=button_height, compound="left")
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