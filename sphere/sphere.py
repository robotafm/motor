from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Button, Label, Style
 
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
 
    def initUI(self):
 
        self.master.title("Конфигуратор Led-Sphere")
        self.pack(fill=BOTH, expand=True)
 
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
 
        lbl = Label(self, text="Окна")
        lbl.grid(sticky=W, pady=4, padx=5)
 
        canvas = Canvas(self, background='black')
        canvas.create_arc(120, 50, 380, 450, outline='blue', start=90, extent=180, width=2)
        canvas.create_arc(120, 50, 380, 450, outline='red', start=270, extent=180, width=2)
        canvas.create_oval(50,50, 450, 450, outline='white', width=2)

        canvas.grid(row=1, column=1, columnspan=3, rowspan=4, padx=5, sticky=E+W+S+N)
        
        combobox_text = StringVar()
        combobox = ttk.Combobox(self, textvariable=combobox_text)
        combobox['values'] = ('Земля', 'Марс', 'Меркурий', 'Юпитер')
        combobox.grid(row=1, column=0)

        load_btn = Button(self, text="Загрузить")
        load_btn.grid(row=2, column=0)

        save_btn = Button(self, text="Сохранить")
        save_btn.grid(row=3, column=0)
 
        change_btn = Button(self, text="Изменить")
        change_btn.grid(row=4, column=0)

        cbtn = Button(self, text="Закрыть")
        cbtn.grid(row=5, column=0, pady=4)
 
        hbtn = Button(self, text="Помощь")
        hbtn.grid(row=6, column=0, padx=5)
 
        obtn = Button(self, text="Готово")
        obtn.grid(row=6, column=3)
 
 
def main():
 
    root = Tk()
    root.geometry("660x600")
    app = Example()
    root.mainloop()
 
 
if __name__ == '__main__':
    main()