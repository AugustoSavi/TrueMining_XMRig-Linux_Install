from src.pages.page import *
from PIL import ImageTk, Image
from src.ImageProcessor import Sprite
import tkinter.font as font

class HomePage(Page):
    def __init__(self, parent):

        # init page/ delete old page
        Page.__init__(self, parent)

        walletAdressLabel = Label(self, text="Wallet Address:")
        walletAdressLabel.place(x=25, y=70)

        walletAdressEntry = Entry(self, width = 40, justify='center')
        walletAdressEntry.place(x=155, y=70)

        startMining = Button(self, text ="Start Mining",
                             height=2, width=12 , bg="#fc8e3f",
                             fg="#fff", borderwidth=0,
                             activebackground="#f7673e", 
                             activeforeground="#fff")
        startMining.place(x= 300, y=350)
        startMiningFont = font.Font(weight="bold")
        startMining['font'] = startMiningFont
