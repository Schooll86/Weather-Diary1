import tkinter as tk, json, os
from tkinter import messagebox

file="weather.json"; data=[]

def load():
    global data
    if os.path.exists(file): data=json.load(open(file))
    update()

def save(): json.dump(data,open(file,"w"),indent=4)

def add():
    d,t,desc,r=e1.get(),e2.get(),e3.get(),var.get()
    if not d or not t.replace('-','').isdigit() or not desc:
        return messagebox.showerror("Ошибка","Проверь ввод")
    data.append({"date":d,"temp":int(t),"desc":desc,"rain":r})
    update()

def update(arr=None):
    lb.delete(0,tk.END)
    for x in (arr or data):
        lb.insert(tk.END,f"{x['date']} {x['temp']}C {x['desc']}")

def filt():
    d,t=e4.get(),e5.get()
    arr=[x for x in data if (d in x['date'] or not d) and (x['temp']>int(t) if t else True)]
    update(arr)

root=tk.Tk()
e1,e2,e3=[tk.Entry(root) for _ in range(3)]
[e.pack() for e in [e1,e2,e3]]
var=tk.StringVar(value="нет")
tk.Checkbutton(root,text="Осадки",variable=var,onvalue="да",offvalue="нет").pack()
tk.Button(root,text="Добавить",command=add).pack()

lb=tk.Listbox(root); lb.pack()

e4,e5=tk.Entry(root),tk.Entry(root)
e4.pack(); e5.pack()
tk.Button(root,text="Фильтр",command=filt).pack()

root.protocol("WM_DELETE_WINDOW",lambda:(save(),root.destroy()))
load(); root.mainloop()
