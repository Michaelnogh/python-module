import tkinter as tk
# root = tk.Tk()
# label = tk.Label(root, text="My first app with pyton")
# label2 = tk.Label(root,text="Michael propoganda",fg="purple")
# label.pack()
# label2.pack()
# root.mainloop()
#-------------------------------------------------------------------------------------------------------------#
root = tk.Tk()
root.geometry("800x500")
root.title("My First GUI")


label = tk.Label(root,text="Michael First GUI", font=('Arial',18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root,height=3 ,font=('Arial', 16))
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text ="1", font=('Arial',18))
btn1.grid(row=0, column=0)
button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=10, pady=10)




myentry = tk.Entry(root)


root.mainloop()

