import tkinter


def change_name():
    character_name["text"] = f"Character 1: {input.get().upper()}"
    input.delete(0, "end")


def change_name2():
    character_name2["text"] = f"Character 2: {input2.get().upper()}"
    input2.delete(0, "end")


window = tkinter.Tk()
window.title("D&D Character Sheet")
window.minsize(width=500, height=300)
window.config(padx=20, pady=10)

character_name = tkinter.Label(
    text="Character 1: IRB", font=("Arial", 18, "bold"))
character_name.config(padx=10)
character_name.grid(column=0, row=0)

charactar_stats = tkinter.Label(
    text="Strength: 10\n\nIntelligence: 100\n\nStamina: 10\n\nCharisma: 100\n\nLuck: 10",
    font=("Arial", 15))
charactar_stats.grid(column=0, row=2)

button = tkinter.Button(text="Change Name", command=change_name)
button.grid(column=0, row=4)

input = tkinter.Entry(width=15)
input.grid(column=0, row=3)

character_name2 = tkinter.Label(
    text="Character 2: DAN", font=("Arial", 18, "bold"))
character_name2.grid(column=1, row=0)

charactar_stats2 = tkinter.Label(
    text="Strength: 10\n\nIntelligence: 100\n\nStamina: 10\n\nCharisma: 100\n\nLuck: 10",
    font=("Arial", 15))
charactar_stats2.grid(column=1, row=2)

button2 = tkinter.Button(text="Change Name", command=change_name2)
button2.grid(column=1, row=4)

input2 = tkinter.Entry(width=15)
input2.grid(column=1, row=3)


window.mainloop()
