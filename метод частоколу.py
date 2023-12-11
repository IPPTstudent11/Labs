import tkinter as tk

window = tk.Tk()
label = tk.Label()
label.pack()

entry = tk.Entry(fg='black', bg='grey', width=100, font=("Arial", 18))
entry.pack()
entry1 = tk.Entry(fg='black', bg='grey', width=100, font=("Arial", 18))
entry1.pack()

result_label = tk.Label(window, text="", fg="black", font=("Arial", 18))  # Зміна розміру шрифту
result_label.pack()

def click():
    global script
    script = ""
    key = int(entry1.get())
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

    result_label.configure(text=script)  # Оновлення тексту у вікні з результатом

button = tk.Button(
    text="chpoink",
    width=100,
    height=50,
    font=("Arial", 18),
    bg="red",
    fg="white",
    command=click
)
button.pack()
window.mainloop()
