"""Application entry point for Property Rental Management System."""
import tkinter as tk
from GUI.login_gui import LoginGUI


def main():
    root = tk.Tk()
    LoginGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
