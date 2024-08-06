
                 #password genarator




from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip


def submit_action():
        global usr_input
        usr_input=input_entry.get()
        messagebox.showinfo("input recieved",f"you enterd : {usr_input}")


def generator():
    small_alphabet=string.ascii_lowercase
    capital_alphabet=string.ascii_uppercase
    numbers=string.digits
    spacial_characters=string.punctuation

    all=small_alphabet+capital_alphabet+numbers+spacial_characters+usr_input
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(usr_input+numbers,password_length))
    if choice.get()==2:
        passwordField.insert(0,random.sample(capital_alphabet+usr_input+numbers,password_length))
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))

   
def copy():
   random_password= passwordField.get()
   pyperclip.copy(random_password)



root = Tk()
root.config(bg="bisque2")
choice=IntVar()
Font =('arial',11,'bold')


passwordLabel=Label(root,text="password genarator",font=('times new roman',20,'bold'),bg='bisque2',fg='purple4')
passwordLabel.grid()

weakradioButton=Radiobutton(root,text='weak',value=1,variable=choice)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='medium',value=2,variable=choice)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='strong',value=3,variable=choice)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text="password length",font=Font,bg='bisque2',fg='purple4')
lengthLabel.grid(pady=5)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

input_label=Label(root,text="enter something:",font=Font,bg='bisque2',fg='purple4')
input_label.grid(pady=5)

input_entry=Entry(root,width=30)
input_entry.grid(pady=5)

submit_button=Button(root,text="submit",font=Font,bg='bisque2',fg='purple4',command=submit_action)
submit_button.grid(pady=5)

generateButton=Button(root,text='generate',font=Font,command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=5)

copyButton=Button(root,text='copy',font=Font,command=copy)
copyButton.grid()

root.mainloop()