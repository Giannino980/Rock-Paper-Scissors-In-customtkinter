import customtkinter as ctk
import random


Elements = ["Rock" , "Paper" , "Scissors"]
Choose_bot = random.choice(Elements)

def select_rock():
    global Choose_bot
    if Choose_bot == "Scissors":
        Text.configure(text=f"The Enemy Has Choose\n {Choose_bot} YOU WON!!!!")

    elif Choose_bot == "Rock":
         Text.configure(text=f"The Enemy Has Choose\n {Choose_bot} PAIR!!")

    else:
         Text.configure(text=f"The Enemy Has Choose\n {Choose_bot} You lost :(")



def select_Paper():
    global Choose_bot
    if Choose_bot == "Rock":
        Text.configure(text=f"The Enemy Has Choose\n {Choose_bot} YOU WON!!!!")

    elif Choose_bot == "Paper":
         Text.configure(text=f"The Enemy Has Choose\n {Choose_bot} PAIR!!")

    else:
         Text.configure(text=f"The Enemy Has Choose\n {Choose_bot} You lost :(")

def select_scissors():
    global Choose_bot
    if Choose_bot == "Paper":
        Text.configure(text=f"The Enemy Has Choose\n {Choose_bot} YOU WON!!!!")

    elif Choose_bot == "Scissors":
         Text.configure(text=f"The Enemy Has Choose\n {Choose_bot} PAIR!!")

    else:
         Text.configure(text=f"The Enemy Has Choose\n {Choose_bot} You lost :(")

def restart_game():
     global Choose_bot
     global Elements
     Choose_bot = random.choice(Elements)
     Text.configure(text="Select Rock Paper or Scissors")


     















ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

font = ("Liberation mono" ,25, "bold")
font_keys = ("Liberation mono" ,30, "bold")


root = ctk.CTk()
root.geometry("500x400")
root.resizable(False , False)
root.title("Rock Paper Scissors")

Text = ctk.CTkLabel(master=root , text="Select Rock Paper or Scissors" , font=(font))
Text.pack()

rock = ctk.CTkButton(master=root , text="Rock" , font=(font_keys) , width=110 , command=select_rock)
rock.place(y=150 , x=10)

paper = ctk.CTkButton(master=root , text="Paper" , font=(font_keys) , width=110 , command=select_Paper)
paper.place(y=150 , x=180)

scissors= ctk.CTkButton(master=root , text="Scissors" , font=(font_keys) , width=110 , command=select_scissors)
scissors.place(y=150 , x=330)

restart = ctk.CTkButton(master=root , text="Restart" , font=(font_keys) , width=110 , command=restart_game)
restart.place(y=300 , x=180)







root.mainloop()
