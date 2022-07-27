from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oh No!", message="Unable to save file...")

root = Tk()
        
def openFile():
    global filename
    file = askopenfile(parent=root,title='Select a File')
    filename = file.name
    t = file.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    file.close()

def ln():
    pos = text.index(INSERT).split(".")
    message1 = ("Row: "+ str(pos[0]))
    message2 = ("Column: "+ str(pos[1]))
    main = Tk()
    main.title("Line Position")
    main.minsize(width=100, height=100)
    main.maxsize(width=100, height=100)
    row = Message(main, text=message1, width=100)
    row.grid(row=0, column=1)
    column = Message(main, text=message2, width=100)
    column.grid(row=1, column=1)
    
root.title("MonkeyCode Editor")
text = Text(root)
text.grid()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
toolmenu = Menu(root)
toolmenu.add_command(label="Line Number", command=ln)
menubar.add_cascade(label="Tools", menu=toolmenu)


root.config(menu=menubar)
root.mainloop()