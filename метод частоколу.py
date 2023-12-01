import tkinter as tk

window = tk.Tk()
label = tk.Label()
label.pack()

entry = tk.Entry(fg='black', bg='grey', width=10)
entry.pack()
entry1 = tk.Entry(fg='black', bg='grey', width=10)
entry1.pack()



def click():
    script = ""  # Global variable
    key =int(entry1.get())
    text = entry.get()
    list_text = list(text)
    length = len(list_text)

    while key > 0:
        count = 0
        while count < len(list_text):
            numberOfLetters = count + 1
            if numberOfLetters % key == 0:
                if (list_text[count] != 0):
                    script += list_text[count]
                list_text[count] = 0
            count += 1
        key -= 1

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
