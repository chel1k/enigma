import os, sys, string, random


class Enigma:
    def __init__(self):
        self.symbol_values   = {}
        self.encryption_keys = {}
        self.get_symbol_values()
        self.rotor_indicies = {}
        for i in range(1, 4):
            self.rotor_indicies[i] = random.choice(range(1, 27))            
        self.state = None
        self.count = 1

    def get_symbol_values(self):
        """
        iterate over symbols used and assign a numeric value to each 
        symbol. These values are used as the basis for encryption and
        decrytpion
        """
        symbols = enumerate(string.ascii_uppercase)
        for symbol in symbols:
            value = list(symbol.__iter__())          # tuple of (index, symbol)
            self.symbol_values[value[1]] = value[0]+1# dict[symbol] = index

    def update_rotor_indicies(self):
        """
        stimulate the cylcing of the rotor indicies by updating
        after each key press.
        """
        # update rotor 3
        if self.count % 138 == 0:
            self.rotor_indicies[3] += 1

        # update rotor 2
        if self.rotor_indicies[1] % 23 == 0:
            self.rotor_indicies[2] += 1
            
        # update rotor 1
        self.rotor_indicies[1] += 1
        self.count += 1

        # if any rotor has completed a 'cycle' then update
        for i in range(len(self.rotor_indicies.keys())):
            if self.rotor_indicies[i+1] > 26:
                self.rotor_indicies[i+1] = 1


    def encrypt(self, message):
        enc =  self.cipher(self.cipher(self.cipher(message, 1), 2), 3)
        self.update_rotor_indicies()
        return str(enc)
    
    
    def cipher(self, message, index):
        """
        msg must be a variable of type str
        """
        self.state = 'encryption'
        encrypted_message = ''
        for symbol in message:
            value         = self.symbol_values[symbol]
            encrypted_key = value + self.rotor_indicies[index]
            if encrypted_key > 26:
                #print(encrypted_key, end= ' ')
                encrypted_key = encrypted_key - 26
            #print(encrypted_key)
            for element in self.symbol_values:
                if self.symbol_values[element] == encrypted_key:
                    encrypted_symbol = element
            # update rotor indicies went here
            encrypted_message = encrypted_message + encrypted_symbol         
        return encrypted_message

    def decrypt(self, encrypted_message, index):
        """
        msg must be a variable of type str. To successfully decrypt,
        must manually input the rotor indicies which the message
        was started when it was first encrypted.
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
        return decrypted_message
