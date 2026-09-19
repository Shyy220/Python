from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("My Letter Writer")
window.geometry("600x400")

text = Text(window, width=70, height=20)
text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def open_letter():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        text.delete("1.0", END)
        file = open(filename, "r")
        text.insert("1.0", file.read())
        file.close()

def save_letter():
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        file = open(filename, "w")
        file.write(text.get("1.0", END))
        file.close()

open_button = Button(window, text="Open Letter", command=open_letter)
open_button.grid(row=1, column=0, padx=10, pady=10)

save_button = Button(window, text="Save Letter", command=save_letter)
save_button.grid(row=1, column=1, padx=10, pady=10)

clear_button = Button(
    window,
    text="Clear",
    command=lambda: text.delete("1.0", END)
)
clear_button.grid(row=1, column=2, padx=10, pady=10)

window.mainloop()