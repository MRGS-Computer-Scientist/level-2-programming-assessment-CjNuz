from tkinter import *
from os import path
from PIL import Image, ImageTk
from app_settings import *

class App():
    main_app = None  # Main app instance

    def __init__(self, root=None, is_sub_window=False):
        self.is_sub_window = is_sub_window
        if not root:
            self.root = Tk()
            App.main_app = self  # Set main app instance
        else:
            self.root = root

        # Window properties
        self.root.geometry("430x932")
        self.root.title("SportsX")
        self.root.configure(background="black")
        self.root.resizable(width=False, height=False)

        # Create frames
        self.top_frame = Frame(self.root, background="black", width=frame_width, height=topF_height)
        self.top_frame.pack_propagate(False)  # Prevent frame from resizing to fit content
        self.main_frame = Frame(self.root, background="black", width=frame_width, height=frame_height)

        # Pack frames
        self.top_frame.pack(side=TOP, fill=BOTH)
        self.main_frame.pack(side=TOP, fill=BOTH)

        # Image file paths
        dirname = path.dirname(__file__)
        self.logo_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\sportsxlogo.jpg')
        self.basketball_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Basketball_grey.png')
        self.basketball_green_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Basketball_green.png')
        self.football_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Football_grey.png')
        self.football_green_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Football_green.png')
        self.cricket_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Cricket_grey.png')
        self.cricket_green_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Cricket_green.png')
        self.shooting_form_filename = path.join(dirname, r'C:\Users\23399\github-classroom\MRGS-Computer-Scientist\level-2-programming-assessment-CjNuz\Images\Shooting-form.png')

        # Load images and create buttons
        self.load_images()
        self.create_buttons(self.top_frame, self.main_frame)

        # Start the main loop if this is the main window
        if not root:
            self.root.mainloop()

    def load_images(self):
        # Load and resize images
        self.logo_image = self.resize_image(self.logo_filename, (300, 100))
        self.basketball_image = self.resize_image(self.basketball_filename)
        self.basketball_green_image = self.resize_image(self.basketball_green_filename)
        self.football_image = self.resize_image(self.football_filename)
        self.football_green_image = self.resize_image(self.football_green_filename)
        self.cricket_image = self.resize_image(self.cricket_filename)
        self.cricket_green_image = self.resize_image(self.cricket_green_filename)
        self.shooting_form_image = self.resize_image(self.shooting_form_filename, (150, 150))  # Make the button bigger

    def resize_image(self, filepath, size=(100, 100)):
        # Resize image
        img = Image.open(filepath)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def create_buttons(self, top_frame, main_frame):
        # Create logo button
        logo_button = Button(top_frame, image=self.logo_image, command=self.return_to_home, highlightthickness=0, bd=0, bg="black", activebackground="black")
        logo_button.pack(pady=10)

        # Configure columns
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)
        main_frame.grid_columnconfigure(3, weight=1)  # Add a new column for the new button

        # Create sport buttons
        self.basketball_button = Button(main_frame, image=self.basketball_image, command=self.open_basketball_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.basketball_button.grid(row=0, column=0, padx=10, pady=10)

        self.football_button = Button(main_frame, image=self.football_image, command=self.open_football_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.football_button.grid(row=0, column=1, padx=10, pady=10)

        self.cricket_button = Button(main_frame, image=self.cricket_image, command=self.open_cricket_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.cricket_button.grid(row=0, column=2, padx=10, pady=10)

        # Create shooting form button only if this is the main window or basketball window
        if not self.is_sub_window or self.root.title() == "Basketball Window":
            self.shooting_form_button = Button(main_frame, image=self.shooting_form_image, command=self.open_basketball_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
            self.shooting_form_button.grid(row=1, column=0, padx=10, pady=10)

    def open_basketball_window(self):
        # Open basketball window
        self.open_new_window("Basketball Window", change_basketball_image=True)

    def open_football_window(self):
        # Open football window
        self.open_new_window("Football Window", change_football_image=True)

    def open_cricket_window(self):
        # Open cricket window
        self.open_new_window("Cricket Window", change_cricket_image=True)


    def open_new_window(self, title, change_basketball_image=False, change_football_image=False, change_cricket_image=False):
        # Open new window and change images if needed
        if self.is_sub_window:
            self.root.destroy()
        else:
            self.root.withdraw()
        new_root = Toplevel()
        new_app = App(new_root, is_sub_window=True)
        new_app.root.title(title)
        new_app.root.configure(background="black")
        new_app.root.geometry("430x932")
        
        # Change images if required
        if change_basketball_image:
            new_app.basketball_button.config(image=new_app.basketball_green_image)
        if change_football_image:
            new_app.football_button.config(image=new_app.football_green_image)
        if change_cricket_image:
            new_app.cricket_button.config(image=new_app.cricket_green_image)

    def return_to_home(self):
        # Return to main window
        if self.is_sub_window:
            self.root.destroy()
            App.main_app.root.deiconify()

# Main program entry point
if __name__ == "__main__":
    main_app = App()
