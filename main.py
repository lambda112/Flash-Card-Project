from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

# Window
root = Tk()
root.title("Flash Cards")

# New Window
class FlashName(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        # Label 
        self.title("Flash Card Name")
        window_title = Label(self, text = "Name of Flash Card")
        window_title.grid(column=0, row=0, sticky="ew")

        # Entry
        self.config(padx=40, pady=40)
        self.name_flash = Entry(self)
        self.name_flash.grid(column=0, row=1, sticky="ew")

        # Button
        self.confirm_button = Button(self, text = "Confirm", height=2, width = 10, command=self.get_flash_name)
        self.confirm_button.grid(column=0, row = 2, sticky="ew")

    def get_flash_name(self):
        """Get name of flashcard user wants to create if already exists show error message otherwise create txt file"""
        # Check if flash card folder exists
        if not os.path.isdir("flashcards"):
            os.makedirs("flashcards")

        # Get name of clash card
        name_flash = f"{self.name_flash.get()}.txt"

        # Check if name of flash card already exists if so show message
        if os.path.isfile(f"flashcards\\{name_flash}"):  
            messagebox.showerror(title="ERROR", message="flash card already exists.")

        # Create new flashcard as txt file and destroy window
        else:
            with open(f"flashcards\\{name_flash}", "w"):
                pass
            self.destroy()

    
# Function
def create_entry_window():
    window = FlashName()

# Canvas 
img = ImageTk.PhotoImage(Image.open("note.png"))
canvas = Canvas(root, height = 400, width = 400)
canvas.grid(column=0, row=0)

# Canvas Widgets
canvas.create_image(200, 200, image = img)
canvas.create_text(204, 50, text="FLASH CARD", font=("arial", 25, "bold"), fill="purple")

# Buttons 
add_flash = Button(text = "Create Card", width=20, height = 5, bg = "orange", fg = "purple", command=create_entry_window)
open_flash = Button(text = "Open Card", width = 20, height = 5, bg = "orange", fg = "purple")
canvas.create_window(100, 350, window=add_flash)
canvas.create_window(305, 350, window=open_flash)

root.mainloop()