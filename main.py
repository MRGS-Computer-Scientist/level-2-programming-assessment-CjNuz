from tkinter import *

#Main Page
window = Tk()
window.geometry("430x932")
window.title ("SportsX")
window.configure(background="black")

#button functions
def basketball():
    print("You clicked the button!")

#style

#buttons
button = Button(window, text= "🏀", command=basketball, font=("Roboto", 38))
button.pack(pady=50)

#run
window.mainloop()

#Basketball Page
#Football Page
#Cricket Page
#images
photo = PhotoImage()