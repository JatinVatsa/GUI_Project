# starter code
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title('GUI')

# create labels
# widgets--> label,buttons,radio buttons -tk,ttk
name_label=ttk.Label(win,text='Enter your name: ')
name_label.grid(row=0,column=0,sticky=tk.W)
email_label=ttk.Label(win,text="Enter your email:")
email_label.grid(row=1,column=0,sticky=tk.W)
age_label=ttk.Label(win,text='Enter your age: ')
age_label.grid(row=2,column=0,sticky=tk.W)
gender_label=ttk.Label(win,text='select your gender: ')
gender_label.grid(row=3,column=0,sticky=tk.W)
name_label.configure(foreground='blue')


# entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=20,textvariable= name_var)
name_entrybox.grid(row=0,column=1)
# name_entrybox.focus()

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=20,textvariable= email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=20,textvariable= age_var)
age_entrybox.grid(row=2,column=1)


# combo box
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=17,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

# radio button
usertype=tk.StringVar()
radiottn1=ttk.Radiobutton(win,text='student',value='student',variable=usertype)
radiottn1.grid(row=4,column=0)
radiottn2=ttk.Radiobutton(win,text='teacher',value='teacher',variable=usertype)
radiottn2.grid(row=4,column=1)

# check button
checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text='check if you want to subscribe qweertuyykfgdfxnvn',variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)


# button creating
# def action():
#     username=name_var.get()
#     userage=age_var.get()
#     user_email=email_var.get()
#     print(f'{username} is {userage} years old ,{user_email}')
#     usergender=gender_var.get()
#     user_type=usertype.get()
#     if checkbtn_var.get()==0:
#         subcribed='NO'
#     else:
#         subcribed='YES'   
#     print(usergender,user_type,subcribed)     
    
#     with open('file5.txt','a') as f:
#         f.write(f'{username},{userage},{user_email},{usergender},{user_type},{subcribed}\n')

#     
#     # name_label.configure(foreground='blue')

def action():
    username=name_var.get()
    userage=age_var.get()
    user_email=email_var.get()
    usergender=gender_var.get()
    user_type=usertype.get()
    if checkbtn_var.get()==0:
        subcribed='NO'
    else:
        subcribed='YES' 

    with open('file6.csv','a',newline='') as f:
        dict_writer=DictWriter(f,fieldnames=['UserName','User Age','User Email','User Gender','User Type','Subcribed'])
        if os.stat('file6.csv').st_size==0:
            dict_writer.writeheader()

        dict_writer.writerow({
            'UserName': username,
            'User Age': userage,
            'User Email': user_email,
            'User Gender': usergender,
            'User Type': user_type,
            'Subcribed': subcribed

        })

    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)    
    

submit_button=tk.Button(win,text='submit',command=action)
submit_button.grid(row=6,column=0,sticky=tk.W)


win.mainloop()