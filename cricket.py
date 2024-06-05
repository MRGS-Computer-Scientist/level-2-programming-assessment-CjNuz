from tkinter import *
from app_settings import *
from os import * 
from PIL import Image, ImageTk 


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

        self.window.mainloop()