import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from yield_calculator import yield_calculator as calc
from PIL import Image, ImageTk
import sys

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

master = tk.Tk()

variable = tk.StringVar(master)
variable.set(OPTIONS[0]) # default value


dollar_img = Image.open("dollar.jpg")
dollar_img = dollar_img.resize((50, 24), Image.ANTIALIAS)
dollar_img = ImageTk.PhotoImage(dollar_img)

label = tk.Label(master,image = dollar_img)



w = tk.OptionMenu(master, label, *OPTIONS)
w.pack()

def ok():
    print ("value is:" + str(type(variable.get())))

button = tk.Button(master, text="OK", command=ok)
button.pack()

tk.mainloop()