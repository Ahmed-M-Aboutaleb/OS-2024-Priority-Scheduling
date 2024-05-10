import tkinter as tk
from classes import Application as App

def main():
    root = tk.Tk()
    app = App.Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()