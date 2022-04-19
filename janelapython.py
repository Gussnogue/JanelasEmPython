
from tkinter import *
from turtle import bgcolor

janela_numeroum = Tk()

janela_numeroum.title("janeladegustavo")

janela_numeroum.geometry("550x350+205+205")

janela_numeroum.resizable(True, True)

janela_numeroum.minsize(400, 200)

janela_numeroum.maxsize(800,600)

janela_numeroum.state("zoomed")

janela_numeroum.state("iconic")

janela_numeroum["bg"] = "red"

janela_numeroum.mainloop()