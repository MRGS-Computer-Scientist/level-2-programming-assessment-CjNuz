from tkinter import *
from PIL import Image, ImageTk
from os import path

class App:
    main_app = None  # Main app instance

    def __init__(self, root=None, is_sub_window=False):
        self.is_sub_window = is_sub_window # Flag to indicate if this instance is a sub-window or main window
        self.root = root if root else Tk() # Set the root window to the provided root or create a new Tkinter window if none is provided
        if not App.main_app:
            App.main_app = self  # Set main app instance

        # Window properties
        self.root.geometry("480x932")  # Set window size
        self.root.title("SportsX")  # Set window title
        self.root.configure(background="black")  # Set background color
        self.root.resizable(width=False, height=False)  # Disable window resizing

        # Create frames
        self.top_frame = Frame(self.root, background="black", width=430, height=100)
        self.top_frame.pack_propagate(False)  # Prevent frame from resizing to fit content
        self.main_frame = Frame(self.root, background="black", width=430, height=600)

        # Pack frames
        self.top_frame.pack(side=TOP, fill=BOTH)
        self.main_frame.pack(side=TOP, fill=BOTH)

        # Image file paths
        dirname = path.dirname(__file__)  # Get current directory
        self.logo_filename = path.join(dirname, 'Images/sportsxlogo.jpg')  # Logo image path
        self.basketball_filename = path.join(dirname, 'Images/Basketball_grey.png')  # Basketball image path
        self.basketball_green_filename = path.join(dirname, 'Images/Basketball_green.png')  # Basketball green image path
        self.football_filename = path.join(dirname, 'Images/Football_grey.png')  # Football image path
        self.football_green_filename = path.join(dirname, 'Images/Football_green.png')  # Football green image path
        self.cricket_filename = path.join(dirname, 'Images/Cricket_grey.png')  # Cricket image path
        self.cricket_green_filename = path.join(dirname, 'Images/Cricket_green.png')  # Cricket green image path
        self.shooting_form_filename = path.join(dirname, 'Images/Shooting-form.png')  # Shooting form image path
        self.bicycle_kick_filename = path.join(dirname, 'Images/Bicyclekick.jpg')  # Bicycle kick image path
        self.donald_filename = path.join(dirname, 'Images/Donald.png')  # Donald image path

        # Load images and create buttons
        self.load_images()  # Load all images
        self.create_buttons(self.top_frame, self.main_frame)  # Create buttons for sports

        # Text to display beside shooting form image
        self.shooting_text = """When it comes to basketball, it is quite vital that proper shooting techniques are employed. It also aids players in improved accuracy and uniformity of their shots. If you have the right form, there are more baskets because your shots have a better chance of going through. It’s like the starting point of constructing a house, should you lack it, then everything becomes slightly unstable. Common aspects of shooting include factors such as how one grasps the basketball, the positioning of the legs and the manner in which the ball is released. Constant practice of the form makes you improve your shooting ability, which dictates how good a basketball player you will be."""

        self.bicycle_kick_text = """In football, the bicycle kick is among the risky but very impressive moves that fans of the game could always look forward to. Robbed of most of its vigorous expressions, it entails a player jumping and assuming an airborne posture with his back to the goal, and then scoring with a bicycle kick. This is done with great elegance – in fact, it needs great timing, balance, and synchronization hence the very few times one sees it on the soccer playing arena. When well done the spectacular move also draws appreciation of the talents of the footballer as they give the football fans memories that are etched in football history due to the beauty allied to their brass heart to try the impossible."""

        self.donald_text = """Over the years, many legends have graced the field of cricket but none can MATCH the genius of Sir Donald Bradman whose legacy continues to be felt even in the present era. Bradman – arguably the best batsman of the age, was born on November 27, 1908, in New South Wales, Australia. His career batting average of 99 in Test cricket remains unmatched. Bradman's unparalleled skill and determination set him apart as a player who dominated his era, controlling bowlers with his exceptional technique and focus. Beyond his statistical achievements, Bradman symbolizes the essence of cricketing culture and is revered for his enduring impact on the sport."""

        # Display shooting form image and text only if this is the main window
        if not is_sub_window:
            self.display_sports_content()

        # Start the main loop if this is the main window
        if not root:
            self.root.mainloop()

    def load_images(self):
        # Load and resize images
        self.logo_image = self.resize_image(self.logo_filename, (300, 100))  # Load and resize logo image
        self.basketball_image = self.resize_image(self.basketball_filename, (100, 100))  # Load and resize basketball image
        self.basketball_green_image = self.resize_image(self.basketball_green_filename, (100, 100))  # Load and resize green basketball image
        self.football_image = self.resize_image(self.football_filename, (100, 100))  # Load and resize football image
        self.football_green_image = self.resize_image(self.football_green_filename, (100, 100))  # Load and resize green football image
        self.cricket_image = self.resize_image(self.cricket_filename, (100, 100))  # Load and resize cricket image
        self.cricket_green_image = self.resize_image(self.cricket_green_filename, (100, 100))  # Load and resize green cricket image
        self.shooting_form_image = self.resize_image(self.shooting_form_filename, size=(150, 150))  # Load and resize shooting form image
        self.bicycle_kick_image = self.resize_image(self.bicycle_kick_filename, size=(150, 150))  # Load and resize bicycle kick image
        self.donald_image = self.resize_image(self.donald_filename, size=(150, 150))  # Load and resize Donald image

    def resize_image(self, filepath, size=(100, 100)):
        # Resize image to specified size
        img = Image.open(filepath)  # Open image file
        img = img.resize(size, Image.LANCZOS)  # Resize image with Lanczos filter
        return ImageTk.PhotoImage(img)  # Return resized image as PhotoImage

    def create_buttons(self, top_frame, main_frame):
        # Create logo button
        self.logo_button = Button(top_frame, image=self.logo_image, command=self.return_to_home, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.logo_button.pack(pady=10)  # Add logo button to top frame with padding

        # Configure columns and rows for main frame
        main_frame.grid_columnconfigure(0, weight=1)  # Column 0 grows with window size
        main_frame.grid_columnconfigure(1, weight=1)  # Column 1 grows with window size
        main_frame.grid_columnconfigure(2, weight=1)  # Column 2 grows with window size
        main_frame.grid_rowconfigure(0, weight=1)  # Row 0 grows with window size
        main_frame.grid_rowconfigure(1, weight=1)  # Row 1 grows with window size
        main_frame.grid_rowconfigure(2, weight=1)  # Row 2 grows with window size
        main_frame.grid_rowconfigure(3, weight=1)  # Row 3 grows with window size
        main_frame.grid_rowconfigure(4, weight=1)  # Row 4 grows with window size
        main_frame.grid_rowconfigure(5, weight=1)  # Row 5 grows with window size

        # Create sport buttons
        self.basketball_button = Button(main_frame, image=self.basketball_image, command=self.open_basketball_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.basketball_button.grid(row=0, column=0, padx=10, pady=10)  # Add basketball button to main frame

        self.football_button = Button(main_frame, image=self.football_image, command=self.open_football_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.football_button.grid(row=0, column=1, padx=10, pady=10)  # Add football button to main frame

        self.cricket_button = Button(main_frame, image=self.cricket_image, command=self.open_cricket_window, highlightthickness=0, bd=0, bg="black", activebackground="black")
        self.cricket_button.grid(row=0, column=2, padx=10, pady=10)  # Add cricket button to main frame

    def display_sports_content(self):
        # Display shooting form content
        shooting_form_title_label = Label(self.main_frame, text="Shooting Form", bg="black", fg="white", font=("Helvetica", 16))
        shooting_form_title_label.grid(row=1, column=0, columnspan=3, padx=10, pady=0, sticky=W)  # Add title label for shooting form

        shooting_form_label = Label(self.main_frame, image=self.shooting_form_image, bg="black")
        shooting_form_label.grid(row=2, column=0, padx=10, pady=10, sticky=N)  # Add image for shooting form

        shooting_text_widget = Text(self.main_frame, wrap=WORD, bg="black", fg="white", width=25, height=10, padx=10, pady=10, bd=0, relief=FLAT)
        shooting_text_widget.insert(INSERT, self.shooting_text)  # Add text for shooting form
        shooting_text_widget.tag_configure("justified", justify=LEFT)
        shooting_text_widget.tag_add("justified", "1.0", "end")
        shooting_text_widget.config(state=DISABLED)  # Make text widget read-only
        shooting_text_widget.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky=W)

        # Display bicycle kick content
        bicycle_kick_title_label = Label(self.main_frame, text="Bicycle Kick", bg="black", fg="white", font=("Helvetica", 16))
        bicycle_kick_title_label.grid(row=3, column=0, columnspan=3, padx=10, pady=0, sticky=E)
        bicycle_kick_text_widget = Text(self.main_frame, wrap=WORD, bg="black", fg="white", width=25, height=10, padx=10, pady=10, bd=0, relief=FLAT)
        bicycle_kick_text_widget.insert(INSERT, self.bicycle_kick_text)  # Add text for bicycle kick
        bicycle_kick_text_widget.tag_configure("justified", justify=LEFT)
        bicycle_kick_text_widget.tag_add("justified", "1.0", "end")
        bicycle_kick_text_widget.config(state=DISABLED)  # Make text widget read-only
        bicycle_kick_text_widget.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=E)

        bicycle_kick_label = Label(self.main_frame, image=self.bicycle_kick_image, bg="black")
        bicycle_kick_label.grid(row=4, column=2, padx=10, pady=10, sticky=W)  # Add image for bicycle kick

        # Display Donald Bradman content
        donald_title_label = Label(self.main_frame, text="Donald Bradman", bg="black", fg="white", font=("Helvetica", 16))
        donald_title_label.grid(row=5, column=0, columnspan=3, padx=10, pady=0, sticky=W)

        donald_label = Label(self.main_frame, image=self.donald_image, bg="black")
        donald_label.grid(row=6, column=0, padx=10, pady=10, sticky=W)  # Add image for Donald Bradman

        donald_text_widget = Text(self.main_frame, wrap=WORD, bg="black", fg="white", width=25, height=10, padx=10, pady=10, bd=0, relief=FLAT)
        donald_text_widget.insert(INSERT, self.donald_text)  # Add text for Donald Bradman
        donald_text_widget.tag_configure("justified", justify=LEFT)
        donald_text_widget.tag_add("justified", "1.0", "end")
        donald_text_widget.config(state=DISABLED)  # Make text widget read-only
        donald_text_widget.grid(row=6, column=1, columnspan=2, padx=10, pady=10, sticky=W)

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
        # Open new window and optionally change button images
        current_window = self.root
        new_window = Toplevel(current_window)
        new_app = App(new_window, is_sub_window=True)
        new_app.root.title(title)

        if change_basketball_image:
            new_app.basketball_button.config(image=self.basketball_green_image)
        if change_football_image:
            new_app.football_button.config(image=self.football_green_image)
        if change_cricket_image:
            new_app.cricket_button.config(image=self.cricket_green_image)

        current_window.withdraw()  # Hide the current window

    def return_to_home(self):
        # Return to home screen from sub-window
        self.root.withdraw()
        if App.main_app:
            App.main_app.root.deiconify()

if __name__ == "__main__":
    main_app = App()

