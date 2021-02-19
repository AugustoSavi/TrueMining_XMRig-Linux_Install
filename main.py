import pyautogui, time, threading, tkinter
from tkinter import *

root = Tk()


class Application():

    stop_threads = False
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.buttons()
        self.inputs()
        root.mainloop()

    def tela(self):
        self.root.title('True mining')
        self.root.geometry('450x200')
        self.root.resizable(False,False)
    
    def frame(self):
        self.frame = Frame(self.root)
        self.frame.place(relx = 0 , rely = 0,relwidth = 1, relheight = 1)

    def buttons(self):
        #Bottão Start 
        self.btnStart = Button(self.frame, text = 'F9- Start', command = self.start)
        self.btnStart.place ( relx = 0.76, rely = 0.39, width = 100, height = 50)
        
        #Bottão Stop 
        self.btnStop = Button(self.frame, text = 'F10- Stop', command = self.stop)
        self.btnStop.place ( relx = 0.76, rely = 0.68, width = 100, height = 50)
    
    def inputs(self):

        self.labelText = Label(self.frame, text = 'Text:')
        self.labelText.place(relx = 0.01, rely = 0)

        self.textBox = Text(self.frame,height = 10 , width = 40)
        self.textBox.place(relx = 0.02, rely = 0.1)

    def clear(self):
        self.textBox.delete('1.0', END)
         
    def start(self):
        self.startThreading = threading.Thread(target=self.SpamLoop)
        self.startThreading.start()
        
    def SpamLoop(self):
        stringTextBox = self.textBox.get('1.0', END)
        
        splitStringTextBox = stringTextBox.splitlines()

        time.sleep(3.0)
        
        
        for word in splitStringTextBox:
            time.sleep(1.0)
            
            global stop_threads
            if self.stop_threads: 
                break
            
            pyautogui.typewrite(word)
            pyautogui.press('enter')

    def stop(self):
        self.stop_threads = True

    def keyPressed(event):
        if event.keysym == 'F9':
            print('F9')
        
        elif  event.keysym == 'F10':
            print('F10')

    
    root.bind("<Key>", keyPressed)

Application()