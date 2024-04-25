import tkinter as tk
from tkinter import filedialog
import pytesseract
from PIL import Image, ImageTk
import os
import pywhatkit
import tkinter.scrolledtext as st

def browseImage():
    fl = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Text Image',filetypes=(('JPG File','*.jpg'),('PNG File','*.png'),('All Files','*')))
    global img 
    img = Image.open(fl)
    imgcpy = img
    imgcpy.thumbnail((500,500))
    imgcpy = ImageTk.PhotoImage(imgcpy)
    label.configure(image=imgcpy)
    label.image = imgcpy

def extractText():
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(img)
    result = result.replace(result[-1], '  ')
    txt.insert(tk.END, result)

def saveText():
    fl = filedialog.asksaveasfile(defaultextension='.txt')
    filetext = str(txt.get(1.0,tk.END))
    fl.write(filetext)
    fl.close()

def searchImage():
    pywhatkit.search('Text Image')

def removeAllText():
    txt.delete(1.0, tk.END)

win = tk.Tk()
win.geometry('1920x1080')
win.title('Image Text extractor')
win.iconbitmap('./img/extract.ico')

lfont = ('Castellar',20,'bold')
label = tk.Label(win,text='Your image will be shown here',font=lfont)
label.pack(side=tk.TOP)

txt = st.ScrolledText(win,undo=True)
txt.place(x=550,y=500)

frame = tk.Frame(win)
frame.place(x=543,y=440)

f = ('Algerian', 10,'bold')

browseicon = tk.PhotoImage(file='./img/browse1.png')
browseicon = browseicon.subsample(11,11)
btn0 = tk.Button(frame,fg='white',bg='red',text=' Browse Image',image=browseicon,compound=tk.LEFT,command=browseImage,font=f,cursor="hand2")
btn0.pack(side=tk.LEFT,padx=5)

extracticon = tk.PhotoImage(file='./img/down.png')
extracticon = extracticon.subsample(5,5)
btn1 = tk.Button(frame,fg='white',bg='blue', text=' Extract Image Text',image=extracticon,compound=tk.LEFT,command=extractText,font=f,cursor="hand2")
btn1.pack(side=tk.LEFT, padx=40)

searchicon = tk.PhotoImage(file='./img/search.png')
searchicon = searchicon.subsample(5,5)
btn2 = tk.Button(frame,fg='white',bg='orange', text=' Search Image Online',image=searchicon,compound=tk.LEFT,command=searchImage,font=f,cursor="hand2")
btn2.pack(side=tk.LEFT, padx=10)

saveicon = tk.PhotoImage(file='./img/save1.png')
btn3 = tk.Button(win, image=saveicon,command=saveText,bd=0,cursor="hand2")
btn3.place(x=1400,y=510)

removeicon = tk.PhotoImage(file='./img/remove.png')
removeicon = removeicon.subsample(16,16)
btn4 = tk.Button(win,image=removeicon,command=removeAllText,bd=0,cursor="hand2")
btn4.place(x=1400,y=610)

undoicon = tk.PhotoImage(file='./img/Undo.png')
undoicon = undoicon.subsample(10,10)
undobtn = tk.Button(win,image=undoicon,command=txt.edit_undo,bd=0,cursor="hand2")
undobtn.place(x=1380,y=710)

redoicon = tk.PhotoImage(file='./img/Redo.png')
redoicon = redoicon.subsample(10,10)
redobtn = tk.Button(win,image=redoicon,command=txt.edit_undo,bd=0,cursor="hand2")
redobtn.place(x=1450,y=710)

win.mainloop()