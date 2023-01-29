import tkinter


def change_name():
    character_name["text"] = f"Character 1: {input.get().upper()}"
    input.delete(0, "end")


window = tkinter.Tk()
window.title("D&D Character Sheet")
window.minsize(width=500, height=300)

character_name = tkinter.Label(
    text="Character 1: IRB", font=("Arial", 24, "bold"))
character_name.place(x=0, y=0)

charactar_stats = tkinter.Label(
    text="Strength: 10\n\nIntelligence: 100\n\nStamina: 10\n\nCharisma: 100\n\nLuck: 10",
    font=("Arial", 15))
charactar_stats.pack(side="right", expand=True)

button = tkinter.Button(text="Change Name", command=change_name)
button.place(x=0, y=230)

input = tkinter.Entry(width=15)
input.place(x=0, y=200)


window.mainloop()
