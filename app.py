from tkinter import *
from os import path
from PIL import Image, ImageTk
from app_settings import *

# Define the main application class
class App():
    def __init__(self):
        # Initialize the main Tkinter window
        self.window = Tk()
        self.window.geometry("430x932")  # Set window size
        self.window.title("SportsX")  # Set window title
        self.window.configure(background="black")  # Set window background color
        self.window.resizable(width=False, height=False)  # Disable window resizing

        # Create frames for layout
        self.top_frame = Frame(self.window, background="black", width=frame_width, height=topF_height)
        self.top_frame.pack_propagate(False)  # Prevent frame from resizing to fit content
        self.main_frame = Frame(self.window, background="black", width=frame_width, height=frame_height)

        # Pack frames into the main window
        self.top_frame.pack(side=TOP, fill=BOTH)
        self.main_frame.pack(side=TOP, fill=BOTH)

        # File paths for images
        dirname = path.dirname(__file__)
        self.logo_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\sportsxlogo.jpg')
        self.basketball_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Basketball_grey.png')
        self.football_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Football_grey.png')
        self.cricket_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Cricket_grey.png')

        # Load images
        self.load_images()
        # Create buttons using the loaded images
        self.create_buttons()

        # Start the Tkinter main loop
        self.window.mainloop()

    def load_images(self):
        # Function to load and resize images using PIL
        self.logo_image = self.resize_image(self.logo_filename, (300, 100))
        self.basketball_image = self.resize_image(self.basketball_filename)
        self.football_image = self.resize_image(self.football_filename)
        self.cricket_image = self.resize_image(self.cricket_filename)

    def resize_image(self, filepath, size=(100, 100)):
        # Function to resize an image
        img = Image.open(filepath)
        img = img.resize(size, Image.LANCZOS)  # Resize using Lanczos filter
        return ImageTk.PhotoImage(img)  # Convert to Tkinter PhotoImage

    def create_buttons(self):
        # Function to create buttons in the main frame

        # Create a button for the logo in the top frame
        home_button = Button(self.top_frame, image=self.logo_image, command=self.return_to_home,
                             highlightthickness=0, bd=0, bg="black", activebackground="black")
        home_button.pack(pady=10)  # Add padding and pack the button

        # Create buttons for sports in the main frame
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)

        button1 = Button(self.main_frame, image=self.basketball_image, command=self.open_basketball_window,
                         highlightthickness=0, bd=0, bg="black", activebackground="black")
        button1.grid(row=0, column=0, padx=10, pady=10)  # Grid placement with padding

        button2 = Button(self.main_frame, image=self.football_image, command=self.open_football_window,
                         highlightthickness=0, bd=0, bg="black", activebackground="black")
        button2.grid(row=0, column=1, padx=10, pady=10)  # Grid placement with padding

        button3 = Button(self.main_frame, image=self.cricket_image, command=self.open_cricket_window,
                         highlightthickness=0, bd=0, bg="black", activebackground="black")
        button3.grid(row=0, column=2, padx=10, pady=10)  # Grid placement with padding

    def open_basketball_window(self):
        # Function to open a new window for basketball
        self.create_new_window("Basketball Window")

    def open_football_window(self):
        # Function to open a new window for football
        self.create_new_window("Football Window")
    
    def open_cricket_window(self):
        # Function to open a new window for cricket
        self.create_new_window("Cricket Window")

    def create_new_window(self, title):
        # Function to create a new top-level window
        new_window = Toplevel(self.window)  # Create a new window
        new_window.title(title)  # Set window title
        new_window.configure(background="black")  # Set window background color
        new_window.geometry("430x932")  # Set window size
        label = Label(new_window, text=f"This is the {title}", padx=10, pady=10)
        label.pack()  # Pack label into the window

    def return_to_home(self):
        # Function to destroy all top-level windows
        for widget in self.window.winfo_children():
            if isinstance(widget, Toplevel):
                widget.destroy()

# Main program entry point
if __name__ == "__main__":
    app = App()  # Create an instance of the application
