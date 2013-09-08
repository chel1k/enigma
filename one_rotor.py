import os, sys, string, random

class enigma:
    def __init__(self):
        self.symbol_values   = {}
        self.encryption_keys = {}
        self.get_symbol_values()
        self.index = random.choice(range(99))
        self.state = None

    def get_symbol_values(self):
        """
        iterate over symbols used and assign a numeric value to each 
        symbol. These values are used as the basis for encryption and
        decrytpion
        """
        symbols = enumerate(string.ascii_letters + string.digits +
                   string.punctuation + string.whitespace)
        for symbol in symbols:
            value = list(symbol.__iter__())         # tuple of (index, symbol)
            self.symbol_values[value[1]] = value[0] # dict[symbol] = index

    def rotor_one(self):
        """
        The first rotor moves one step at each key press. This is captured here
        by storing index information. To do: clean up encryption/decryption
        cycle logic as it is very messy.
        """
        self.index += 1
        if self.state == 'encryption':
            if self.index > 99:
                self.index = 0
        if self.state == 'decryption':
            if self.index < 0:
                self.index = self.index + 99
            if self.index > 99:
                self.index = self.index - 100 

    def encrypt(self, message):
        """
        msg must be a variable of type str
        """
        self.state = 'encryption'
        encrypted_message = ''
        for symbol in message:
            
            value            = self.symbol_values[symbol]
            encrypted_key    = value + self.index
            if encrypted_key > 99:
                encrypted_key = encrypted_key - 99
            for element in self.symbol_values:
                if self.symbol_values[element] == encrypted_key:
                    encrypted_symbol = element
            self.rotor_one()
            encrypted_message = encrypted_message + encrypted_symbol         
        return encrypted_message

    def decrypt(self, encrypted_message, index):
        """
        msg must be a variable of type list
        """
        self.state = 'decryption'
        decrypted_message = ''
        self.index = index
        for symbol in encrypted_message:
            value = self.symbol_values[symbol]
            decrypted_key = value - self.index
            if decrypted_key < 0:
                decrypted_key = decrypted_key + 99
            for element in self.symbol_values:
                if self.symbol_values[element] == decrypted_key:
                    decrypted_symbol = element
            decrypted_message = decrypted_message + decrypted_symbol
            self.rotor_one()
            
            ########################################
##            self.index += 1
##            if self.index < 0:
##                self.index = self.index + 99
##            if self.index > 99:
##                self.index = self.index - 100
            ########################################
        return decrypted_message

        
