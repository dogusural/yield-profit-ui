import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from yield_calculator import yield_calculator as calc
from PIL import Image, ImageTk


class yield_gui:
    def __init__(self):
        self.fields = [ ('scale', 'USD Amount', 50000 , 5, 0), ('scale', 'Harvesting Period (days)',360, 1, 1), ('scale', 'Duration in Years',10, 1, 1) , ('entry', '% APY on stable') , ('entry', '% APY on $CAKE') ]
        self.entries = {}
        self.root= None
        self.calculator = None
        self.chart = None
        self.result = None






    def makeform(self):
        img = Image.open("pancake.jpg")
        img = img.resize((40, 40), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        for field in self.fields:
            row = tk.Frame(self.root)
            if "NONE" in field[1]:
                lab = tk.Label(row, image = img)
            else:
                lab = tk.Label(row, width=22, text=field[1]+": ", anchor='w')

            if field[0] == 'scale':
                scl = tk.Scale(row, from_=0, to=field[2], resolution=field[3], orient=tk.HORIZONTAL)
                scl.set(field[4])
            else:
                scl = tk.Entry(row)
                if "stable" in field[1]:
                    scl.insert(0, "28.77")
                else:
                    scl.insert(0, "229.35")

            row.pack(side=tk.TOP, 
                    fill=tk.X, 
                    padx=5, 
                    pady=5)
            lab.pack(side=tk.LEFT,fill = "both", expand = "no")
            scl.pack(side=tk.RIGHT, 
                    expand=tk.YES, 
                    fill=tk.X)
            self.entries[field[1]] = scl

    def get_values(self):
        if self.chart is not None :
            self.chart.get_tk_widget().pack_forget()
        if self.result is None :
            self.result = tk.Label(self.root,text="0")
            self.result.pack()

        amount = int(self.entries['USD Amount'].get())
        period = int(self.entries['Harvesting Period (days)'].get())
        duration = int(self.entries['Duration in Years'].get())
        stable_apy = float(self.entries['% APY on stable'].get())
        cake_apy = float(self.entries['% APY on $CAKE'].get())
       
        self.calculator = calc(amount,period,stable_apy,cake_apy,duration)
        data = self.calculator.calculate()
        fig = plt.Figure(figsize=(5,4),dpi=100)
        fig.add_subplot(111).plot(data[1],data[0],marker='')
        self.result.config(text=str(int(data[0][-1])) + ' $')
        self.chart = FigureCanvasTkAgg(fig,self.root)
        self.chart.get_tk_widget().pack()
        


    def run(self):
        self.root = tk.Tk()
        self.root.title('Pancake')
        self.root.geometry("700x700")
        self.makeform()
        tk.Button(self.root, text='Calculate', command=self.get_values).pack(pady=8)
        row = tk.Frame(self.root)
        img = Image.open("dollar.jpg")
        img = img.resize((50, 24), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(row, image = img)
        row.pack()
        panel.pack(side = "bottom", fill = "both", expand = "no")




        self.root.mainloop()


gdp = yield_gui()
gdp.run()