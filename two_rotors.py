import os, sys, string, random
from tkinter import *
from enigma import Enigma

class GUI(Enigma):
    def __init__(self):
        Enigma.__init__(self)
        root = Tk()
        root.title('Enigma Cipher')
        #root.geometry("200x100")
        self.make_widgets()
        self.plain_text.bind("<Key>", self.update)
        root.mainloop()

    def make_widgets(self):
        for i in range(len(self.rotor_indicies.keys())):
            self.rotor = Label(text=self.get_rotor_value(i+1), relief=RIDGE)
            self.rotor.config(font=('courier', 20, 'bold'), fg='white', bg='black')
            self.rotor.grid(row=1, column=i+1)

        self.plain_text = Entry(relief=SUNKEN, font=('courier', 14, ))
        self.message = self.encrypt(self.plain_text.get())
        self.cipher_text = Label(text=self.message, font=('courier', 14, 'bold'))
        
        self.plain_text.grid(row=3, columnspan=5)
        self.cipher_text.grid(row=2, columnspan=5)

    def get_rotor_value(self, rotor):
        if rotor not in self.rotor_indicies.keys():
            return
        index = self.rotor_indicies[rotor]
        for symbol in self.symbol_values:
            if self.symbol_values[symbol] == index:
                return symbol

    def update(self, event):
        self.update_message()
        self.update_rotor_indicies()
        print(self.plain_text.get()[-1])

    def update_message(self):
        self.message = self.encrypt(self.plain_text.get())
        self.cipher_text.config(text=self.message)

if __name__ == '__main__':
    GUI()
    
        
