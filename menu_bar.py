import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('MenuBar')

def func():
    print('function called')

# menubar=tk.Menu(win)
# ***********************************************simple menubar*********************************************
# menubar.add_command(label='Save',command=func)
# menubar.add_command(label='SaveAs',command=func)
# menubar.add_command(label='Copy',command=func)
# menubar.add_command(label='Undo',command=func)
# menubar.add_command(label='Redo',command=func)

main_menu=tk.Menu(win)
file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New File',command=func)
file_menu.add_command(label='WERT',command=func)
file_menu.add_separator()
file_menu.add_command(label='Save File',command=func)
main_menu.add_cascade(label='File',menu=file_menu)

edit_menu=tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='New File',command=func)
edit_menu.add_command(label='dtyr',command=func)
edit_menu.add_command(label='undu',command=func)
main_menu.add_cascade(label='Edit',menu=edit_menu)
win.config(menu=main_menu)






win.mainloop()
