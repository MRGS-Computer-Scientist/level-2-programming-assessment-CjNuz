from tkinter import *

#Main Page
window = Tk()
window.geometry("430x932")
window.title ("SportsX")
window.configure(background="black")

#button functions
def basketball():
    print("You clicked the button!")

# Load the image
#basketball_image = PhotoImage(file=r"C:\Users\23399\OneDrive - Mt Roskill Grammar School\Pictures\basketball_logo_orange_ball.jpg")
#style
#image=basketball_image
#buttons
button = Button(window, text= "🏀", command=basketball, font=("Roboto", 38), width=3, height=1, compound="left")
button.pack(anchor="w", padx=20, pady=150)
button = Button(window, text= "⚽", command=basketball, font=("Roboto", 38), width=3, height=1, compound="left")
button.pack(anchor="w", pady=90, padx=150)

#run
window.mainloop()

#Basketball Page
#Football Page
#Cricket Page
