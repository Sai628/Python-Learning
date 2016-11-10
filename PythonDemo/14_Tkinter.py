# coding=utf-8


from Tkinter import *


root = Tk()
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'JQuery', 'Bootstrap']

list1 = Listbox(root)
list2 = Listbox(root)

for item in li:
    list1.insert(0, item)

for item in movie:
    list2.insert(0, item)

list1.pack()
list2.pack()
root.mainloop()
