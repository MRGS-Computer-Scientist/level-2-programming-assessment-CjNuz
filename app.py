from tkinter import *
from os import path
from PIL import Image, ImageTk
from app_settings import *

class App():
    main_app = None  # Class variable to hold the main app instance

    def __init__(self, root=None, is_sub_window=False):
        self.is_sub_window = is_sub_window
        if not root:
            self.root = Tk()
            App.main_app = self  # Set the main app instance
        else:
            self.root = root

        # Set the window properties
        self.root.geometry("430x932")
        self.root.title("SportsX")
        self.root.configure(background="black")
        self.root.resizable(width=False, height=False)

        # Create top and main frames
        self.top_frame = Frame(self.root, background="black", width=frame_width, height=topF_height)
        self.top_frame.pack_propagate(False)  # Prevent the frame from resizing to fit content
        self.main_frame = Frame(self.root, background="black", width=frame_width, height=frame_height)

        # Pack the frames into the main window
        self.top_frame.pack(side=TOP, fill=BOTH)
        self.main_frame.pack(side=TOP, fill=BOTH)

        # File paths for images
        dirname = path.dirname(__file__)
        self.logo_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\sportsxlogo.jpg')
        self.basketball_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Basketball_grey.png')
        self.football_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Football_grey.png')
        self.cricket_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Cricket_grey.png')

        # Load images and create buttons
        self.load_images()
        self.create_buttons(self.top_frame, self.main_frame)

        # Start the Tkinter main loop if this is the main window
        if not root:
            self.root.mainloop()

    def load_images(self):
        # Function to load and resize images
        self.logo_image = self.resize_image(self.logo_filename, (300, 100))
        self.basketball_image = self.resize_image(self.basketball_filename)
        self.football_image = self.resize_image(self.football_filename)
        self.cricket_image = self.resize_image(self.cricket_filename)

    def resize_image(self, filepath, size=(100, 100)):
        # Function to resize an image
        img = Image.open(filepath)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def create_buttons(self, top_frame, main_frame):
        # Create a button for the logo in the top frame
        logo_button = Button(top_frame, image=self.logo_image, command=self.return_to_home, highlightthickness=0, bd=0, bg="black", activebackground="black")
        logo_button.pack(pady=10)

        # Configure columns in the main frame
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)

        # Create buttons for sports in the main frame
        button1 = Button(main_frame, image=self.basketball_image, command=self.open_basketball_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = Button(main_frame, image=self.football_image, command=self.open_football_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        button2.grid(row=0, column=1, padx=10, pady=10)

        button3 = Button(main_frame, image=self.cricket_image, command=self.open_cricket_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        button3.grid(row=0, column=2, padx=10, pady=10)

    def open_basketball_window(self):
        # Open a new window for basketball
        self.open_new_window("Basketball Window")

    def open_football_window(self):
        # Open a new window for football
        self.open_new_window("Football Window")

    def open_cricket_window(self):
        # Open a new window for cricket
        self.open_new_window("Cricket Window")

    def open_new_window(self, title):
        # Open a new window and close the current one if it's a sub-window
        if self.is_sub_window:
            self.root.destroy()
        else:
            self.root.withdraw()
        new_root = Toplevel()
        new_app = App(new_root, is_sub_window=True)
        new_app.root.title(title)
        new_app.root.configure(background="black")
        new_app.root.geometry("430x932")

    def return_to_home(self):
        # Return to the main window by destroying the sub-window and showing the main window
        if self.is_sub_window:
            self.root.destroy()
            App.main_app.root.deiconify()

# Main program entry point
if __name__ == "__main__":
    main_app = App()
