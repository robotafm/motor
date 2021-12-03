from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Button, Label, Style
from PIL import Image, ImageTk
 
current_color = 'white'


def clicked(led):
    print(led)

def onObjectClick(event):                  
    cid = event.widget.find_closest(event.x,event.y)[0]
    event.widget.itemconfigure(cid, fill=current_color)

root = Tk()    

Window = Frame() 
Window.master.title("Конфигуратор Led-Sphere")
Window.pack(fill=BOTH, expand=True)
 
Window.columnconfigure(1, weight=1)
Window.columnconfigure(3, pad=7)
Window.rowconfigure(3, weight=1)
Window.rowconfigure(5, pad=7)
 
lbl = Label(Window, text="Окна")
lbl.grid(sticky=W, pady=4, padx=5)
 
canvas = Canvas(Window, background='black')
canvas.create_arc(120, 50, 380, 450, outline='blue', start=90, extent=180, width=2)
canvas.create_arc(120, 50, 380, 450, outline='red', start=270, extent=180, width=2)
canvas.create_oval(50,50, 450, 450, outline='white', width=2)
for led in range(1, 65):
    canvas.create_oval(247,46+led*6.2, 253, 52+led*6.2, fill='red', 
                       activefill='lightgreen', tags=led)
    canvas.tag_bind(led, '<ButtonPress-1>', onObjectClick) 

canvas.grid(row=1, column=1, columnspan=3, rowspan=4, padx=5, sticky=E+W+S+N)
        
combobox_text = StringVar()
combobox = ttk.Combobox(Window, textvariable=combobox_text)
combobox['values'] = ('Земля', 'Марс', 'Меркурий', 'Юпитер')
combobox.grid(row=1, column=0)

load_btn = Button(Window, text="Загрузить")
load_btn.grid(row=2, column=0)

#Добавим палитру
palette = Canvas(Window, height=333, width=335)
image = Image.open("../data/imgs/canvas_f2.png")
photo = ImageTk.PhotoImage(image)
image = palette.create_image(0, 0, anchor='nw',image=photo)
palette.grid(row=3,column=0)

save_btn = Button(Window, text="Сохранить")
save_btn.grid(row=4, column=0)
 
change_btn = Button(Window, text="Изменить")
change_btn.grid(row=5, column=0)

cbtn = Button(Window, text="Закрыть")
cbtn.grid(row=6, column=0, pady=4)
 
hbtn = Button(Window, text="Помощь")
hbtn.grid(row=7, column=0, padx=5)
 
obtn = Button(Window, text="Готово")
obtn.grid(row=7, column=3)
  
root.geometry("860x600")
root.mainloop()