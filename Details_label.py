import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Label Frame')


label_frame=ttk.LabelFrame(win,text='Enter your details: ')
label_frame.grid(row=0,column=0,padx=10,pady=3)


labels=['What is your name:' ,'What is your age:' ,'What is your gender:' ,'Country:' ,'State:' ,'City:']
for i in range(len(labels)):
    cur_label='label'+ str(i)
    cur_label=ttk.Label(label_frame,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W, padx=6, pady=2)

# entry box
name_var=tk.StringVar()
user_info={
    'name': tk.StringVar(),
    'age' : tk.StringVar(),
    'gender' : tk.StringVar(),
    'country' : tk.StringVar(),
    'state' : tk.StringVar(),
    'city' : tk.StringVar()


}
counter=0
for i in user_info:
    cur_entrybox='Entry'+ i
    cur_entry=ttk.Entry(label_frame,width=20,textvariable=user_info[i])
    cur_entry.grid(row=counter,column=1, padx=6, pady=2)
    counter +=1  

def action():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info['gender'].get())
    print(user_info['country'].get())


submit_btn=ttk.Button(win,text='Submit',command=action)   
submit_btn.grid(row=1,columnspan=2) 
 

for child in label_frame.winfo_children():
    child.grid_configure(padx=4,pady=4)


win.mainloop()