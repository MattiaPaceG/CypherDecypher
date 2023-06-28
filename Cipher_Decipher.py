from tkinter import messagebox
import json

class Cypher_Decypher():

    def __init__(self, master_window):
        self.master = master_window
        self.char_to_hex_dict = {}
        self.hex_to_char_dict = {}
        self.char_list = []

        with open("ASCII.json", encoding="utf8") as json_file:
            ascii_chars = json.load(json_file)["ASCII"]

            for char in ascii_chars:
                index = char[0]
                hex = char[1]
                char = char[3]

                if (char.strip() != "" and int(index) >= 40):
                    self.char_to_hex_dict[char] = hex
                    self.hex_to_char_dict[hex] = char
                    self.char_list.append(char)


    def caesar(self, text, shift, encryption=True):

        result = ""

        for char in text:
            if char == " ":
                result = result + char
            else:
                char_index = self.char_list.index(char)
                if encryption:
                    shifted_index = char_index + shift
                    if shifted_index > len(self.char_list) - 1:
                        shifted_index = shifted_index - len(self.char_list)
                    result = result + self.char_list[shifted_index]

                else:
                    shifted_index = char_index - shift
                    if shifted_index < 0:
                        shifted_index = len(self.char_list) - shifted_index
                    result = result + self.char_list[shifted_index]

        return result

    def hexa(self, text, value, encryption = True):

        result = ""

        if value == "all":
            value = len(text)

        if encryption:
            text_to_change = text[0:value]
            text_to_keep = text[value:]

            for char in text_to_change:
                if char == " ":
                    result = result + " "
                else:
                    result = result + self.char_to_hex_dict[char]

            result = result + text_to_keep

        else:
            text = text.replace(" ", "  ")
            text_to_change = text[0:value*2]
            text_to_keep = text[value*2:]


            print(text_to_change)

            splitted = [text_to_change[i:i+2] for i in range (0, len(text_to_change), 2)]
            print(splitted)

            try:
                for part in splitted:
                    if part == "  ":
                        result = result + " "
                    else:
                        result = result + self.hex_to_char_dict[part]

                result = result + text_to_keep

                return result
            except KeyError:
                messagebox.showerror("IMPOSSIBLE TO DECRYPT", "Values entered are not valid for decrypting")

        return result




    def encrypt(self, text, caesar, hexa):
        caesar = self.caesar(text, caesar)
        hexa = self.hexa(caesar, hexa)

        return (caesar, hexa)


    def decrypt(self, text, caesar, hexa):
        reverse_hexa = self.hexa(text, hexa, encryption=False)
        reverse_caesar = self.caesar(reverse_hexa, caesar, encryption=False)

        return (reverse_caesar, reverse_hexa)

    def check_input(self, text, caesar, hexa):

        text_dim = len(text)
        for char in text:
            if char not in self.char_list and char != " ":
                return (False, 1)

        if hexa != "all":
            if hexa > text_dim:
                return (False, 2)

        return (True, 0)

