import tkinter as tk
from Cipher_Decipher import Cypher_Decypher
from PIL import Image, ImageTk
from tkinter import messagebox
import pyperclip

class CipherToolGUI:

    def __init__(self, window):
        #class main attributes
        self.window = window
        self.window.title("Cipher/Decipher Tool")

        #creation of cypher-decypher object
        self.cypdec = Cypher_Decypher(self.window)

        #put image as a background
        image = "Images/bg.jpg"
        image = Image.open(image)
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #constant
        font_size_title = 24
        font_subtitles_entries = 16
        font_size_entries = 10


        # ENCRYPTION SECTION
        self.encryption_frame = tk.Frame(self.window)
        self.encryption_frame.pack(side=tk.LEFT, padx=20, pady=50)

        encryption_title = tk.Label(self.encryption_frame, text="Encryption Section", font=("Arial", font_size_title, "bold"))
        encryption_title.grid(row=0, columnspan=2, pady=20)

        plaintext_label = tk.Label(self.encryption_frame, text="Plaintext:", font=("Arial", font_subtitles_entries))
        plaintext_label.grid(row=1, column=0, pady=20)

        self.plaintext_entry = tk.Entry(self.encryption_frame, width=60, font=("Arial", font_size_entries))
        self.plaintext_entry.grid(row=1, column=1, padx= (0, 20), sticky=tk.W)

        caesar_shift_label = tk.Label(self.encryption_frame, text="Caesar Shift Value:", font=("Arial", font_subtitles_entries))
        caesar_shift_label.grid(row=2, column=0, padx=10)

        self.caesar_shift_entry = tk.Entry(self.encryption_frame, width=5, font=("Arial", font_size_entries))
        self.caesar_shift_entry.grid(row=2, column=1, sticky=tk.W)

        hexacode_label = tk.Label(self.encryption_frame, text="HexaCode Value:", font=("Arial", font_subtitles_entries))
        hexacode_label.grid(row=3, column=0, padx=10)

        self.hexacode_entry = tk.Entry(self.encryption_frame, width=5, font=("Arial", font_size_entries))
        self.hexacode_entry.grid(row=3, column=1, sticky=tk.W)

        encrypt_button = tk.Button(self.encryption_frame, text="Encrypt", command=self.encrypt, font=("Arial", font_size_entries))
        encrypt_button.grid(row=4, columnspan=2, pady=10)

        after_caesar_shift_label = tk.Label(self.encryption_frame, text="After Caesar Shift:", font=("Arial", font_subtitles_entries))
        after_caesar_shift_label.grid(row=5, column=0, padx=10)

        self.after_caesar_entry = tk.Entry(self.encryption_frame, width=60, font=("Arial", font_size_entries))
        self.after_caesar_entry.grid(row=5, column=1, padx=(0, 20), sticky=tk.W)
        self.after_caesar_entry.config(state="disabled")

        caesar_to_hexa = tk.Label(self.encryption_frame, text="Hexadecimal Conversion", font=("Arial", font_subtitles_entries))
        caesar_to_hexa.grid(row=6, column=0, padx=10)

        self.caesar_to_hexa_entry = tk.Entry(self.encryption_frame, width=60, font=("Arial", font_size_entries))
        self.caesar_to_hexa_entry.grid(row=6, column=1, padx=(0, 20), sticky=tk.W)
        self.caesar_to_hexa_entry.config(state="disabled")

        after_hexacode_label = tk.Label(self.encryption_frame, text="After HexaCode:", font=("Arial", font_subtitles_entries))
        after_hexacode_label.grid(row=7, column=0, padx=10)

        self.after_hexacode_entry = tk.Entry(self.encryption_frame, width=60, font=("Arial", font_size_entries))
        self.after_hexacode_entry.grid(row=7, column=1, padx=(0, 20), sticky=tk.W)
        self.after_hexacode_entry.config(state="disabled")

        encrypt_clear_button = tk.Button(self.encryption_frame, text="Clear Section", command=self.clear_encrypt, font=("Arial", font_subtitles_entries))
        encrypt_clear_button.grid(row=8, column = 1, columnspan=1, pady=10, sticky=tk.W)

        copy_encrypted__button = tk.Button(self.encryption_frame, text="Copy Encryption", command=self.copy_encrypt, font=("Arial", font_subtitles_entries))
        copy_encrypted__button.grid(row=8, column = 1, columnspan=1, pady=10, padx = (200,0), sticky=tk.W)


        # DECRYPTION SECTION
        self.decryption_frame = tk.Frame(self.window)
        self.decryption_frame.pack(side=tk.LEFT, padx=20, pady=50)

        # Create the title for the decryption section
        decryption_title = tk.Label(self.decryption_frame, text="Decryption Section", font=("Arial", font_size_title, "bold"))
        decryption_title.grid(row=0, columnspan=2, pady=20)

        ciphertext_label = tk.Label(self.decryption_frame, text="Ciphertext:", font=("Arial", font_subtitles_entries))
        ciphertext_label.grid(row=1, column=0, pady=20)

        self.ciphertext_entry = tk.Entry(self.decryption_frame, width=60, font=("Arial", font_size_entries))
        self.ciphertext_entry.grid(row=1, column=1, padx= (0, 20), sticky=tk.W)

        reverse_caesar_shift_label = tk.Label(self.decryption_frame, text="Caesar Shift Value:", font=("Arial", font_subtitles_entries))
        reverse_caesar_shift_label.grid(row=2, column=0, padx=10)

        self.reverse_caesar_shift_entry = tk.Entry(self.decryption_frame, width=5, font=("Arial", font_size_entries))
        self.reverse_caesar_shift_entry.grid(row=2, column=1, sticky=tk.W)

        reverse_hexacode_shift_label = tk.Label(self.decryption_frame, text="HexaCode Value:", font=("Arial", font_subtitles_entries))
        reverse_hexacode_shift_label.grid(row=3, column=0, padx=10)

        self.reverse_hexacode_entry = tk.Entry(self.decryption_frame, width=5, font=("Arial", font_size_entries))
        self.reverse_hexacode_entry.grid(row=3, column=1, sticky=tk.W)

        decrypt_button = tk.Button(self.decryption_frame, text="Decrypt", command=self.decrypt, font=("Arial", font_size_entries))
        decrypt_button.grid(row=4, columnspan=2, pady=10)

        after_reverse_hexacode_label = tk.Label(self.decryption_frame, text="Reverse HexaCode:", font=("Arial", font_subtitles_entries))
        after_reverse_hexacode_label.grid(row=5, column=0, padx=10)

        self.after_reverse_hexacode_entry = tk.Entry(self.decryption_frame, width=60, font=("Arial", font_size_entries))
        self.after_reverse_hexacode_entry.grid(row=5, column=1, padx=(0, 20), sticky=tk.W)
        self.after_reverse_hexacode_entry.config(state="disabled")

        hexa_to_text_label = tk.Label(self.decryption_frame, text="Hexadecimal to Text:", font=("Arial", font_subtitles_entries))
        hexa_to_text_label.grid(row=6, column=0, padx=10)

        self.hexa_to_text_entry = tk.Entry(self.decryption_frame, width=60, font=("Arial", font_size_entries))
        self.hexa_to_text_entry.grid(row=6, column=1, padx=(0, 20), sticky=tk.W)
        self.hexa_to_text_entry.config(state="disabled")

        after_reverse_caesar_shift_label = tk.Label(self.decryption_frame, text="Reverse Caesar Shift:", font=("Arial", font_subtitles_entries))
        after_reverse_caesar_shift_label.grid(row=7, column=0, padx=10)

        self.after_reverse_caesar_entry = tk.Entry(self.decryption_frame, width=60, font=("Arial", font_size_entries))
        self.after_reverse_caesar_entry.grid(row=7, column=1, padx=(0, 20), sticky=tk.W)
        self.after_reverse_caesar_entry.config(state="disabled")

        decrypt_clear_button = tk.Button(self.decryption_frame, text="Clear Section", command=self.clear_decrypt, font=("Arial", font_subtitles_entries))
        decrypt_clear_button.grid(row=8, column = 1, columnspan=1, pady=10, sticky=tk.W)

        copy_decrypted__button = tk.Button(self.decryption_frame, text="Copy Decryption", command=self.copy_decrypt, font=("Arial", font_subtitles_entries))
        copy_decrypted__button.grid(row=8, column = 1, columnspan=1, pady=10, padx = (200,0), sticky=tk.W)

    def clear_entry(self, entry,  mode=0):
        if mode == 1:
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.config(state="disabled")
        else:
            entry.delete(0, tk.END)

    def set_text(self, entry,text, mode=0):
        if mode == 1:
            entry.config(state="normal")
            entry.insert(tk.END, text)
            entry.config(state="disabled")
        else:
            entry.insert(tk.END, text)

    def clear_encrypt(self):
        self.clear_entry(self.plaintext_entry)
        self.clear_entry(self.caesar_shift_entry)
        self.clear_entry(self.hexacode_entry)
        self.clear_entry(self.after_caesar_entry, mode=1)
        self.clear_entry(self.after_hexacode_entry, mode=1)
        self.clear_entry(self.caesar_to_hexa_entry, mode=1)

    def clear_decrypt(self):
        self.clear_entry(self.ciphertext_entry)
        self.clear_entry(self.reverse_caesar_shift_entry)
        self.clear_entry(self.reverse_hexacode_entry)
        self.clear_entry(self.after_reverse_caesar_entry, mode=1)
        self.clear_entry(self.after_reverse_hexacode_entry, mode=1)
        self.clear_entry(self.hexa_to_text_entry, mode=1)

    def encrypt(self):
        self.clear_entry(self.after_caesar_entry, mode=1)
        self.clear_entry(self.after_hexacode_entry, mode=1)
        self.clear_entry(self.caesar_to_hexa_entry, mode=1)

        try:
            shift = int(self.caesar_shift_entry.get())
            hexa = self.hexacode_entry.get()
        except:
            messagebox.showerror("VALUE ERROR", "Caesar Shift or Hexacode Value not valid. Please try again")
        else:
            text_to_encrypt = self.plaintext_entry.get()
            Is_valid = self.cypdec.check_input(text_to_encrypt)

            if (Is_valid[0] == True):
                #SEND TO ENCRYPTION
                encrypted = self.cypdec.encrypt(text_to_encrypt, shift, hexa)
                self.set_text(self.after_caesar_entry, encrypted[0], mode=1)
                self.set_text(self.caesar_to_hexa_entry, encrypted[1], mode=1)
                self.set_text(self.after_hexacode_entry, encrypted[2], mode=1)

            else:
                message = "The input value has some not permitted characters"
                messagebox.showerror("ERROR", message)


    def decrypt(self):
        self.clear_entry(self.after_reverse_caesar_entry, mode=1)
        self.clear_entry(self.after_reverse_hexacode_entry, mode=1)
        self.clear_entry(self.hexa_to_text_entry, mode=1)

        try:
            shift = int(self.reverse_caesar_shift_entry.get())
            hexa = self.reverse_hexacode_entry.get()
        except:
            messagebox.showerror("VALUE ERROR", "Caesar Shift or Hexacode Value not valid. Please try again")
        else:
            text_to_decrypt = self.ciphertext_entry.get()
            Is_valid = self.cypdec.check_input(text_to_decrypt)

            if (Is_valid[0] == True):
                # SEND TO ENCRYPTION
                decrypted = self.cypdec.decrypt(text_to_decrypt, shift, hexa)
                self.set_text(self.after_reverse_hexacode_entry, decrypted[0], mode=1)
                self.set_text(self.hexa_to_text_entry, decrypted[1], mode=1)
                self.set_text(self.after_reverse_caesar_entry, decrypted[2], mode=1)

            else:
                message = "The input value has some not permitted characters"
                messagebox.showerror("ERROR", message)


    def copy_encrypt(self):
        text = self.after_hexacode_entry.get()
        if text.strip() == "":
            messagebox.showwarning("EMPTY VALUE", "There is nothing to be copied")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("SUCCESFULL", "Encrypted text has been succesfully copied")

    def copy_decrypt(self):
        text = self.after_reverse_caesar_entry.get()
        if text.strip() == "":
            messagebox.showwarning("EMPTY VALUE", "There is nothing to be copied")
        else:
            pyperclip.copy(text)
            messagebox.showinfo("SUCCESFULL", "Encrypted text has been succesfully copied")


