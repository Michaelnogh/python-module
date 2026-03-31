import tkinter as tk
from tkinter import messagebox

class NotesApp:

    def __init__(self):
        # יצירת חלון
        self.root = tk.Tk() # Create Window
        self.root.title("Notes App") # Title Name
        self.root.geometry("400x500") # Size of the Window

        # כותרת
        self.title_label = tk.Label(self.root, text="My Notes", font=('Arial',20))
        self.title_label.pack(pady=10)

        #Text
        self.textbox = tk.Text(self.root, height=5, font=('Arial', 14)) # the user puting notes
        self.textbox.pack(padx=10, pady=10)
        
        #Add button
        self.add_button = tk.Button(self.root, text="Add Note", command=self.add_note) # Add Button
        self.add_button.pack(pady=5)

        #Note Lists
        self.listbox = tk.Listbox(self.root, font=('Arial', 14))
        self.listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        #Delete Buttom
        self.delete_button = tk.Button(self.root, text="Delete Selected", font=("Arial", 14), command=self.delete_note)
        self.delete_button.pack(pady=5)
        # Erua lehiza al List
        self.listbox.bind("<<ListboxSelect>>", self.show_selected_note)
        #AFALA SHEL A TOHNIT
        self.root.mainloop()

        #ADDING NOTE FUNC
    def add_note(self):
        text = self.textbox.get("1.0", tk.END).strip()

        if text == "":
            messagebox.showwarning("Warning", "Note is empty!")    
            return
        
        self.listbox.insert(tk.END, text)
        self.textbox.delete("1.0", tk.END)

        #Deleting NOTE FUNC
    def delete_note(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
        except:
            messagebox.showerror("Error", "No note Selected!")

       # Viewing Note With One click
    def show_selected_note(self, event):
        try:
            selected_index = self.listbox.curselection()[0]
            selected_text = self.listbox.get(selected_index)

            self.textbox.delete("1.0", tk.END)
            self.textbox.insert(tk.END, selected_text)
        except:
            pass


NotesApp()            
     

