from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from datetime import *

import DateTime

root = Tk()
root.title("My first GUI")
root.geometry('500x150+350+170')
frame = Frame(root, bg = "#56ADFF", bd = 5)
frame.pack(pady  =10, padx = 10, fill = X)
s = ttk.Style()
s.configure('my.TButton', font = ('Arial',19))
def choose_dir():
    dir_path = filedialog.askdirectory()
    E_PATH.delete(0,END)
    E_PATH.insert(0, dir_path)
def start_files():
    cur_path = E_PATH.get()
    if cur_path:
        for folder, subfolder, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                zdate = datetime.fromtimestamp(mtime)
                zdate = zdate.strftime('%Y-%m-%d')
                date_folder = os.path.join(cur_path,zdate)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path,os.path.join(date_folder,file))
        messagebox.showinfo('Отсортировано!','Операция прошла успешно')
        E_PATH.delete(0, END)
    else:
        messagebox.showerror('Ошибка!', 'Операция не удалась. ')




E_PATH =ttk.Entry(frame)
E_PATH.pack(side = LEFT, expand = True,ipady = 2, fill = X)
btn_dialog = ttk.Button(frame, text = 'Выберите папку', command = choose_dir)
btn_dialog.pack(side = LEFT, padx = 5)
btn1_dialog = ttk.Button(frame, text = 'Старт', command = start_files)
btn1_dialog.pack(fill = X,padx =10)
root.mainloop()
