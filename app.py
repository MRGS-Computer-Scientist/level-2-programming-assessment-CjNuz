from tkinter import *
from os import path
from PIL import Image, ImageTk
from app_settings import *

class App:
    main_app = None  # Main app instance

    def __init__(self, root=None, is_sub_window=False):
        self.is_sub_window = is_sub_window
        if not root:
            self.root = Tk()
            App.main_app = self  # Set main app instance
        else:
            self.root = root

        # Window properties
        self.root.geometry("480x932")
        self.root.title("SportsX")
        self.root.configure(background="black")
        self.root.resizable(width=False, height=False)

        # Create frames
        self.top_frame = Frame(self.root, background="black", width=430, height=100)
        self.top_frame.pack_propagate(False)  # Prevent frame from resizing to fit content
        self.main_frame = Frame(self.root, background="black", width=430, height=600)

        # Pack frames
        self.top_frame.pack(side=TOP, fill=BOTH)
        self.main_frame.pack(side=TOP, fill=BOTH)

        # Image file paths
        dirname = path.dirname(__file__)
        print("PATHNAME: ", dirname + '\Images\sportsxlogo.jpg')
        self.logo_filename = dirname + '\Images\sportsxlogo.jpg'
        self.basketball_filename = dirname + '\Images\Basketball_grey.png'
        self.basketball_green_filename = dirname + '\Images\Basketball_green.png'
        self.football_filename = dirname + '\Images\Football_grey.png'
        self.football_green_filename = dirname + '\Images\Football_green.png'
        self.cricket_filename = dirname + '\Images\Cricket_grey.png'
        self.cricket_green_filename = dirname + '\Images\Cricket_green.png'
        self.shooting_form_filename = dirname + '\Images\Shooting-form.png'
        self.bicycle_kick_filename = dirname + '\Images\Bicyclekick.jpg'

        # Load images and create buttons
        self.load_images()
        self.create_buttons(self.top_frame, self.main_frame)

        # Text to display beside shooting form image
        self.shooting_text = """When it comes to basketball, it is quite vital that proper shooting techniques are employed. It also aids players in improved accuracy and uniformity of their shots. If you have the right form, there are more baskets because your shots have a better chance of going through. It’s like the starting point of constructing a house, should you lack it, then everything becomes slightly unstable. Common aspects of shooting include factors such as how one grasps the basketball, the positioning of the legs and the manner in which the ball is released. Constant practice of the form makes you improve your shooting ability, which dictates how good a basketball player you will be."""

        self.bicycle_kick_text = """In football, the bicycle kick is among the risky but very impressive moves that fans of the game could always look forward to. Robbed of most of its vigorous expressions, it entails a player jumping and assuming an airborne posture with his back to the goal, and then scoring with a bicycle kick. This is done with great elegance – in fact, it needs great timing, balance, and synchronization hence the very few times one sees it on the soccer playing arena. When well done the spectacular move also draws appreciation of the talents of the footballer as they give the football fans memories that are etched in football history due to the beauty allied to their brass heart to try the impossible."""

        # Display shooting form image and text only if this is the main window
        if not is_sub_window:
            self.display_shooting_content()

        # Start the main loop if this is the main window
        if not root:
            self.root.mainloop()

    def load_images(self):
        # Load and resize images
        self.logo_image = self.resize_image(self.logo_filename, (300, 100))
        self.basketball_image = self.resize_image(self.basketball_filename, (100, 100))
        self.basketball_green_image = self.resize_image(self.basketball_green_filename, (100, 100))
        self.football_image = self.resize_image(self.football_filename, (100, 100))
        self.football_green_image = self.resize_image(self.football_green_filename, (100, 100))
        self.cricket_image = self.resize_image(self.cricket_filename, (100, 100))
        self.cricket_green_image = self.resize_image(self.cricket_green_filename, (100, 100))
        self.shooting_form_image = self.resize_image(self.shooting_form_filename, size=(150, 150))
        self.bicycle_kick_image = self.resize_image(self.bicycle_kick_filename, size=(150, 150))

    def resize_image(self, filepath, size=(100, 100)):
        # Resize image
        img = Image.open(filepath)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def create_buttons(self, top_frame, main_frame):
        # Create logo button
        self.logo_button = Button(top_frame, image=self.logo_image, command=self.return_to_home, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.logo_button.pack(pady=10)

        # Configure columns
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_rowconfigure(3, weight=1)  # Add another row for the bicycle kick image
        main_frame.grid_rowconfigure(4, weight=1)  # Add a row for spacing

        # Create sport buttons
        self.basketball_button = Button(main_frame, image=self.basketball_image, command=self.open_basketball_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.basketball_button.grid(row=0, column=0, padx=10, pady=10)

        self.football_button = Button(main_frame, image=self.football_image, command=self.open_football_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.football_button.grid(row=0, column=1, padx=10, pady=10)

        self.cricket_button = Button(main_frame, image=self.cricket_image, command=self.open_cricket_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.cricket_button.grid(row=0, column=2, padx=10, pady=10)

    def display_shooting_content(self):
        # Create title label for shooting form
        shooting_form_title_label = Label(self.main_frame, text="Shooting Form", bg="black", fg="white", font=("Helvetica", 16))
        shooting_form_title_label.grid(row=1, column=0, columnspan=3, padx=10, pady=0, sticky=S)  # Position the title directly above the image

        # Create label for shooting form image
        shooting_form_label = Label(self.main_frame, image=self.shooting_form_image, bg="black")
        shooting_form_label.grid(row=2, column=0, padx=10, pady=10, sticky=N)  # Position the image below the title

        # Create text widget for shooting text
        shooting_text_widget = Text(self.main_frame, wrap=WORD, bg="black", fg="white", width=25, height=10, padx=10, pady=10, bd=0, relief=FLAT)
        shooting_text_widget.insert(INSERT, self.shooting_text)
        shooting_text_widget.tag_configure("justified", justify=LEFT)
        shooting_text_widget.tag_add("justified", "1.0", "end")
        shooting_text_widget.config(state=DISABLED)  # Make the text widget read-only
        shooting_text_widget.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky=W)

        # Create title label for bicycle kick
        bicycle_kick_title_label = Label(self.main_frame, text="Bicycle Kick", bg="black", fg="white", font=("Helvetica", 16))
        bicycle_kick_title_label.grid(row=3, column=0, columnspan=3, padx=10, pady=0, sticky=S)  # Position the title in the middle above the text and image

        # Create text widget for bicycle kick text
        bicycle_kick_text_widget = Text(self.main_frame, wrap=WORD, bg="black", fg="white", width=25, height=10, padx=10, pady=10, bd=0, relief=FLAT)
        bicycle_kick_text_widget.insert(INSERT, self.bicycle_kick_text)
        bicycle_kick_text_widget.tag_configure("justified", justify=LEFT)
        bicycle_kick_text_widget.tag_add("justified", "1.0", "end")
        bicycle_kick_text_widget.config(state=DISABLED)  # Make the text widget read-only
        bicycle_kick_text_widget.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=E)

        # Create label for bicycle kick image
        bicycle_kick_label = Label(self.main_frame, image=self.bicycle_kick_image, bg="black")
        bicycle_kick_label.grid(row=4, column=2, padx=10, pady=10, sticky=W)

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
            return  # Prevent opening a new window if this is a sub-window
        new_window = Toplevel(self.root)
        new_app = App(new_window, is_sub_window=True)
        new_app.root.title(title)

        if change_basketball_image:
            new_app.basketball_button.config(image=self.basketball_green_image)
        if change_football_image:
            new_app.football_button.config(image=self.football_green_image)
        if change_cricket_image:
            new_app.cricket_button.config(image=self.cricket_green_image)

        self.root.destroy()  # Close the current window

    def return_to_home(self):
        # Return to home screen
        self.root.destroy()
        App.main_app = None
        main_app = App()

if __name__ == "__main__":
    main_app = App()
