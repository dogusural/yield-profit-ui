from PIL import Image, ImageTk
import tkinter as tk



root = tk.Tk()
row = tk.Frame(root)
img = Image.open("pancake.jpg")
img = img.resize((40, 40), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
tk.Label(row, image = img).pack()
row.pack()

row = tk.Frame(root)
img = Image.open("pancake.jpg")
img = img.resize((40, 40), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = tk.Label(row, image = img)
row.pack()
panel.pack(side = "bottom", fill = "both", expand = "no")

# row = tk.Frame(root)
# img = Image.open("dollar.jpg")
# img = img.resize((40, 40), Image.ANTIALIAS)
# img = ImageTk.PhotoImage(img)
# panel = tk.Label(row, image = img)
# row.pack()
# panel.pack(side = "bottom", fill = "both", expand = "no")

root.mainloop()