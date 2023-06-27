import tkinter as tk
from Cipher_Decipher import Cypher_Decypher
from PIL import Image, ImageTk

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


        # ENCRYPTION SECTION
        self.encryption_frame = tk.Frame(self.window)
        self.encryption_frame.pack(side=tk.LEFT, padx=20, pady=50)

        encryption_title = tk.Label(self.encryption_frame, text="Encryption Section", font=("Arial", 24, "bold"))
        encryption_title.grid(row=0, columnspan=2, pady=20)

        plaintext_label = tk.Label(self.encryption_frame, text="Plaintext:", font=("Arial", 18))
        plaintext_label.grid(row=1, column=0, pady=20)

        self.plaintext_entry = tk.Entry(self.encryption_frame, width=30, font=("Arial", 20))
        self.plaintext_entry.grid(row=1, column=1, padx= (0, 20), sticky=tk.W)

        caesar_shift_label = tk.Label(self.encryption_frame, text="Caesar Shift Value:", font=("Arial", 18))
        caesar_shift_label.grid(row=2, column=0, padx=10)

        self.caesar_shift_entry = tk.Entry(self.encryption_frame, width=5, font=("Arial", 15))
        self.caesar_shift_entry.grid(row=2, column=1, sticky=tk.W)

        hexacode_label = tk.Label(self.encryption_frame, text="HexaCode Value:", font=("Arial", 18))
        hexacode_label.grid(row=3, column=0, padx=10)

        self.hexacode_entry = tk.Entry(self.encryption_frame, width=5, font=("Arial", 15))
        self.hexacode_entry.grid(row=3, column=1, sticky=tk.W)

        encrypt_button = tk.Button(self.encryption_frame, text="Encrypt", command=self.cypdec.encrypt(), font=("Arial", 18))
        encrypt_button.grid(row=4, columnspan=2, pady=10)

        after_caesar_shift_label = tk.Label(self.encryption_frame, text="After Caesar Shift:", font=("Arial", 18))
        after_caesar_shift_label.grid(row=5, column=0, padx=10)

        self.after_caesar_entry = tk.Entry(self.encryption_frame, width=30, font=("Arial", 20))
        self.after_caesar_entry.grid(row=5, column=1, padx=(0, 20), sticky=tk.W)
        self.after_caesar_entry.config(state="disabled")

        after_hexacode_label = tk.Label(self.encryption_frame, text="After HexaCode:", font=("Arial", 18))
        after_hexacode_label.grid(row=6, column=0, padx=10, pady=15)

        self.after_hexacode_entry = tk.Entry(self.encryption_frame, width=30, font=("Arial", 20))
        self.after_hexacode_entry.grid(row=6, column=1, padx=(0, 20), sticky=tk.W, pady=15)
        self.after_hexacode_entry.config(state="disabled")

        encrypt_clear_button = tk.Button(self.encryption_frame, text="Clear Section", command=self.clear_encrypt(), font=("Arial", 18))
        encrypt_clear_button.grid(row=7, columnspan=2, pady=10)


        # DECRYPTION SECTION
        self.decryption_frame = tk.Frame(self.window)
        self.decryption_frame.pack(side=tk.LEFT, padx=20, pady=50)

        # Create the title for the decryption section
        decryption_title = tk.Label(self.decryption_frame, text="Decryption Section", font=("Arial", 24, "bold"))
        decryption_title.grid(row=0, columnspan=2, pady=20)

        ciphertext_label = tk.Label(self.decryption_frame, text="Ciphertext:", font=("Arial", 18))
        ciphertext_label.grid(row=1, column=0, pady=20)

        self.ciphertext_entry = tk.Entry(self.decryption_frame, width=30, font=("Arial", 20))
        self.ciphertext_entry.grid(row=1, column=1, padx= (0, 20), sticky=tk.W)

        reverse_caesar_shift_label = tk.Label(self.decryption_frame, text="Caesar Shift Value:", font=("Arial", 18))
        reverse_caesar_shift_label.grid(row=2, column=0, padx=10)

        self.reverse_caesar_shift_entry = tk.Entry(self.decryption_frame, width=5, font=("Arial", 18))
        self.reverse_caesar_shift_entry.grid(row=2, column=1, sticky=tk.W)

        reverse_hexacode_shift_label = tk.Label(self.decryption_frame, text="HexaCode Value:", font=("Arial", 18))
        reverse_hexacode_shift_label.grid(row=3, column=0, padx=10)

        self.reverse_hexacode_entry = tk.Entry(self.decryption_frame, width=5, font=("Arial", 18))
        self.reverse_hexacode_entry.grid(row=3, column=1, sticky=tk.W)

        decrypt_button = tk.Button(self.decryption_frame, text="Decrypt", command=self.cypdec.decrypt(), font=("Arial", 18))
        decrypt_button.grid(row=4, columnspan=2, pady=10)

        after_reverse_hexacode_label = tk.Label(self.decryption_frame, text="Reverse HexaCode:", font=("Arial", 18))
        after_reverse_hexacode_label.grid(row=6, column=0, padx=10)

        self.after_reverse_hexacode_entry = tk.Entry(self.decryption_frame, width=30, font=("Arial", 20))
        self.after_reverse_hexacode_entry.grid(row=5, column=1, padx=(0, 20), sticky=tk.W, pady=15)
        self.after_reverse_hexacode_entry.config(state="disabled")

        after_reverse_caesar_shift_label = tk.Label(self.decryption_frame, text="Reverse Caesar Shift:", font=("Arial", 18))
        after_reverse_caesar_shift_label.grid(row=5, column=0, padx=10, pady=15)

        self.after_reverse_caesar_entry = tk.Entry(self.decryption_frame, width=30, font=("Arial", 20))
        self.after_reverse_caesar_entry.grid(row=6, column=1, padx=(0, 20), sticky=tk.W)
        self.after_reverse_caesar_entry.config(state="disabled")

        decrypt_clear_button = tk.Button(self.decryption_frame, text="Clear Section", command=self.clear_encrypt(), font=("Arial", 18))
        decrypt_clear_button.grid(row=7, columnspan=2, pady=10)


    def clear_encrypt(self):
        pass

    def clear_decrypt(self):
        pass

