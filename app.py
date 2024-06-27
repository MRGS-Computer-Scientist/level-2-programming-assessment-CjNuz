from tkinter import *
from PIL import Image, ImageTk
from os import path
import webbrowser

class App:
    main_app = None  # Main app instance

    def __init__(self, root=None, is_sub_window=False):
        self.is_sub_window = is_sub_window  # Flag to indicate if this instance is a sub-window or main window
        self.root = root if root else Tk()  # Set the root window to the provided root or create a new Tkinter window if none is provided
        if not App.main_app:
            App.main_app = self  # Set main app instance

        # Window properties
        self.root.geometry("480x932+100+100")  # Set window size, "100+100" makes the window stays in place 
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
        self.dirname = path.dirname(__file__)  # Get current directory
        self.logo_filename = path.join(self.dirname, 'Images/sportsxlogo.jpg')  # Logo image path
        self.basketball_filename = path.join(self.dirname, 'Images/Basketball_grey.png')  # Basketball image path
        self.basketball_green_filename = path.join(self.dirname, 'Images/Basketball_green.png')  # Basketball green image path
        self.football_filename = path.join(self.dirname, 'Images/Football_grey.png')  # Football image path
        self.football_green_filename = path.join(self.dirname, 'Images/Football_green.png')  # Football green image path
        self.cricket_filename = path.join(self.dirname, 'Images/Cricket_grey.png')  # Cricket image path
        self.cricket_green_filename = path.join(self.dirname, 'Images/Cricket_green.png')  # Cricket green image path
        self.shooting_form_filename = path.join(self.dirname, 'Images/Shooting-form.png')  # Shooting form image path
        self.bicycle_kick_filename = path.join(self.dirname, 'Images/Bicyclekick.jpg')  # Bicycle kick image path
        self.donald_filename = path.join(self.dirname, 'Images/Donald.png')  # Donald image path

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

        # Placeholder images for famous basketball players
        self.lebron_james_image = self.resize_image(path.join(self.dirname, 'Images/Lebron.png'), size=(50, 50))
        self.kobe_bryant_image = self.resize_image(path.join(self.dirname, 'Images/Kobe_Bryant_2014.jpg'), size=(50, 50))
        self.magic_johnson_image = self.resize_image(path.join(self.dirname, 'Images/Magic-Johnson.png'), size=(50, 50))
        self.larry_bird_image = self.resize_image(path.join(self.dirname, 'Images/LarryBird.png'), size=(50, 50))
        self.shaquille_oneal_image = self.resize_image(path.join(self.dirname, 'Images/Shaq.png'), size=(50, 50))
        self.tim_duncan_image = self.resize_image(path.join(self.dirname, 'Images/TimDuncan.jpg'), size=(50, 50))


        # Placeholder images for football techniques
        self.passing_image = self.resize_image(path.join(self.dirname, 'Images/Passing.png'), size=(50, 50))
        self.dribbling_image = self.resize_image(path.join(self.dirname, 'Images/Dribbling.png'), size=(50, 50))
        self.shooting_image = self.resize_image(path.join(self.dirname, 'Images/Shooting.png'), size=(50, 50))
        self.defending_image = self.resize_image(path.join(self.dirname, 'Images/Defending.png'), size=(50, 50))
        self.heading_image = self.resize_image(path.join(self.dirname, 'Images/Heading.png'), size=(50, 50))
        self.tackling_image = self.resize_image(path.join(self.dirname, 'Images/Tackling.png'), size=(50, 50))
        self.ball_control_image = self.resize_image(path.join(self.dirname, 'Images/Ball_Control.png'), size=(50, 50))

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
            new_app.display_basketball_content()
        if change_football_image:
            new_app.football_button.config(image=self.football_green_image)
            new_app.display_football_content()
        if change_cricket_image:
            new_app.cricket_button.config(image=self.cricket_green_image)
            new_app.display_cricket_content()

        current_window.withdraw()  # Hide the current window

    def return_to_home(self):
        # Return to home screen from sub-window
        self.root.withdraw()
        if App.main_app:
            App.main_app.root.deiconify()

    def display_basketball_content(self):
        def open_google_search(player_name):
            url = f"https://www.google.com/search?q={player_name.replace(' ', '+')}"
            webbrowser.open(url)

        # Clear existing content in main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Basketball rules
        rules_frame = Frame(self.main_frame, bg="black")
        rules_frame.pack(fill=X, padx=10, pady=5)

        rules_title_label = Label(rules_frame, text="Basketball Rules", bg="black", fg="white", font=("Helvetica", 16))
        rules_title_label.pack(anchor=W, pady=(10, 0))

        rules_text = """1. The game is played with two teams of five players each.\n
2. The objective is to score by shooting the ball through the opponent's hoop.\n
3. The game is played in four quarters of 12 minutes each.\n
4. A shot made from beyond the three-point line is worth three points.\n
5. The team with the most points at the end of the game wins.\n
6. Players cannot run with the ball without dribbling it.\n
7. Physical contact is generally not allowed, with different levels of fouls and penalties applied for violations.\n
8. A free throw is awarded after certain fouls and is worth one point each."""

        rules_text_widget = Text(rules_frame, wrap=WORD, bg="black", fg="white", padx=10, pady=10, bd=0, relief=FLAT, font=("Helvetica", 12), height=8)
        rules_text_widget.insert(INSERT, rules_text)
        rules_text_widget.config(state=DISABLED)
        rules_text_widget.pack(anchor=W, pady=(0, 10))

        # Famous basketball players
        players_frame = Frame(self.main_frame, bg="black")
        players_frame.pack(fill=X, padx=10, pady=5)

        players_title_label = Label(players_frame, text="Famous Basketball Players", bg="black", fg="white", font=("Helvetica", 16))
        players_title_label.pack(anchor=W, pady=(10, 0))

        players = [
            ("LeBron James", self.lebron_james_image),
            ("Kobe Bryant", self.kobe_bryant_image),
            ("Magic Johnson", self.magic_johnson_image),
            ("Larry Bird", self.larry_bird_image),
            ("Shaquille O'Neal", self.shaquille_oneal_image),
            ("Tim Duncan", self.tim_duncan_image),
        ]

        for player, image in players:
            player_frame = Frame(players_frame, bg="black")
            player_frame.pack(fill=X, pady=2)

            player_image_label = Label(player_frame, image=image, bg="black")
            player_image_label.pack(side=LEFT, padx=(0, 10))

            player_label = Label(player_frame, text=player, bg="black", fg="white", font=("Helvetica", 12), cursor="hand2")
            player_label.pack(side=LEFT, anchor=W)
            player_label.bind("<Button-1>", lambda e, p=player: open_google_search(p))

        # Basketball Techniques
        techniques_frame = Frame(self.main_frame, bg="black")
        techniques_frame.pack(fill=X, padx=10, pady=5)

        techniques_title_label = Label(techniques_frame, text="Basketball Techniques", bg="black", fg="white", font=("Helvetica", 16))
        techniques_title_label.pack(anchor=W, pady=(10, 0))

        techniques_text = """1. Passing: Use crisp chest passes or bounce passes to move the ball efficiently.\n
2. Dribbling: Keep the ball low, use your fingertips for control, and change pace to keep defenders guessing.\n
3. Shooting: Square your body to the hoop, follow through with your shooting hand, and aim for the back of the rim.\n
4. Rebounding: Box out opponents, anticipate the ball's trajectory, and use both hands to secure the rebound.\n
5. Defense: Maintain a low stance, stay between your opponent and the basket, and contest shots without fouling."""

        techniques_text_widget = Text(techniques_frame, wrap=WORD, bg="black", fg="white", padx=10, pady=10, bd=0, relief=FLAT, font=("Helvetica", 12), height=8)
        techniques_text_widget.insert(INSERT, techniques_text)
        techniques_text_widget.config(state=DISABLED)
        techniques_text_widget.pack(anchor=W, pady=(0, 10))

    def display_football_content(self):
        # Clear existing content in main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Football techniques and form
        techniques_frame = Frame(self.main_frame, bg="black")
        techniques_frame.pack(fill=X, padx=10, pady=5)

        techniques_title_label = Label(techniques_frame, text="Football Techniques & Form", bg="black", fg="white", font=("Helvetica", 16))
        techniques_title_label.pack(anchor=W, pady=(10, 0))

        techniques = [
            ("Passing", self.passing_image, "Use the inside of your foot for accuracy."),
            ("Dribbling", self.dribbling_image, "Keep the ball close to your feet and use both feet."),
            ("Shooting", self.shooting_image, "Plant your non-kicking foot beside the ball, keep your head down and follow through."),
            ("Defending", self.defending_image, "Stay low, keep your eyes on the ball, and use your body to block the opponent."),
            ("Heading", self.heading_image, "Use your forehead, keep your eyes open, and time your jump."),
            ("Tackling", self.tackling_image, "Use the side tackle sparingly, focus on timing and positioning."),
            ("Ball Control", self.ball_control_image, "Cushion the ball with your foot, thigh, or chest to bring it under control."),
        ]

        for technique, image, description in techniques:
            technique_frame = Frame(techniques_frame, bg="black")
            technique_frame.pack(fill=X, pady=2, padx=10)

            technique_image_label = Label(technique_frame, image=image, bg="black")
            technique_image_label.pack(side=LEFT, padx=(0, 10))

            text_frame = Frame(technique_frame, bg="black")
            text_frame.pack(side=LEFT, fill=X)

            technique_label = Label(text_frame, text=technique, bg="black", fg="white", font=("Helvetica", 12))
            technique_label.pack(anchor=W)

            description_label = Label(text_frame, text=description, bg="black", fg="white", font=("Helvetica", 12), wraplength=300, justify=LEFT)
            description_label.pack(anchor=W)

        # Football Rules
        rules_frame = Frame(self.main_frame, bg="black")
        rules_frame.pack(fill=X, padx=10, pady=5)

        rules_title_label = Label(rules_frame, text="Football Rules", bg="black", fg="white", font=("Helvetica", 16))
        rules_title_label.pack(anchor=W, pady=(10, 0))

        rules_text = """1. The game is played with two teams of eleven players each.\n
2. The objective is to score by getting the ball into the opponent's goal.\n
3. The game is played in two halves of 45 minutes each.\n
4. A goal is worth one point.\n
5. The team with the most points at the end of the game wins.\n
6. Players cannot use their hands or arms to play the ball, except the goalkeeper within the penalty area.\n
7. Offside rule: A player is offside if they are closer to the opponent's goal line than both the ball and the second last opponent when the ball is played to them.\n
8. Fouls and misconduct are penalized by free kicks, yellow cards, or red cards.\n
9. A penalty kick is awarded for certain fouls committed inside the penalty area.\n
10. The game is supervised by a referee with the authority to enforce the rules and ensure fair play."""

        rules_text_widget = Text(rules_frame, wrap=WORD, bg="black", fg="white", padx=10, pady=10, bd=0, relief=FLAT, font=("Helvetica", 12), height=8)
        rules_text_widget.insert(INSERT, rules_text)
        rules_text_widget.config(state=DISABLED)
        rules_text_widget.pack(anchor=W, pady=(0, 10))

        # Add quiz button
        quiz_button = Button(self.main_frame, text="Take Football Quiz", command=self.start_quiz, bg="black", fg="white", font=("Helvetica", 16))
        quiz_button.pack(pady=20)


    def display_cricket_content(self):
        # Clear existing content in main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Cricket rules
        rules_frame = Frame(self.main_frame, bg="black")
        rules_frame.pack(fill=X, padx=10, pady=5)

        rules_title_label = Label(rules_frame, text="Cricket Rules", bg="black", fg="white", font=("Helvetica", 16))
        rules_title_label.pack(anchor=W, pady=(10, 0))

        rules_text = """1. Cricket is played between two teams of eleven players each.\n
2. The game is played on a circular or oval-shaped field with a 22-yard pitch in the center.\n
3. The objective is to score runs by hitting the ball and running between the wickets.\n
4. A run is scored each time the batsmen successfully run to the opposite end of the pitch.\n
5. The game can be played in different formats: Test cricket (5 days), One-Day Internationals (50 overs per side), and T20 Internationals (20 overs per side).\n
6. The team with the most runs at the end of the match wins.\n
7. A bowler delivers the ball overarm to the batsman, aiming to get them out.\n
8. There are several ways a batsman can be out: bowled, caught, leg before wicket (LBW), run out, stumped, and hit wicket.\n
9. The fielding team tries to prevent runs by catching the ball, throwing it to the wicket, or stopping it with their body.\n
10. The game is supervised by two on-field umpires who ensure the rules are followed and make decisions on dismissals."""

        rules_text_widget = Text(rules_frame, wrap=WORD, bg="black", fg="white", padx=10, pady=10, bd=0, relief=FLAT, font=("Helvetica", 12), height=8)
        rules_text_widget.insert(INSERT, rules_text)
        rules_text_widget.config(state=DISABLED)
        rules_text_widget.pack(anchor=W, pady=(0, 10))

        # Cricket techniques
        techniques_frame = Frame(self.main_frame, bg="black")
        techniques_frame.pack(fill=X, padx=10, pady=5)

        techniques_title_label = Label(techniques_frame, text="Cricket Techniques", bg="black", fg="white", font=("Helvetica", 16))
        techniques_title_label.pack(anchor=W, pady=(10, 0))

        techniques_text = """1. Batting: Stand sideways, keep your eyes on the ball, and use a straight bat.\n
2. Bowling: Keep your arm straight, follow through, and aim for the stumps.\n
3. Fielding: Stay low, keep your eyes on the ball, and use two hands to catch.\n
4. Wicketkeeping: Stay low, keep your gloves close to the stumps, and move quickly.\n
5. Running between wickets: Run in straight lines, communicate with your partner, and slide your bat into the crease.\n
6. Spin Bowling: Use your fingers or wrist to impart spin on the ball.\n
7. Fast Bowling: Use a strong run-up, high arm action, and follow through with your body.\n
8. Catching: Keep your eyes on the ball, cushion the catch with soft hands, and follow through with your body."""

        techniques_text_widget = Text(techniques_frame, wrap=WORD, bg="black", fg="white", padx=10, pady=10, bd=0, relief=FLAT, font=("Helvetica", 12), height=8)
        techniques_text_widget.insert(INSERT, techniques_text)
        techniques_text_widget.config(state=DISABLED)
        techniques_text_widget.pack(anchor=W, pady=(0, 10))

        # Interesting cricket facts
        facts_frame = Frame(self.main_frame, bg="black")
        facts_frame.pack(fill=X, padx=10, pady=5)

        facts_title_label = Label(facts_frame, text="Interesting Cricket Facts", bg="black", fg="white", font=("Helvetica", 16))
        facts_title_label.pack(anchor=W, pady=(10, 0))

        facts_text = """- The longest cricket match was played for 14 days in 1939 between England and South Africa.\n
- Sachin Tendulkar is the only player to have scored 100 international centuries.\n
- The highest individual score in a Test match is 400 not out, scored by Brian Lara.\n
- Cricket was played for the first time in the Olympic Games in 1900.\n
- The first ever Test match was played between England and Australia in 1877."""

        facts_text_widget = Text(facts_frame, wrap=WORD, bg="black", fg="white", padx=10, pady=10, bd=0, relief=FLAT, font=("Helvetica", 12), height=8)
        facts_text_widget.insert(INSERT, facts_text)
        facts_text_widget.config(state=DISABLED)
        facts_text_widget.pack(anchor=W, pady=(0, 10))

    def start_quiz(self):
        self.quiz_questions = [
            {"question": "Which country won the first World Cup in 1930?", "options": ["Brazil", "Germany", "Uruguay", "Argentina"], "answer": "Uruguay"},
            {"question": "Who is known as the King of Football?", "options": ["Pelé", "Maradona", "Messi", "Ronaldo"], "answer": "Pelé"},
            {"question": "Which country has won the most World Cups?", "options": ["Brazil", "Germany", "Italy", "Argentina"], "answer": "Brazil"},
            {"question": "Who scored the Hand of God goal?", "options": ["Pelé", "Maradona", "Messi", "Ronaldo"], "answer": "Maradona"},
            {"question": "Which country hosted the 2018 World Cup?", "options": ["Brazil", "Russia", "Qatar", "Germany"], "answer": "Russia"}
        ]
        self.quiz_index = 0
        self.quiz_score = 0

        self.display_quiz_question()

    def display_quiz_question(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        question_data = self.quiz_questions[self.quiz_index]
        question_label = Label(self.main_frame, text=question_data["question"], bg="black", fg="white", font=("Helvetica", 16))
        question_label.pack(pady=20)

        self.quiz_var = StringVar(value="")

        for option in question_data["options"]:
            radio_button = Radiobutton(self.main_frame, text=option, variable=self.quiz_var, value=option, bg="black", fg="white", font=("Helvetica", 14), selectcolor="black")
            radio_button.pack(anchor=W, padx=20, pady=5)

        next_button = Button(self.main_frame, text="Next", command=self.check_answer, bg="black", fg="white", font=("Helvetica", 16))
        next_button.pack(pady=20)

    def check_answer(self):
        if self.quiz_var.get() == self.quiz_questions[self.quiz_index]["answer"]:
            self.quiz_score += 1

        self.quiz_index += 1
        if self.quiz_index < len(self.quiz_questions):
            self.display_quiz_question()
        else:
            self.display_quiz_result()

    def display_quiz_result(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        result_label = Label(self.main_frame, text=f"Quiz Over! Your score: {self.quiz_score}/{len(self.quiz_questions)}", bg="black", fg="white", font=("Helvetica", 16))
        result_label.pack(pady=20)

        restart_button = Button(self.main_frame, text="Restart Quiz", command=self.start_quiz, bg="red", fg="white", font=("Helvetica", 16))
        restart_button.pack(pady=10)

        home_button = Button(self.main_frame, text="Back to Home", command=self.return_to_home, bg="green", fg="white", font=("Helvetica", 16))
        home_button.pack(pady=10)

if __name__ == "__main__":
    main_app = App()
