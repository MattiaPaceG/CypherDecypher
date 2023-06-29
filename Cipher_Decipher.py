from tkinter import messagebox
import json

class Cypher_Decypher():

    def __init__(self, master_window):
        self.master = master_window
        self.char_to_hex_dict = {}
        self.hex_to_char_dict = {}
        self.char_list = []
        self.hex_list = []

        self.char_to_hex_dict[" "] = 20
        self.hex_to_char_dict["20"] = " "

        with open("ASCII.json", encoding="utf8") as json_file:
            ascii_chars = json.load(json_file)["ASCII"]

            for char in ascii_chars:
                index = char[0]
                hex = char[1]
                char = char[3]

                if (char.strip() != "" and int(index) >= 40):
                    self.char_to_hex_dict[char] = hex
                    self.hex_to_char_dict[hex] = char

        self.char_list = list(self.char_to_hex_dict.keys())
        self.hex_list =list(self.hex_to_char_dict.keys())

    def caesar(self, text, shift, encryption=True, hexa=False):

        result = []
        digits = 1
        list_to_use = self.char_list

        if hexa:
            digits = 2
            list_to_use = self.hex_list

        splitted_input = [text[i:i + digits] for i in range(0, len(text), digits)]
        print(splitted_input)

        for char in splitted_input:
            print(char)
            if char == " ":
                result.append(" ")
            else:
                char_index = int(list_to_use.index(char))
                print(char_index)
                if encryption:
                    shifted_index = char_index + int(shift)
                    if shifted_index > len(list_to_use) - 1:
                        shifted_index = shifted_index - len(list_to_use)
                else:
                    shifted_index = char_index - int(shift)
                    if shifted_index < 0:
                        shifted_index = len(list_to_use) - shifted_index

                result.append(str(list_to_use[shifted_index]))

        joined = "".join(result)
        return joined

    def to_hex(self, text):
        hexa_txt = ""

        for char in text:
            hexa_txt = hexa_txt + str(self.char_to_hex_dict[char])

        return (hexa_txt)

    def to_txt(self, text):
        splitted_text = [text[i:i + 2] for i in range(0, len(text), 2)]
        result = []

        for digit in splitted_text:
            result.append(str(self.hex_to_char_dict[digit]))

        joined_result = "".join(result)
        return joined_result


    def encrypt(self, text, caesar_shift, hexa_shift):
        caesar = self.caesar(text, caesar_shift)
        to_hexa = self.to_hex(caesar)
        shifted_hexa = self.caesar(to_hexa, hexa_shift, hexa=True)

        return (caesar, to_hexa, shifted_hexa)


    def decrypt(self, text, caesar_shift, hexa_shift):
        reverse_hexa = self.caesar(text, hexa_shift, encryption=False, hexa=True)
        to_text = self.to_txt(reverse_hexa)
        reverse_caesar = self.caesar(to_text, caesar_shift, encryption=False)

        return (reverse_hexa, to_text, reverse_caesar)

    def check_input(self, text):

        for char in text:
            if char not in self.char_list:
                return (False, 1)

        return (True, 0)

