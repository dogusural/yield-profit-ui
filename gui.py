import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from yield_calculator import yield_calculator as calc
from PIL import Image, ImageTk
import sys



class yield_gui:
    def __init__(self):
        self.entries = {}
        self.root= None
        self.calculator = None
        self.chart = None
        self.result = None
        self.pixels = 30
        self.background = "white"
        self.pancake_img = ((Image.open("pancake.jpg")).resize((self.pixels, self.pixels), Image.ANTIALIAS))
        self.usd_img = ((Image.open("usd.jpg")).resize((self.pixels, self.pixels), Image.ANTIALIAS))
        self.fields = [ ('scale', 'USD Amount', 50000 , 5, 0), ('scale', 'Harvesting Period (days)',360, 1, 1), ('scale', 'Duration in Years',10, 1, 1) , ('entry',"usd_img", None , None, "28.77") , ('entry', "pancake_img", None , None, "229.35") ]

    def makeform(self):
        self.pancake_img = ImageTk.PhotoImage(self.pancake_img)
        self.usd_img = ImageTk.PhotoImage(self.usd_img)

        for field in self.fields:
            row = tk.Frame(self.root,bg=self.background)
            if field[0] == 'entry':
                if field[1] == 'usd_img':
                    label = tk.Label(row, bg=self.background,image = self.usd_img)
                else:
                    label = tk.Label(row,bg=self.background, image = self.pancake_img)
                entry = tk.Entry(row,width=10)
                entry.insert(0, field[4])
                row.pack(side=tk.TOP, 
                    fill=tk.X, 
                    padx=5, 
                    pady=5)
                label.pack(side=tk.LEFT,fill = "both", expand = "no")
                entry.pack( expand=tk.NO )
                self.entries[field[1]] = entry
            else:
                label = tk.Label(row,bg=self.background, width=22, text=field[1]+": ", anchor='w')
                scale = tk.Scale(row, from_=0, to=field[2],bg=self.background, resolution=field[3], orient=tk.HORIZONTAL)
                scale.set(field[4])
                row.pack(side=tk.TOP, 
                    fill=tk.X, 
                    padx=5, 
                    pady=5)
                label.pack(side=tk.LEFT,fill = "both", expand = "no")
                scale.pack( expand=tk.NO, 
                        fill=tk.X)
                self.entries[field[1]] = scale 

    def exit(self):
        sys.exit()

    def get_values(self):
        if self.chart is not None :
            self.chart.get_tk_widget().pack_forget()
        if self.result is None :
            self.result = tk.Label(self.root,text="0", bg= self.background)
            self.result.pack()

        amount = int(self.entries['USD Amount'].get())
        period = int(self.entries['Harvesting Period (days)'].get())
        duration = int(self.entries['Duration in Years'].get())
        stable_apy = float(self.entries["usd_img"].get())
        cake_apy = float(self.entries["pancake_img"].get())
       
        self.calculator = calc(amount,period,stable_apy,cake_apy,duration)
        data = self.calculator.calculate()
        fig = plt.Figure(figsize=(5,4),dpi=100)
        fig.add_subplot(111).plot(data[1],data[0],marker='')
        self.result.config(text=str(int(data[0][-1])) + ' $')
        self.chart = FigureCanvasTkAgg(fig,self.root)
        self.chart.get_tk_widget().pack()
        


    def run(self):
        self.root = tk.Tk()
        self.root.configure(background=self.background)
        self.root.title('Pancake')
        self.root.geometry("700x700")
        self.root.resizable(width=False, height=False)
        self.makeform()
        row = tk.Frame(self.root)
        dollar_img = Image.open("dollar.jpg")
        dollar_img = dollar_img.resize((50, 24), Image.ANTIALIAS)
        dollar_img = ImageTk.PhotoImage(dollar_img)

        exit_img = Image.open("exit.png")
        exit_img = exit_img.resize((50, 24), Image.ANTIALIAS)
        exit_img = ImageTk.PhotoImage(exit_img)

        tk.Button(self.root, text='Calculate', image = exit_img,command=self.exit).place(x=630,y=650)
        tk.Button(self.root, text='Calculate', image = dollar_img,command=self.get_values).pack(pady=8)
        self.root.mainloop()


gdp = yield_gui()
gdp.run()