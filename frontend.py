from tkinter import *
from backend import Database

database=Database()

class Window(object):

    def __init__(self, window):

        self.window = window

        self.window.wm_title("English Dictionary")

        label1=Label(window, text="Word:")
        label1.grid(row=0, column=0)

        label2=Label(window, text="Message:")
        label2.grid(row=1, column=0, rowspan=2)

        label3=Label(window, text="Suggestion:")
        label3.grid(row=3, column=0)

        label4=Label(window, text="Definition(s) Found:")
        label4.grid(row=4, column=0)

        self.word_to_define=StringVar()
        self.entry1=Entry(window, textvariable=self.word_to_define, width=50)
        self.entry1.grid(row=0, column=1)

        self.list1=Listbox(window, height=8, width=70)
        self.list1.grid(row=5, column=0, rowspan=8, columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=5, column=2, rowspan=8, sticky="nsw")

        sb2=Scrollbar(window, orient=HORIZONTAL)
        sb2.grid(row=13, column=0, columnspan=2, sticky="nsew")

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)
        self.list1.configure(xscrollcommand=sb2.set)
        sb2.configure(command=self.list1.xview)

        self.list2=Listbox(window, height=2, width=50)
        self.list2.grid(row=1, column=1, rowspan=2)

        self.list3=Listbox(window, height=1, width=50)
        self.list3.grid(row=3, column=1)

        button1=Button(window, text="Get Definition", width=14, command=self.get_definition)
        button1.grid(row=0, column=2)

        button2=Button(window, text="Apply Suggestion", command=self.apply_suggestion)
        button2.grid(row=3, column=2)

        button3=Button(window, text="Reject Suggestion", command=self.reject_suggestion)
        button3.grid(row=3, column=3)

        button4=Button(window, text="Close Dictionary", width=14, command=window.destroy)
        button4.grid(row=12, column=3)

    def get_definition(self):
        self.list1.delete(0, END)
        self.list2.delete(0, END)
        self.list3.delete(0, END)
        # check if any records have been returned
        if len(database.define(self.word_to_define.get())) >0:
        # if there have, return the definitions for that word
            for row in database.define(self.word_to_define.get()):
                self.list1.insert(END, row)
        # if not, look for a close match and return that as a suggestion
        else:
            if len(database.closest_match(self.word_to_define.get())) >0:
                for row in database.closest_match(self.word_to_define.get()):
                    self.list3.insert(END, row)
                self.list2.insert(END, "A close match to your original word has been found.")
                self.list2.insert(END, "Is this what you meant to type?")
            else:
                self.list2.insert(END, "No words found matching your entry.")
                self.list2.insert(END, "Please re-check the spelling and re-enter.")
    
    def apply_suggestion(self):
        self.list1.delete(0, END)
        self.list2.delete(0, END)
        self.entry1.delete(0, END)
        # copy the value from listbox 3 over into the word entry box
        self.entry1.insert(END, self.list3.get(0, 0))
        # prompt the user with a message to hit the 'Get Definition' button
        self.list2.insert(END, "Please press the 'Get Definition' button to look up.")
    
    def reject_suggestion(self):
        self.list3.delete(0, END)
        self.list2.delete(0, END)
        self.list2.insert(END, "Please re-check the spelling and re-enter.")


window=Tk()
Window(window)
window.mainloop()
