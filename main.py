from GUI import CipherToolGUI
import tkinter as tk




def start():
    window = tk.Tk()
    gui = CipherToolGUI(window)

    window.mainloop()


if __name__ == '__main__':
    start()
