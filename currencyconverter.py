from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title("Currency Conversion")
root.geometry("500x500")
#create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)
#create two farmes
currency_farme=Frame(my_notebook,width=480,height=480)
conversion_frame=Frame(my_notebook,width=480,height=480)
currency_farme.pack(fill='both',expand=1)
conversion_frame.pack(fill='both',expand=1)
#add our tabs
my_notebook.add(currency_farme,text="currencies")
my_notebook.add(conversion_frame,text="convert")
#disable 2nd tab
my_notebook.tab(1,state='disabled')

#CURRENCY TAB
def lock():
  if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
    messagebox.showwarning("WARNING!","You Did'nt fill out all the Fields")
  else:
    #disable entry boxes
    home_entry.config(state="disabled")
    conversion_entry.config(state="disabled")
    rate_entry.config(state="disabled")
    #enable tab
    my_notebook.tab(1,state='normal')
    amount_label.config(text=f'Amount of {home_entry.get()} To Convert To {conversion_entry.get()}')
    converted_label.config(text=f'Equals This Many {conversion_entry.get()}')
    convert_button.config(text=f'Convert From {home_entry.get()}')    
def unlock():
  #enable entry boxes
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")
    #enable tab
    my_notebook.tab(1,state='disable')

#currency
home= LabelFrame(currency_farme,text="From CURRENCY ")
home.pack(pady=20)
#home currnecy entry box
home_entry=Entry(home,font=("Helvetica",24))
home_entry.pack(pady=10,padx=10)
#conversion currency frame
conversion = LabelFrame(currency_farme,text="Conversion Currnecy")
conversion.pack(pady=20)
#convert to label
conversion_label = Label(conversion,text="Currency to Convert to...")
conversion_label.pack(pady=10)
#convert to entry
conversion_entry = Entry(conversion,font=("Helvetica",24))
conversion_entry.pack(pady=10,padx=10)
#rate label
rate_label = Label(conversion,text="Current Conversion Rate...")
rate_label.pack(pady=10)
#rate to entry
rate_entry = Entry(conversion,font=("Helvetica",24))
rate_entry.pack(pady=10,padx=10)
#button frame
button_frame = Frame(currency_farme)
button_frame.pack(pady=20)
#create buttons
lock_button = Button(button_frame,text="Lock",command=lock)
lock_button.grid(row=0,column=0,padx=10)

unlock_button = Button(button_frame,text="UnLock",command=unlock)
unlock_button.grid(row=0,column=1,padx=10)

#CONVERSION TAB
def convert():
  #clear converted entry box
  converted_entry.delete(0,END)
  
  #convert
  conversion = float(rate_entry.get()) * float(amount_entry.get())
  conversion=round(conversion,2)
  #add commas
  conversion = '{:,}'.format(conversion)
  #updated entry box
  converted_entry.insert(0,f'${conversion}')
def Clear():
  amount_entry.delete(0,END)
  converted_entry.delete(0,END)
amount_label= LabelFrame(conversion_frame,text="Amount to Convert")
amount_label.pack(pady=20)
#entry box for amount
amount_entry= Entry(amount_label,font=("Helvetica",24))
amount_entry.pack(pady=10,padx=10)
#convert button
convert_button = Button(amount_label, text="Convert",command=convert)
convert_button.pack(pady=20)
#equals frame
converted_label= LabelFrame(conversion_frame,text="Converted to")
converted_label.pack(pady=20)
#converted entry
converted_entry=Entry(converted_label,font=("Helvetica",24),bd=20,bg="systembuttonface")
converted_entry.pack(pady=10,padx=10)
#clear button
clear_button = Button(conversion_frame,text="Clear",command=Clear)
clear_button.pack(pady=2)
#fake space
spacer=Label(conversion_frame,text="",width=68)
spacer.pack()



root.mainloop()