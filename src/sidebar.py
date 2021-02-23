from tkinter import *
from src.ImageProcessor import *
from src.scrollbar import *

side_bar_tab_list = []


class SideBar(ScrollBar):
    def __init__(self, parent, *args, **kwargs):
        ScrollBar.__init__(self, parent)
    def finish(self):
        self.select_first_tab()
        if len(ScrollOnItemsList) < 14:
            i = len(ScrollOnItemsList)
            index = 14 - i
            for i in range(index):
                Spacer(self.scrollframe, "")

    def add_spacer(self, text):
        Spacer(self.scrollframe, text)

    def add_button(self, text, command, icon=None, tab=True):
        SideBarButton(self.scrollframe, text, command, icon=icon, tab=tab)

    def select_first_tab(self):
        i = side_bar_tab_list[0]
        i.click()


class Spacer(Canvas):
    def __init__(self, parent, text, *args, **kwargs):

        self.frame_color = "#8084fb"
        self.hover_border_color = "8084fb"

        Canvas.__init__(self, parent, width=198, height=75, bg=self.frame_color, highlightthickness=1, highlightbackground=self.frame_color, *args, **kwargs)
        self.pack()

        self.text = Label(self, text=text, bg=self.frame_color, font="Segoe 16 bold", fg="black")
        self.text.place(x=3, y=12)

        ScrollOnItemsList.append(self)

    def hover(self, event=None):
        self.config(highlightbackground=self.hover_border_color)

    def unhover(self, event=None):
        self.config(highlightbackground=self.frame_color)

    def click(self, event=None):
        print()


class SideBarButton(Canvas):
    def __init__(self, parent, text, command, icon=None, tab=True, *args, **kwargs):

        self.frame_color = "#8084fb"
        self.hover_color = "#4f3d7d"
        self.hover_border_color = "#4f3d7d"
        self.is_tab = tab

        self.selected = False

        self.command = command

        Canvas.__init__(self, parent, width=198 , height=55, bg=self.frame_color, highlightthickness=1, highlightbackground=self.frame_color, *args, **kwargs)
        self.pack()

        if icon == None:
            pass
        else:
            self.icon = Sprite(icon, 25, 25)
            self.create_image(35, 20, image=self.icon)

        self.text = Label(self, text=text, font="Segoe 12", bg=self.frame_color, fg="black")
        self.text.place(x=75, y=10)

        self.bind('<Enter>', self.hover)
        self.bind('<Button-1>', self.click)
        if self.is_tab == False:
            self.bind('<ButtonRelease-1>', self.unclick)

        self.text.bind('<Enter>', self.hover)
        self.text.bind('<Button-1>', self.click)
        if self.is_tab == False:
            self.text.bind('<ButtonRelease-1>', self.unclick)
        if self.is_tab:
            side_bar_tab_list.append(self)
        ScrollOnItemsList.append(self)

    def hover(self, event=None):
        if self.selected == False:
            self.bind('<Leave>', self.unhover)
            self.config(highlightbackground=self.hover_border_color, bg=self.hover_color)
            self.text.config(bg=self.hover_color)

    def unhover(self, event=None):
        self.config(highlightbackground=self.frame_color, bg=self.frame_color)
        self.text.config(bg=self.frame_color)

    def click(self, event=None):

        if self.is_tab:
            self.bind('<Leave>', str)
            for i in side_bar_tab_list:
                i.unhover()
                i.selected = False

        self.selected = True

        self.config(bg=self.hover_border_color)
        self.text.config(bg=self.hover_border_color)

        self.command()

    def unclick(self, event=None):
        self.selected = False
        self.config(bg=self.hover_color)
        self.text.config(bg=self.hover_color)