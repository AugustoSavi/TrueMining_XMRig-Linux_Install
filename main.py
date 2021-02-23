from src.sidebar import *
from src.pages.home import HomePage

root = Tk()	# create Window

root.resizable(False, False)
root.geometry("950x500")
root.title("")
root.option_add("*Font", 'Gadugi')

# create Frame for tab windows
main_frame = Frame(root, bg="grey", width=1000, height=1000)
main_frame.place(x=200, y=0)


# create sidebar + buttons + spacers
sidebar = SideBar(root)
sidebar.add_spacer("  True Mining")
sidebar.add_button("Home", lambda: HomePage(main_frame), icon="assets/images/home.png")
sidebar.add_button("Settings", lambda: HomePage(main_frame),icon= "assets/images/settings.png")
sidebar.finish()	# finish creation

root.mainloop()