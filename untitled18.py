from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title("GUI CREATOR")
root.geometry("600x600")

elements=["label","button","dropdown"]

combo_box=ttk.Combobox(root,state="readonly",values=elements)
combo_box.pack()

class CreateElement():
    def __inti__(self):
        print("This is CreateElements class")
        
    def createLabel(self):
        label=Label(root,text="A new label has been created by the class",fg="blue")
        label.pack()
    
    def createButton(self):
        btn=Button(root,text="Button",command=self.showMessage)
        btn.pack(padx=20,pady=10)

    def showMessage(self):
        messagebox.showinfo("showinfo", "You clicked the Button using Class.")

    def showDropdown(self):
        val = [1, 2, 3, 4, 5]
        
        dropdown = ttk.Combobox(root, state = "readonly", values = val)
        dropdown.pack()

    def choose(self):
        global combo_box
        
        element = combo_box.get()
        
        if(element == "label"):
            self.createLabel()
            
        elif(element == "button"):
            self.createButton()
            
        elif(element == "dropdown"):
            self.showDropdown()

obj = CreateElement()
main_btn = Button(root, text = "Create Element", command = obj.choose)
main_btn.pack(padx = 20, pady = 10)


root.mainloop()

























































































































































































 





























