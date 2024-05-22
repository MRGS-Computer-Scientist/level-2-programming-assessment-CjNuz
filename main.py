from tkinter import *


#Main Page
window = Tk()
window.geometry("430x932")
window.title ("SportsX")
window.configure(background="black")
window.resizable(width= False, height=False)

#Frame
top_frame = Frame( background= "grey", width=500, height=150)
top_frame.pack()
main_frame = Frame(background= "black", width=500, height=500)
main_frame.pack()

#button functions
#Basketball Page
def basketball():
    print("You clicked the button!")
#Football Page
def football():
    print("Football")
#Cricket Page
def cricket():
    print("cricket")

#Image
Logo = PhotoImage (file = r"C:\Users\23399\OneDrive - Mt Roskill Grammar School\Pictures\Screenshots\sportsxlogo.jpg")
#Image size
Logo = Logo.subsample(3,3)

#buttons
basketball_button = Button(main_frame, text= "🏀", command=basketball, font=("Roboto", 38), width=3, height=1, compound="left")

football_button = Button(main_frame, text= "⚽", command=football, font=("Roboto", 38), width=3, height=1, compound="right")

cricket_button = Button(main_frame, text= "🏏", command=cricket, font=("Roboto", 38), width=3, height=1, compound="right")


#button packs
basketball_button.grid(row=0, column=0, padx=18, pady=150)
football_button.grid(row=0, column=1, padx=30, pady=150)
cricket_button.grid(row=0, column=2, padx=20, pady=150)

#run
window.mainloop()




