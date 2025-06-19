import random
from tkinter import *
import string

def generate_password():
   password = []
   for i in range(5):
      alpha = random.choice(string.ascii_letters)
      symbol = random.choice(string.punctuation)
      password.append(alpha)
      password.append(symbol)
      password.append(numbers := random.choice(string.digits))

   y = "".join(str(i) for x in password)
   lbl.config(text=y)

root = Tk()
root.title("Password generator")
root.geometry("250x200")
btn = Button(root, text="Generate Password", command=generate_password)
btn.grid(row=2,column=2)
lbl = Label(root, font=("times",15,"bold"))
lbl.grid(row=4,column=2)
root.mainloop()