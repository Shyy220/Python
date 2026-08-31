import tkinter as tk

window = tk.Tk()
window.title("GUI")
window.geometry("400x400")

label= tk.Label(window, text="welcome to GUI")
label.pack()

entry = tk.Entry(window)
entry.pack()



def show_name():
    name=entry.get()
    print("hello", name)
    print("welcome shyamsundar", name)
    print("how are you?", name)

button = tk.Button(window, text="submit", command = show_name)
button.pack()

textbox=tk.Text(window, height=5, width=30)
textbox.pack()

window.mainloop()