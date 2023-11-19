import tkinter as tk

window = tk.Tk()
label = tk.Label()
label.pack()

entry = tk.Entry(fg='black', bg='grey', width=10)
entry.pack()
entry1 = tk.Entry(fg='black', bg='grey', width=10)
entry1.pack()

script = ""  # Global variable

def click():
    global script  # Declare script as a global variable
    script = ""
    text = entry.get()
    text_list = list(text)
    key = 2  # No need to convert it to int('2') again
    step = int(entry1.get())
    for i in range(len(text)):
        if (i + 1) % step == 0 and text_list[i] != '0':
            script += text_list[i]
        text_list[i] = "0"
    print(script)

button = tk.Button(
    text="chpoink",
    width=15,
    height=5,
    bg="red",
    fg="white",
    command=click
)
button.pack()
window.mainloop()
