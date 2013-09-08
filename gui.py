import os, sys, string, random
from tkinter import *
from enigma import Enigma

class GUI(Enigma):
    def __init__(self):
        Enigma.__init__(self)
        root = Tk()
        root.title('Enigma Cipher')
        self.keys = [['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K'],
                    ['P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L']
                    ]
        self.cipher_message = ''
        self.font = ('courier', 14, 'bold')
        root.bind("<Key-q>", self.on_Q)
        root.bind("<Key-w>", self.on_W)
        root.bind("<Key-e>", self.on_E)
        root.bind("<Key-r>", self.on_R)
        root.bind("<Key-t>", self.on_T)
        root.bind("<Key-z>", self.on_Z)
        root.bind("<Key-u>", self.on_U)
        root.bind("<Key-i>", self.on_I)
        root.bind("<Key-o>", self.on_O)
        root.bind("<Key-a>", self.on_A)
        root.bind("<Key-s>", self.on_S)
        root.bind("<Key-d>", self.on_D)
        root.bind("<Key-f>", self.on_F)
        root.bind("<Key-g>", self.on_G)
        root.bind("<Key-h>", self.on_H)
        root.bind("<Key-j>", self.on_J)
        root.bind("<Key-k>", self.on_K)
        root.bind("<Key-p>", self.on_P)
        root.bind("<Key-y>", self.on_Y)
        root.bind("<Key-x>", self.on_X)
        root.bind("<Key-c>", self.on_C)
        root.bind("<Key-v>", self.on_V)
        root.bind("<Key-b>", self.on_B)
        root.bind("<Key-n>", self.on_N)
        root.bind("<Key-m>", self.on_M)
        root.bind("<Key-l>", self.on_L)
        self.command_mapping = { 'Q': self.on_Q,
                            'W': self.on_W,
                            'E': self.on_E,
                            'R': self.on_R,
                            'T': self.on_T,
                            'Z': self.on_Z,
                            'U': self.on_U,
                            'I': self.on_I,
                            'O': self.on_O,
                            'A': self.on_A,
                            'S': self.on_S,
                            'D': self.on_D,
                            'F': self.on_F,
                            'G': self.on_G,
                            'H': self.on_H,
                            'J': self.on_J,
                            'K': self.on_K,
                            'P': self.on_P,
                            'Y': self.on_Y,
                            'X': self.on_X,
                            'C': self.on_C,
                            'V': self.on_V,
                            'B': self.on_B,
                            'N': self.on_N,
                            'M': self.on_M,
                            'L': self.on_L}
        self.make_widgets()

        self.Q_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
                          width=2, relief=RIDGE, bd=1, text='Q')
    

        root.mainloop()

    def make_widgets(self):
        self.make_rotorboard()
        self.make_lightboard()
        self.make_keyboard()


    def make_rotorboard(self):
        """
        Draw the rotor displays; these change per key press. need to track
        state, so each rotor display must have a unique name.
        """
        font = ('courier', 12, )
        # Base of the rotorboard
        self.rotorboard = Frame(height=150, width=300, bd=1, relief=RAISED,
                           bg='grey')
        self.rotorboard.pack(fill=X, padx=5, pady=5)

        # rotor's displays and wheels
        self.rotor_one = StringVar()
        self.rotor_one.set(self.get_rotor_value(1))
        self.first_rotor = Label(self.rotorboard, textvariable=self.rotor_one, text=self.rotor_one,
            width=2, bg='grey', fg='black', relief=SUNKEN,
            font=('courier', 18, 'bold')).pack(side=RIGHT, padx=5,
                                               pady=5)
    
        self.rotor_two = StringVar()
        self.rotor_two.set(self.get_rotor_value(2))
        self.secon_rotor = Label(self.rotorboard, textvariable=self.rotor_two, text=self.rotor_two,
            width=2, bg='grey', fg='black', relief=SUNKEN,
            font=('courier', 18, 'bold')).pack(side=RIGHT, padx=5,
                                               pady=5)

        self.rotor_thr = StringVar()
        self.rotor_thr.set(self.get_rotor_value(3))
        self.three_rotor = Label(self.rotorboard, textvariable=self.rotor_thr, text = self.rotor_thr,
            width=2, bg='grey', fg='black', relief=SUNKEN,
            font=('courier', 18, 'bold')).pack(side=RIGHT, padx=5,
                                               pady=5)


        # cipher text label
        self.var = StringVar()
        self.var.set(self.cipher_message)
        self.cipher_text = Label(self.rotorboard, textvariable=self.var, text=self.cipher_message,
                                 bg='grey', font=self.font)
        self.cipher_text.pack(side=LEFT, fill=X)


    def make_lightboard(self):
        font = ('courier', 14, 'bold')
        self.lightboard = Frame(height=150, width=300, bd=1, relief=RAISED,
                           bg='grey')
        self.lightboard.pack(fill=X, padx=5, pady=5)
        odd_col = 1
        eve_col = 2
        for x in self.keys[0]:
            light = Label(self.lightboard, bg='black', fg='black', font=self.font,
                          width=2, relief=RIDGE, bd=1, text=x).grid(row=1,
                          column=odd_col, padx=4)
            odd_col += 2
        odd_col = 1
        for x in self.keys[1]:
            light = Label(self.lightboard, bg='black', fg='black', font=self.font,
                          width=2, relief=RIDGE, bd=1, text=x).grid(row=2,
                          column=eve_col,  padx=4)
            eve_col += 2
        for x in self.keys[2]:
            light = Label(self.lightboard, bg='black', fg='black', font=self.font,
                          width=2, relief=RIDGE, bd=1, text=x).grid(row=3,
                          column=odd_col,  padx=4)
            odd_col += 2

    def flash(self, char):
        for x in self.lightboard:
            if x.text == char:
                x.fg = 'white'
                x.after(250)
                x.fg = 'black'
              
            

    def make_keyboard(self):
        font = ('courier', 14, 'bold')
        self.keyboard = Frame(height=150, width=300, bd=1, relief=RAISED,
                           bg='grey')
        self.keyboard.pack(fill=X, padx=5, pady=5)
        odd_col = 1
        eve_col = 2
        for x in self.keys[0]:
            light = Button(self.keyboard, bg='grey', fg='black', font=self.font,
                           width=2, bd=1, command=self.command_mapping[x],
                           text=x).grid(row=1, column=odd_col, padx=2)
            odd_col += 2
        odd_col = 1
        for x in self.keys[1]:
            light = Button(self.keyboard, bg='grey', fg='black', font=self.font,
                           width=2, bd=1, command=self.command_mapping[x],
                           text=x).grid(row=2, column=eve_col, padx=2)
            eve_col += 2
        for x in self.keys[2]:
            light = Button(self.keyboard, bg='grey', fg='black', font=self.font,
                           width=2, bd=1, command=self.command_mapping[x],
                           text=x).grid(row=3, column=odd_col, padx=2)
            odd_col += 2

    ###########################################################################
    # Key Bindings
    ###########################################################################

    def on_Q(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('Q')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_W(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('W')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_E(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('E')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_R(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('R')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_T(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('T')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_Z(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('Z')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_U(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('U')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_I(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('I')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_O(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('O')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_A(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('A')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_S(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('S')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_D(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('D')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_F(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('F')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_G(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('G')
        self.var.set(self.cipher_message)
    def on_H(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('H')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_J(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('J')
        self.var.set(self.cipher_message)
    def on_K(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('K')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_P(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('P')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_Y(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('Y')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_X(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('X')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_C(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('C')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_V(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('V')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_B(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('B')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_N(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('N')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_M(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('M')
        self.var.set(self.cipher_message)
        self.update_rotor_display()
    def on_L(self, event):
        self.cipher_message = self.cipher_message + self.encrypt('L')
        self.var.set(self.cipher_message)
        self.update_rotor_display()

        
    ###########################################################################
    # light widgets
    ###########################################################################

##    self.Q_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='Q')
    
##    self.W_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='W')
##    
##    self.E_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='E')
##    
##    self.R_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='R')
##    
##    self.T_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='T')
##    
##    self.Z_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='Z')
##
##    self.U_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='U')
##    
##    self.I_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='I')
##    
##    self.O_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='O')
##    
##    self.A_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='A')
##    
##    self.S_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='S')
##    
##    self.D_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='D')
##    
##    self.F_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='F')
##    
##    self.G_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='G')
##    
##    self.H_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='H')
##    
##    self.J_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='J')
##    
##    self.K_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='K')
##
##    self.P_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='P').
##    
##    self.Y_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='Y')
##    
##    self.X_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='X')
##    
##    self.C_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='C')
##    
##    self.V_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='V')
##    
##    self.B_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='B')
##    
##    self.N_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='N')
##    
##    self.M_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='M')
##    
##    self.L_light = Label(self.lightboard, bg='black', fg='black', font=self.font,
##                          width=2, relief=RIDGE, bd=1, text='L')

    
    ###########################################################################
    # other functions
    ###########################################################################

    def get_rotor_value(self, rotor):
        if rotor not in self.rotor_indicies.keys():
            return
        index = self.rotor_indicies[rotor]+1
        if index >= 27:
            index = 1
        for symbol in self.symbol_values:
            if self.symbol_values[symbol] == index:
                return symbol


    def update_rotor_display(self):
        self.rotor_one.set(self.get_rotor_value(1))
        self.rotor_two.set(self.get_rotor_value(2))
        self.rotor_thr.set(self.get_rotor_value(3))
        
        

if __name__ == '__main__':
    GUI()
    
        
